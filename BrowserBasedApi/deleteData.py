import requests
import json
URL = 'http://localhost:8000/studentapi/'


def delete_data():
    data = {
        'id':4,
    }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    res = requests.delete(url=URL,headers=headers ,data=json_data)
    json_data = res.json()
    print(json_data)
delete_data()
