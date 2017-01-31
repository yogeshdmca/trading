

from django.conf.urls import url, include

from .views import (AccountBalanceReportUpdate, )
from .ajax import *

urlpatterns = [
    url(r'^accounts/balance/report/$', AccountBalanceReportUpdate.as_view(), name='accounts-balance-report'),
    url(r'^accounts/subscribe/autotrade/$', subscribe_autotrade, name='accounts-balance-report'),
    ]


