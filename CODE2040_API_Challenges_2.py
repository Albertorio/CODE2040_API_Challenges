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

#get dictionary
data = {}
data['token'] = token
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/haystack", json_data)
result = r.json()
dictionary = result['result']

#get needle and array from dictionary
needle = dictionary['needle']
array = dictionary['haystack']

#get the position of the needle
pos = array.index(needle)

#send position
data = {}
data['token'] = token
data['needle'] = pos
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/validateneedle", json_data)

#print result
print r.text
