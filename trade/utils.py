import json
from websocket import create_connection
from django.utils import timezone

def update_balance_by_socket(profile,cls):
    ws = create_connection("wss://ws.binaryws.com/websockets/v3")
    json_data = json.dumps({'authorize':profile.token})
    ws.send(json_data)
    result =  ws.recv()
    result= json.loads(result)
    if result.get('msg_type',None) =="authorize":
        balance = result['authorize']['balance']
        currency = result['authorize']['currency']
        cls.objects.create(amount=balance,profile=profile)
        profile.balance_updated_at = timezone.now()
        profile.balance = balance
        profile.currency = currency
        profile.save()
        return True
    return False