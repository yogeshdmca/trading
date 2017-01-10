from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required, permission_required
from .views import HomeView, FaqView


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^faq/$', login_required(FaqView.as_view()), name='faq'),
]