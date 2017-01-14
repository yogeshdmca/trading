from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    balance =  models.FloatField("Account  Balance",default=0.0)
    phone =  models.CharField("Phone",max_length=12,null=True, blank=True)
    alternet_email = models.CharField("Alternet Email ",max_length=100,null=True, blank=True)
    account_id = models.CharField("Broker account Id ",max_length=200,null=True, blank=True)

    @property
    def bid_amount(self):
    	return (self.balance*5)/100


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()