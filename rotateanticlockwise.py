import requests
import json

def send_rpc_request(method, params, rpc_id=1):
    url = "http://192.168.149.1:9030"
    headers = {"Content-Type": "application/json"}
    payload = {
    "method":"Move",
    "params":[2, 0, -20, 200, 2],
    #<mode>, <movement_direction>, <rotation>, <speed>, <times> 
    "jsonrpc" : "2.0", 
    "id": 1 
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Example usage
response = send_rpc_request("Move", [2, 0, -20, 200, 2], rpc_id=1)
print(response)
