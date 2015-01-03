import requests
import json

#register
data = {}
data['github'] = 'https://github.com/Albertorio/CODE2040_API_Challenges'
data['email'] = 'luisalbertorio21@gmail.com'
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/register", json_data)

#get token
result = r.json()
token = result["result"]

#get string
data = {}
data['token'] = token
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/getstring", json_data)
result = r.json()
word = result['result']

#reverse string using extended slice
reverse_word = word[::-1]

#send reversed string
data = {}
data['token'] = token
data['string'] = reverse_word
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/validatestring", json_data)

#print result
print r.text

