

from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

from .views import (UserProfile,UserDashbord,UserBimaryData, 
                      check_profile,SignalListing, 
                      AccountBinaryHelp, UserAuthorize,
                      )


from .ajax import *


urlpatterns = [
    url(r'^accounts/profile/$', check_profile, name='accounts-profile'),
    url(r'^accounts/settings/$', UserProfile.as_view(), name='accounts-settings'),
    url(r'^accounts/authorize/$', UserAuthorize.as_view(), name='accounts-authorize'),
    
    url(r'^accounts/dashbord/$', RedirectView.as_view(url=reverse_lazy('accounts-dashbord'), permanent=True)),
    url(r'^accounts/dashboard/$', UserDashbord.as_view(), name='accounts-dashbord'),
    url(r'^accounts/binary_responce/', UserBimaryData.as_view(), name='accounts-binary-responce'),
    
    
    url(r'^accounts/signals/$', SignalListing.as_view(), name='accounts-signal-listing'),
    url(r'^accounts/binary/help/$', AccountBinaryHelp.as_view(), name='accounts-need-help'),
]

urlpatterns += [
    url(r'^accounts/update/binary_balance/', update_binary_balance, name='update-binary-balance'),
    
]


