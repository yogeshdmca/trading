from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Signal)

admin.site.register(SignalBid)

admin.site.register(Transaction)

admin.site.register(Currency)

admin.site.register(ExpireIN)

admin.site.register(UserBalanceInfo)

admin.site.register(AutoTrade)

admin.site.register(AutoTradeHistory)
admin.site.register(ErrorLog)








