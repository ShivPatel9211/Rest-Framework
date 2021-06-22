import requests
import json
URL = 'http://localhost:8000/studentapi/'


def update_data():
    data = {
        'id':5,
        'name':'Patel',
        'roll':104,
        'city': 'Balinagar'
    }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}

    res = requests.put(url=URL,headers=headers,data=json_data)
    json_data = res.json()
    print(json_data)
update_data()
