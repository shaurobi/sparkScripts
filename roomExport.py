# imports list of users in room, imports into array, then dumps into team. At this stage, team will be predefined
import json
import requests

#get list of users in room


#define authentication key
key = "Bearer MGE4NTYzYTMtZmYzNi00Mzk4LTkyMGEtODgzZmNhYmVhYjJkZGRlYzI4NjctYjI3"
#define URL we're trying to hit
url = "https://api.ciscospark.com/v1/memberships"
#build the query
querystring = {"roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vNjNkZTE0MDAtODBhMC0xMWU2LTkzYjMtOTVhMjYxMjNlYTkx"}
#don't forget the headers
headers = {
    'authorization': "Bearer MGE4NTYzYTMtZmYzNi00Mzk4LTkyMGEtODgzZmNhYmVhYjJkZGRlYzI4NjctYjI3",
    'cache-control': "no-cache",
    'postman-token': "69a83b1c-b337-8e43-7f7b-5282386e3148"
    }
#capture the response
response = requests.request("GET", url, headers=headers, params=querystring)

#load the response into a dictionary, using Python's JSON parser
room_dict = json.loads(response.text)

#create a list to drop people's emails into
list = []
#drop the emails into a list
for room in room_dict['items']:
    list.append(room['personEmail'])
#EVERYTHING IS WORKING UP TO THIS POINT, HERE THERE BE DRAGONS
url2 = "https://api.ciscospark.com/v1/team/memberships"
headers = {
	    'authorization': "Bearer MGE4NTYzYTMtZmYzNi00Mzk4LTkyMGEtODgzZmNhYmVhYjJkZGRlYzI4NjctYjI3",
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "8499bb62-c358-b25e-2ad0-315be5cd80b2"
	    }

for people in list:
	data = {
		'teamId':   'Y2lzY29zcGFyazovL3VzL1RFQU0vMGY2ZGU4OTAtODBhMS0xMWU2LWFiNjAtMTEyMTljNzY4ZDc5',
	   	'personEmail': people
	   	}
	payload = json.dumps(data)
	print payload
	response = requests.request("POST", url2, data=payload, headers=headers)
	print response.status_code