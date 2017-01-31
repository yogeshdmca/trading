from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from django.utils import timezone
import json

@csrf_exempt
def update_binary_balance(request):
    profile = request.user.profile
    #if timezone.now()-timedelta(days=1) > profile.balance_updated_at :
    profile.balance = request.POST.get('balance')
    profile.currency = request.POST.get('currency')
    profile.balance_updated_at = timezone.now()
    profile.save()
    return HttpResponse(json.dumps({'result':'true'}))
