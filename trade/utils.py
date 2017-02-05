import json
from websocket import create_connection
from django.utils import timezone

def update_balance_by_socket(profile,cls):
    if not profile.token and not profile.account_id:
        return False
    ws = create_connection("wss://ws.binaryws.com/websockets/v3")
    json_data = json.dumps({'authorize':profile.token})
    ws.send(json_data)
    result =  ws.recv()
    result= json.loads(result)
    print (result)
    if result.get('msg_type',None) =="authorize":
        try:
            balance = result['authorize']['balance']
            currency = result['authorize']['currency']
            cls.objects.create(amount=balance,profile=profile)
            profile.balance_updated_at = timezone.now()
            profile.balance = balance
            profile.currency = currency
            profile.save()
        except Exception as exp:
            from .models import ErrorLog
            ErrorLog.objects.create(user= profile, error=exp, log=json.dumps(result))
        return True
    return False

def trade_now(profile,trade):
    try:
        print (profile,profile.currency,profile.bid_amount)
        ws = create_connection("wss://ws.binaryws.com/websockets/v3")
        json_data = json.dumps({'authorize':profile.token})
        ws.send(json_data)
        result =  ws.recv()
        proposal = {
                      "proposal": 1,
                      "amount": str(profile.bid_amount),
                      "basis": "payout",
                      "contract_type":trade.get_contract_type,
                      "currency": profile.currency,
                      "duration": trade.expire_in.get_time,
                      "duration_unit": trade.expire_in.get_unit,
                      "symbol": trade.currency.pair_name
                    }
        proposal_data = json.dumps(proposal)
        ws.send(proposal_data)
        val = json.loads(ws.recv())
	try:
            contract_id = val['proposal']['id']
            price = val['proposal']['payout']
        except:
            from .models import ErrorLog
            ErrorLog.objects.create(user= profile, error=trade, log=json.dumps(val))
            return False
        buy_contract = {
            'buy':contract_id,
            'price':price
        }
        contract_data = json.dumps(buy_contract)
        ws.send(contract_data)
        buy_data = json.loads(ws.recv())
        ws.close()
        return buy_data['buy']
    except Exception as exp:
        from .models import ErrorLog
        ErrorLog.objects.create(user= profile, error=trade, log=exp)
        return False
