from __future__ import unicode_literals

from django.db import models
from django.conf import settings

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

    def __str__(self):
        return self.name

class ExpireIN(models.Model):
    """docstring for ClassName"""
    unit = models.CharField("Expire Time Unit",max_length=20, choices=EXPIRE_IN)
    time = models.FloatField("Time",default=0.0)

    def __str__(self):
        return "%s %s"%(self.time,self.unit)

        

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