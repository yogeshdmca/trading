from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime , timedelta

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    balance =  models.FloatField("Account  Balance",default=0.0)
    currency = models.CharField("Currency",max_length=200,null=True, blank=True)
    balance_updated_at = models.DateTimeField(auto_now=True)
    phone =  models.CharField("Phone",max_length=12,null=True, blank=True)
    alternet_email = models.CharField("Alternet Email ",max_length=100,null=True, blank=True)
    account_id = models.CharField("Broker Real account Id ",max_length=200,null=True, blank=True)
    token  = models.CharField("Broker Real token ",max_length=200,null=True, blank=True)
    account_id2 = models.CharField("Broker virtual account Id ",max_length=200,null=True, blank=True)
    token2  = models.CharField("Broker virtual tocken",max_length=200,null=True, blank=True)

    @property
    def get_target_of_the_day(self):
        try:
            return (self.balance*10)/100
        except Exception, e:
            return 0.0

    @property
    def bid_amount(self):
        try:
            return (self.balance*5)/100
        except Exception, e:
            return 0.0


    @property
    def get_account_balance(self):
        if self.balance_updated_at > datetime.now()-timedelta(days=1):
            return True
        return False
    

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()