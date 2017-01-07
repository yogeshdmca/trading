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

    list_display = UserAdmin.list_display + ('balance','bid_amount')


admin.site.unregister(User)

admin.site.register(User, UserProfileAdmin)
