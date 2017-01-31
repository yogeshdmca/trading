from __future__ import unicode_literals
from datetime import datetime, timedelta
from django.utils import timezone
from django.db import models
from django.conf import settings
from accounts.models import Profile
from utils import trade_now

STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('in_active', 'InActive'),
        ('win', 'Win'),
        ('lose', 'Lose'),
    )

DIRECTION_CHOICES = (
        ('up', 'UP'),
        ('down', 'Down'),
    )


TRANSACTION_TYPE = (
        ('added', 'Added'),
        ('withdraw', 'Withdraw'),
        ('transfer', 'Transfer'),
        ('received', 'received'),
    )

EXPIRE_IN = (
        ('hours', 'Hours'),
        ('minuts', 'minuts'),
        ('seconds', 'Seconds'),
    )


class Currency(models.Model):
    """docstring for ClassName"""
    name = models.CharField("Currency Name", max_length=200)
    pair_name = models.CharField("Currency Name", max_length=200,null=True, blank=True)

    def __str__(self):
        return self.name

class ExpireIN(models.Model):
    """docstring for ClassName"""
    unit = models.CharField("Expire Time Unit",max_length=20, choices=EXPIRE_IN)
    time = models.FloatField("Time",default=0.0)

    def __str__(self):
        return "%s %s"%(self.time,self.unit)

    @property
    def get_time_in_minuts(self):
        if self.unit == 'hours':
            return int(self.time*60*60)
        if self.unit == 'seconds':
            return int(self.time)
        else:
            return int(self.time*60)

    @property
    def get_unit(self):
        if self.unit == 'hours':
            return 'h'
        if self.unit == 'seconds':
            return 's'
        else:
            return 'm'
        
    @property
    def get_time(self):
        return int(self.time)
        

class Signal(models.Model):
    """docstring for ClassName"""
    currency = models.ForeignKey(Currency, max_length=200)
    expire_in = models.ForeignKey(ExpireIN, max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    direction = models.CharField("Direction",max_length=20,choices=DIRECTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='0')


    def __str__(self):
        return "%s %s %s %s"%(self.currency,self.expire_in,self.direction,self.status)
    
    @property
    def get_contract_type(self):
        if self.direction == 'up':
            return 'CALL'
        if self.direction == 'down':
            return 'PUT'

    @property
    def is_visible(self):
            return timezone.now() < self.created_at+timedelta(seconds=self.expire_in_seonds)
    @property
    def expire_in_seonds(self):
        return self.expire_in.get_time_in_minuts/8.0
    @property
    def get_expire_time(self):
        time_ago = int((timezone.now()- self.created_at).total_seconds())
        return (self.expire_in.get_time_in_minuts/8.0)-time_ago


class AutoTrade(models.Model):
    """docstring for ClassName"""

    profile = models.OneToOneField(Profile, related_name='auto_trades')
    active = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "%s %s"%(self.profile, self.active)

class AutoTradeHistory(models.Model):
    profile = models.ForeignKey(Profile, related_name="auto_trade_histories")
    signal = models.ForeignKey(Signal, related_name='auto_trade_histories')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    payout = models.CharField("Payout", max_length=100)
    payout = models.CharField("Payout", max_length=100)
    contract_id = models.CharField("contract_id", max_length=500)
    longcode = models.CharField("longcode", max_length=5000)
    buy_price = models.CharField("buy_price", max_length=100)
    balance_after = models.CharField("balance_after", max_length=100)
    shortcode = models.CharField("shortcode", max_length=100)
    transaction_id = models.CharField("transaction_id", max_length=100)
    purchase_time = models.CharField("purchase_time", max_length=100)
    start_time = models.CharField("start_time", max_length=100)



class UserBalanceInfo(models.Model):
    """docstring for ClassName"""
    profile = models.ForeignKey(Profile,related_name = 'balances')
    updated_at = models.DateField(auto_now=True)
    amount = models.FloatField("Bid amount",default=0.0)

    def __str__(self):
        return "%s %s"%(self.profile, self.amount)

    @property
    def previous_balance(self):
        previous_entry = type(self).objects.filter(profile = self.profile)
        if len(previous_entry)>1 :
            return (previous_entry[1].amount, previous_entry.last().amount-previous_entry.first().amount)
        return (0.0, 0.0)


class SignalBid(models.Model):
    """docstring for ClassName"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    signal = models.ForeignKey(Signal, related_name='bids')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField("Status",max_length=20, choices=STATUS_CHOICES)
    bid_amount = models.FloatField("Bid amount",default=0.0)


class Transaction(models.Model):
    """docstring for ClassName"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='transaction')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    amount = models.FloatField("Bid amount",default=0.0)
    type = models.CharField("Transaction Type",max_length=50, choices=TRANSACTION_TYPE)


class ErrorLog(models.Model):
    user = models.ForeignKey(Profile, related_name='transaction')
    error = models.TextField("Error Type")
    log = models.TextField("Error Log")

from django.db.models.signals import post_save
from django.dispatch import receiver


from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
from django.template.loader import render_to_string

@receiver(post_save, sender=Signal, dispatch_uid="new_signal_created")
def update_stock(sender, instance, **kwargs):
        if instance.status!='active':
            instance = False
        row =  render_to_string('dashbord/shared/active_signal_trade.html',{'active_singal':instance})
        redis_publisher = RedisPublisher(facility='active_signal', broadcast=True)
        message = RedisMessage(row)
        redis_publisher.publish_message(message)
        auto_trade_users = AutoTrade.objects.filter(active=True)

        if instance:
            for auto in auto_trade_users:
                data = trade_now(auto.profile, instance)
                if data:
                    AutoTradeHistory.objects.create(profile=auto.profile, signal=instance, **data)


