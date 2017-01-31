from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.utils import timezone
import json

from .models import AutoTrade

@csrf_exempt
def subscribe_autotrade(request):
    in_auto_trade = AutoTrade.objects.filter(profile=request.user.profile).last()
    if request.POST.get('value',False)=='true':
        if in_auto_trade:
            in_auto_trade.active=True
            in_auto_trade.save()
        else:
            AutoTrade.objects.create(profile = request.user.profile, active=True)
    else:
        if in_auto_trade:
            in_auto_trade.active=False
            in_auto_trade.save()

    return HttpResponse(json.dumps({'status':'true'}),status=201,content_type="application/json")