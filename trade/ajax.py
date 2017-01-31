from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.utils import timezone
import json

from .models import AutoTrade

@csrf_exempt
def subscribe_autotrade(request):
    last_trade = request.user.profile.auto_trades.all()
    if not last_trade :
        AutoTrade.objects.create(profile = request.user.profile, active=True)
    if last_trade.active is True:
         AutoTrade.objects.create(profile = request.user.profile, active=False)
    if last_trade.active is False:
        AutoTrade.objects.create(profile = request.user.profile, active=True)
    return HttpResponse(json.dumps({'status':'true'}),status=201,content_type="application/json")