from flask import Flask, jsonify
import datetime
import geocoder
#import requests
freegeoip = "http://freegeoip.net/json"
import re
import json
from urllib.request import urlopen

url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

l1, l2 = data['loc'].split(",")

x = datetime.datetime.now()

app = Flask(__name__)



Alarm_types = {1: "VIBRATION", 2: "OVERSPEED", 3: "CRASH", 4: "HARD_ACCELERATION", 5: "HARD_BRAKE", 6: "SHARP_TURN"}

@app.route('/Alarm_types_key/<int:n>')
def fun(n):
    if(n%2):
        print(f"{n} is an odd number")
        result = {
            "type": "ALARM",
            "alarm_type": Alarm_types[n],
            "alarm_time": x,
            "latitude": l1,
            "longitude": l2,
            "file_list": ["a.mp4", "b.mp4"]
        }
    else:
        print(f"{n} is an even number")
        result = {
            "type": "ALARM",
            "alarm_type": Alarm_types[n],
            "alarm_time": x,
            "latitude": l1,
            "longitude": l2,
            "file_list": ["a.mp4", "b.mp4"]
        }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)