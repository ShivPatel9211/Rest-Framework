import requests
import json
URL = 'http://localhost:8000/studentapi/'

def get_data(id = None):
    data={}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.get(url=URL,headers=headers,data=json_data)
    json_data = res.json()
    print(json_data)
get_data(1)
