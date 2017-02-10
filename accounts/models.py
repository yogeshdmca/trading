from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime , timedelta

ACCOUNT_STATUS_CHOICES = (
        ('real', 'Real Acount'),
        ('virtual', 'Virtual account'),
        ('new', 'Account not configured'),
    )

ACCOUNT_ERROR_CHOICES = (
        ('new', 'Need to Athenticate by binary.com for get trading working'),
        ('expire', 'Token Expired, Please thenticate again'),
        ('balance', 'Account having less balance, can not trade'),
        ('deactivated', 'Your account deactivated on binary.com'),
        ('real_account', 'Your Virtual account is Active only, need to activate real account and then authenticate again.'),
        ('ok', 'Everything are Good, Enjoy trading with IqOptionExperts'),
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    balance =  models.FloatField("Account  Balance",default=0.0)
    currency = models.CharField("Currency",max_length=200,null=True, blank=True)
    balance_updated_at = models.DateTimeField(null=True, blank=True)
    phone =  models.CharField("Phone",max_length=12,null=True, blank=True)
    alternet_email = models.CharField("Alternet Email ",max_length=100,null=True, blank=True)
    account_id = models.CharField("Broker Real account Id ",max_length=200,null=True, blank=True)
    token  = models.CharField("Broker Real token ",max_length=200,null=True, blank=True)
    account_id2 = models.CharField("Broker virtual account Id ",max_length=200,null=True, blank=True)
    token2  = models.CharField("Broker virtual tocken",max_length=200,null=True, blank=True)
    account_status = models.CharField(max_length=10, choices=ACCOUNT_STATUS_CHOICES,default='new')
    account_error = models.CharField(max_length=10, choices=ACCOUNT_ERROR_CHOICES,default='new')


    def __str__(self):
        return "%s %s"%(self.user.email, self.user)

    def get_token(self):
        return self.token
        
    def get_binary_account_type(self):
        if "CR" in self.account_id:
            return 'r'
        elif 'VR' in self.account_id :
            return 'v'
        elif 'VR' in self.account_id2:
            return 'v'
        else:
            return 'n'
            

    def is_auto_trade_active(self):
        try:
            return self.auto_trades.active
        except:
            return False

    @property
    def get_target_of_the_day(self):
        try:
            return (self.balance*10)/100
        except Exception, e:
            return 0.0

    @property
    def bid_amount(self):
        try:
            return int((self.balance*5)/100)
        except Exception, e:
            return 0.0

    @property
    def get_account_balance(self):
        if self.balance_updated_at > datetime.now()-timedelta(days=1):
            return True
        return False

    @property
    def is_verified(self):
        if self.account_id  and self.token:
            return True
        else:
            return False
    

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()