from django.conf.urls import url, include

from .views import HomeView, FaqView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^faq/$', FaqView.as_view(), name='faq'),
]