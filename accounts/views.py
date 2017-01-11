from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views import View
from .forms import *
from trade.models import Signal

# Create your views here.

@login_required
def check_profile(request):
    user = request.user
    try:
        profile = user.profile
        if profile.balance > 0:
            return HttpResponseRedirect(reverse('accounts-dashbord'))
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
            return HttpResponseRedirect(reverse('accounts-dashbord'))
        else:
            return render(request, self.template_name,{'user_form':user_form, 'profile':profile_form})
   



# class UserProfile(TemplateView):
#     template_name = "dashbord/profile.html"

class UserDashbord(LoginRequiredMixin,View):
    template_name = "dashbord/dashbord.html"

    def get(self, request):
        
        signals = Signal.objects.filter()[:5]
        active_singals = Signal.objects.filter(status='active')
        active_singal = active_singals and active_singals[0] or False
        return render(request, self.template_name,{'active_singal':active_singal,'signals':signals })


class SignalListing(LoginRequiredMixin,View):
    template_name = "dashbord/signal_listing.html"

    def get(self, request):
        lose_signals = Signal.objects.filter(status='lose')
        win_signals = Signal.objects.filter(status='win')
        return render(request, self.template_name,{'lose_signals':lose_signals,'win_signals':win_signals})
