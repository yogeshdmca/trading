from websocket import create_connection
import json
ws = create_connection("wss://ws.binaryws.com/websockets/v3")
json_data = json.dumps({'authorize':"a1-1dxYsVOc2xWnORkSrdVbFglF4kbxT"})
ws.send(json_data)
result =  ws.recv()
proposal = {
              "proposal": 1,
              "amount": "5",
              "basis": "payout",
              "contract_type":'CALL',
              "currency": 'USD',
              "duration": 60,
              "duration_unit": 's',
              "symbol": 'R_10'
            }
json_data = json.dumps(proposal)
ws.send(json_data)
val = json.loads(ws.recv())
contract_id = val['proposal']['id']
price = val['proposal']['payout']

buy_contract = {
	'buy':contract_id,
	'price':price
}

json_data = json.dumps(buy_contract)
ws.send(json_data)
val2 = json.loads(ws.recv())