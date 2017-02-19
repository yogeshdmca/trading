

from django.conf.urls import url, include

from .views import (AccountBalanceReportUpdate,ApiCreateTrade )
from .ajax import *

urlpatterns = [
	url(r'^api/create/trade/$', ApiCreateTrade.as_view(), name='api-create-trade'),
    url(r'^accounts/balance/report/$', AccountBalanceReportUpdate.as_view(), name='accounts-balance-report'),
    url(r'^accounts/subscribe/autotrade/$', subscribe_autotrade, name='accounts-subscribe-autotrade'),
    ]


