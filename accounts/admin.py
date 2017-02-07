from django.contrib import admin

from .models import Profile
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.



class UserProfileInline(admin.TabularInline):
    model = Profile


class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline, ]
    def balance(self, obj):
        try:
            return obj.profile.balance
        except Profile.DoesNotExist:
            return ''
    def bid_amount(self, obj):
        try:
            return obj.profile.bid_amount
        except Profile.DoesNotExist:
            return ''

    def binary_id(self, obj):
        try:
            return obj.profile.account_id
        except Profile.DoesNotExist:
            return ''

    def binary_token(self, obj):
        try:
            return obj.profile.token
        except Profile.DoesNotExist:
            return ''

    def phone(self, obj):
        try:
            return obj.profile.phone
        except Profile.DoesNotExist:
            return


    list_display = ('email','first_name','balance','bid_amount','binary_id','binary_token','phone','last_login')


admin.site.unregister(User)

admin.site.register(User, UserProfileAdmin)
