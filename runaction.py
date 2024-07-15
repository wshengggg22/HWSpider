import requests
import json

def send_rpc_request(method, params, rpc_id=2):
    url = "http://192.168.149.1:9030"
    headers = {"Content-Type": "application/json"}
    payload = {
    "method":"RunAction",
    "params":[0,1],
    #<actName>, <times>
    "jsonrpc" : "2.0", 
    "id": 6
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

# Example usage
response = send_rpc_request("RunAction", [0,1], rpc_id=6)
print(response)
