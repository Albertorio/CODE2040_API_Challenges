import requests
import json
import datetime
import time
from datetime import timedelta

#register
data = {}
data['github'] = 'https://github.com/Albertorio/CODE2040_API_Challenges'
data['email'] = 'luisalbertorio21@gmail.com'
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/register", json_data)

#get token
result = r.json()
token = result["result"]

#get dictionary
data = {}
data['token'] = token
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/status", json_data)
print r.text