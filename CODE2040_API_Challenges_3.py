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
r = requests.post("http://challenge.code2040.org/api/prefix", json_data)
result = r.json()
dictionary = result['result']

#get prefix
prefix = dictionary['prefix']

#get array
array = dictionary['array']

#initialize new array
newArr=[]

#for each string in array, check the prefix, if prefix not present append to new array
for i in array:
	if i.startswith(prefix) == False:
		newArr.append(i)

#send new array
data = {}
data['token'] = token
data['array'] = newArr
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/validateprefix", json_data)

#print result
print r.text

