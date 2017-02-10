# imports list of users in room, imports into array, then dumps into team. At this stage, team will be predefined
import json
import requests
#define authentication key -- add your own!
key = "" 
startRoom = ""
endTeam = ""

#This section -- get list of users in room

#define URL we're trying to hit
url = "https://api.ciscospark.com/v1/memberships"
#build the query, specifying the room you want to hit
querystring = {"roomId": startRoom}
#don't forget the headers, and use that authorisation we used earlier, american spelling tho
headers = {
    'authorization': key,
    'cache-control': "no-cache",
    'postman-token': "69a83b1c-b337-8e43-7f7b-5282386e3148"
    }
#send it using REST, capture the response
response = requests.request("GET", url, headers=headers, params=querystring)
#load the response into a dictionary, using Python's JSON parser
room_dict = json.loads(response.text)
#create a list to drop people's emails into
list = []
#drop the emails into a list
for room in room_dict['items']:
    list.append(room['personEmail'])
    
#now that we have the emails, lets put them into another room

#define URL we need to hit
url2 = "https://api.ciscospark.com/v1/team/memberships"
#build the headers again, not sure why we're using cache-control or postman-token, postman added them in
headers = {
	    'authorization': key,
	    'content-type': "application/json",
	    'cache-control': "no-cache",
	    'postman-token': "8499bb62-c358-b25e-2ad0-315be5cd80b2"
	    }
#now we've built the headers, lets loop through the emails in the list
for people in list:
	data = {#building the payload here, next line specifies the team youre migrating to
		'teamId':   endTeam,
	   	'personEmail': people #build the email into the payload
	   	}
	payload = json.dumps(data) #build the payload into JSON
	print payload #prints, just for validation
	response = requests.request("POST", url2, data=payload, headers=headers) #submits the request
	print response.status_code #prints a status code after every payload, 200 is good!
