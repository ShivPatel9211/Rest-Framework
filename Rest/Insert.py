import requests
import json

URL = 'http://localhost:8000/createList/'
data = {
    'name':'Raj',
    'rollNo': '204',
    'city':'Raipur'
}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
res = r.json()
print(res)