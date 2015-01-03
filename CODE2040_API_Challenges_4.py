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
r = requests.post("http://challenge.code2040.org/api/time", json_data)
result = r.json()
dictionary = result['result']

print dictionary

#get datestamp and interval
date = dictionary['datestamp']
interval = dictionary['interval']

#change seconds to timedelta (days, hours:min:sec)
new_date = timedelta(seconds=interval)

#split datestamp into date and time
date_arr = date.split("T")

#split date into year, month, day
real = date_arr[0].split('-')

#split time into hour, min, sec
for i in date_arr[1].split(':'):
	real.append(i)

#create datetime object 
datetime1 = datetime.date(int(real[0]), int(real[1]), int(real[2]))

#get the time from datestamp
new_time = str(real[3]) + ":" + str(real[4]) + ":00" 

#change time from datestamp to seconds
x = time.strptime(new_time,'%H:%M:%S')
y = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()

#change seconds to timedelta (days, hours:min:sec)
z = timedelta(seconds=y)

#add timedeltas to get 'final date' 
final_date = new_date + z

a = str(final_date)
b = a.split(', ')[1]

#add 'final date' and datetime object to get real final date
c = datetime1 + final_date
d = str(c)

#print initial date
print date

#concatenate strings to get iso 8601 datestamp
end = d + 'T' + b + '.000Z'

#print final date
print end

#send new array
data = {}
data['token'] = token
data['datestamp'] = end
json_data = json.dumps(data)
r = requests.post("http://challenge.code2040.org/api/validatetime", json_data)

#print results
print r.text

