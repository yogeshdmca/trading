from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import *


class SignalAdmin(admin.ModelAdmin):
    list_display = ['currency', 'expire_in','direction','created_at','status']
    list_filter = (
        ('created_at', DateFieldListFilter),'status', 'currency'
    )
    ordering = ['created_at']

class AutoTradeHistoryAdmin(admin.ModelAdmin):
    list_display = ['profile', 'signal','updated_at','shortcode','buy_price','balance_after', 'longcode']
    ordering = ['updated_at']

class AutoTradeAdmin(admin.ModelAdmin):
    list_display = ['profile', 'active','updated_at']
    list_filter = ('active',)
    ordering = ['updated_at']

class AutoTradeErrorAdmin(admin.ModelAdmin):
    list_display = ['user', 'error','log']
    ordering = ['-id']


admin.site.register(Signal, SignalAdmin)

admin.site.register(SignalBid)

admin.site.register(Transaction)

admin.site.register(Currency)

admin.site.register(ExpireIN)

admin.site.register(UserBalanceInfo)

admin.site.register(AutoTrade, AutoTradeAdmin)

admin.site.register(AutoTradeHistory, AutoTradeHistoryAdmin)

admin.site.register(ErrorLog,AutoTradeErrorAdmin)








