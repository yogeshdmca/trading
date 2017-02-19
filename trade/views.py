from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import UserBalanceInfo, Currency, ExpireIN, Signal
from accounts.models import Profile
from django.utils import timezone
from utils import update_balance_by_socket
import json

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

class ApiCreateTrade(View):

    #@method_decorator(csrf_exempt)
    def get(self, request):
        vals = request.GET
        if vals.get('token') != '9926011586':
            return HttpResponse(status=404)
        currency_code = vals.get('currency_code', None)
        currency_name = vals.get('currency_name', None)
        time = vals.get('expire_time')
        unit = vals.get('expire_unit')
        direction = vals.get('direction')
        responce={'status':200}

        currency = currency_code and Currency.objects.get_or_create(pair_name=currency_code, name=currency_name)[0] or False
        expire_in = (time and unit) and ExpireIN.objects.get_or_create(unit=unit, time=time)[0] or False
        direction = direction in ['up','down'] and direction  or False

        if not currency:
            responce.update({'currency pair': 'invalid currency pair'})

        elif not expire_in:
            responce.update({'expire_in': 'invalid expire_in'})

        elif not direction:
            responce.update({'direction': 'invalid direction'})
        else:

            Signal.objects.create(currency=currency, expire_in=expire_in, direction=direction,user_id=1)
            responce.update({'saved': 'OK','autotrade':'procesing'})
        return HttpResponse(json.dumps(responce))



