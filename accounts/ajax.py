from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def update_binary_balance(request):
    profile = request.user.profile
    profile.balance = request.POST.get('balance')
    profile.currency = request.POST.get('currency')
    profile.save()
    return HttpResponse(json.dumps({'result':'true'}))
