import requests
import json


data = {}
data['github'] = 'https://github.com/Albertorio/CODE2040_API_Challenges'
data['email'] = 'luisalbertorio21@gmail.com'
json_data = json.dumps(data)

r = requests.post("http://challenge.code2040.org/api/register", json_data)

token = r.json()

print token["result"]