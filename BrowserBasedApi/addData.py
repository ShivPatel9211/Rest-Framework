import requests
import json
URL = 'http://localhost:8000/studentapi/'


def add_data():
    data = {
        'name': 'Patel',
        'roll': 104,
        'city': 'RamNagar',
    }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.post(url=URL,headers=headers, data=json_data)
    json_data = res.json()
    print(json_data)
add_data()
