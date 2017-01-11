

from django.conf.urls import url, include

from .views import UserProfile,UserDashbord, check_profile,SignalListing,latest_signal_ajax

urlpatterns = [
    url(r'^accounts/profile/$', check_profile, name='accounts-profile'),
    url(r'^accounts/settings/$', UserProfile.as_view(), name='accounts-settings'),
    url(r'^accounts/dashbord/$', UserDashbord.as_view(), name='accounts-dashbord'),
    url(r'^accounts/signals/$', SignalListing.as_view(), name='accounts-signal-listing'),
    
]


urlpatterns += [
    url(r'^accounts/signal-ajax/$', latest_signal_ajax, name='latest_signal-ajax'),
    
]

