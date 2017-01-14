from django import forms

from django.contrib.auth.models import User
from .models import Profile




class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar','balance','phone','alternet_email','account_id')
