from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from .models import UserBalanceInfo
from accounts.models import Profile
from django.utils import timezone
from utils import update_balance_by_socket

# Create your views here.
class AccountBalanceReportUpdate(LoginRequiredMixin,ListView):
    """docstring for UpdateBalance"""
    template_name = "dashbord/manager/account_balance_report.html"
    model = UserBalanceInfo

    #def get(self, request):
    #    return render(request, self.template_name,{})

    def post(self, request):
        profiles = Profile.objects.all()
        for profile in profiles:
            if profile.account_id and profile.token:
                update_balance_by_socket(profile, UserBalanceInfo)

        return HttpResponseRedirect(reverse('accounts-balance-report'))