from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from .forms import *
from trade.models import Signal
from datetime import datetime

# Create your views here.

@login_required
def check_profile(request):
    user = request.user
    try:
        profile = user.profile
        if profile.balance > 0:
            return HttpResponseRedirect(reverse('accounts-dashbord'))
        return HttpResponseRedirect(reverse('accounts-settings'))
    except:
        return HttpResponseRedirect(reverse('accounts-settings'))


class UserProfile(LoginRequiredMixin,View):
    template_name = "dashbord/profile.html"
    def get(self, request):
        user = request.user
        user_form = UserModelForm(instance=user)
        try:
            profile = request.user.profile
            profile_form = UserProfileForm(instance=profile)
            
        except:
            profile_form = UserProfileForm()
        return render(request, self.template_name,{'user_form':user_form, 'profile':profile_form})

    def post(self,request):
        user = request.user
        user_form = UserModelForm(request.POST,instance=user)
        try:
            profile = request.user.profile
            profile_form = UserProfileForm(request.POST,instance=profile)
            
        except:
            profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return HttpResponseRedirect(reverse('accounts-authorize'))
        else:
            return render(request, self.template_name,{'user_form':user_form, 'profile':profile_form})
   


class UserAuthorize(LoginRequiredMixin,View):
    template_name = "dashbord/login_by_binary.html"
    def get(self, request):
        APP_ID = settings.APP_ID
        return render(request, self.template_name,{'APP_ID':APP_ID})


class UserDashbord(LoginRequiredMixin,View):
    template_name = "dashbord/dashbord.html"

    def get(self, request):
        signals = Signal.objects.filter(status='active')
        active_singal = Signal.objects.filter(status='active').last()
        if active_singal and not active_singal.is_visible:
            active_singal = False

        return render(request, self.template_name,{'active_singal':active_singal,'signals':signals })

class UserBimaryData(LoginRequiredMixin,View):
    def get(self, request):
        url = request.path
        profile = request.user.profile
        import pdb;pdb.set_trace()
        try:
            profile.account_id = request.GET.get('acct1','')
            profile.token = request.GET.get('token1','')
            profile.account_id2 = request.GET.get('acct2','')
            profile.token2 = request.GET.get('token2','')
            profile.save()
        except:
            from urlparse import urlparse, parse_qs
            data_dict = parse_qs(urlparse(url).query)
            profile.account_id = data_dict.get('acct1','')
            profile.token = data_dict.get('token1','')
            profile.account_id2 = data_dict.get('acct2','')
            profile.token2 = data_dict.get('token2','')
        return HttpResponseRedirect(reverse('accounts-dashbord'))

class SignalListing(LoginRequiredMixin,View):
    template_name = "dashbord/signal_listing.html"
    def get(self, request):
        lose_signals = Signal.objects.filter(status='lose')
        win_signals = Signal.objects.filter(status='win')
        return render(request, self.template_name,{'lose_signals':lose_signals,'win_signals':win_signals})


def latest_signal_ajax(request):
    "Ajax call that will refress active signals"
    signals = Signal.objects.filter(status='active')
    active_singal = Signal.objects.filter(status='active').last()
    if active_singal and not active_singal.is_visible:
        active_singal = False

    return render(request, 'dashbord/includes/signal_dashbord.html',{'active_singal':active_singal,'signals':signals })


class AccountBinaryHelp(LoginRequiredMixin,TemplateView):
    template_name = "dashbord/binary_account_help.html"
        