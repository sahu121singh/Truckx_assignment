# Truckx_assignment

Technology used : Python Because, Python has the best framework and  is the best language to develop a RESTful API for any web-based applications.REST is a software architectural style that defines the set of rules to be used for creating web services. Web services which follow the REST architectural style are known as RESTful web services. It allows requesting systems to access and manipulate web resources by using a uniform and predefined set of rules. Interaction in REST based systems happen through Internet’s Hypertext Transfer Protocol


As mentioned each dash cam will have a unique identifier that is IMEI for identification so it means a IMEI will distinguish every dash cam from each other. 

Architecture

Entities : User [Dash Cam]
Attributes for User:
   -> USER _Name = EMIE
   -> Password 
   -> Recorded Videos over the DB
   -> Alarm Records

Alarm 
Attributes for Alarm:
 	-> Type of Alarm
-> Alarm time
	-> Latitude
	-> Longitude
-> File list 

There are four types of REST API’S

1. GET - Wherever we wish to get the data/content about a specific thing, the dash cam will request a through a get api and the backend services will return the response accordingly.

 
GET -> GET all alarms for dash cam
	 URL : localhost/api//user1/alarms
	RESPONSE: list of alarms
	[
	 { ‘type’: ‘ALARM’, ‘alarm_type’: ‘CRASH’, ‘alarm_time’: ‘2020-08-18 16:45:35’, ‘latitude’: 32.378903, ‘longitude’: -122.457324, ‘file_list’: [‘a.mp4’, ‘b.mp4’] },

	{ ‘type’: ‘ALARM2’, ‘alarm_type’: SHARP_TURN, ‘alarm_time’: ‘2020-08-18 16:41:35’, ‘latitude’: 31.378903, ‘longitude’: -102.457324, ‘file_list’: [‘c.mp4’, ‘d.mp4’] }
	]


GET ->  Query parameters with certain filters such as start_time or end_time, alarm specific type
	URL: localhost/api/user1/alarms/{start_time}
	RESPONSE: return us all the alarms which are starting at or after start_time
		
GET  ->  To get the videos recorded by a dash cam
         Will return the response as list of  the videos for a particular dashcam
    

SEND A COMMAND 

First it will create a  form using POST API asking about which command and then according to the command created it will return the response.

{ ‘type’: ‘COMMAND’, ‘imei’: 12345678, ‘command’: ‘some_command_string’ }


COMMAND RESPONSE: If granted it will succeed or else denied

