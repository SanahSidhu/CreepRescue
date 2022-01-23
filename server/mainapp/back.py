import json
import os
from flask import *
import requests
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

load_dotenv()
account_sid = os.getenv("twilio_sid")
auth_token = os.getenv("twilio_token")
key_secret = os.getenv("SECRET_KEY")
geoloc_api_key = os.getenv("geoloc_api_key") 


url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={geoloc_api_key}"


# App configuration
app = Flask(__name__)
app.secret_key = key_secret


@app.route("/sms", methods = ["POST", "GET"])
def chatbot():
    bmsg = request.values.get('Body', '').lower()
    bmsg_words = bmsg.split()
    rep_json = open("C:\\Users\\SANAH\\Desktop\\creepjson.json")
    response = json.load(rep_json)

    #Twilio Syntax

    rep = ""

    for word in bmsg_words:
        if word in response:
            rep = response[word]
        else:
            rep = response["default"]

    resp = MessagingResponse()
    msg = resp.message()

    rep = "\n" + rep
    msg.body(rep)

    return str(resp)


def fake_call():
    client = Client(account_sid,auth_token)
    call = client.calls.create(to = os.getenv("my_phone_no"), from_ = "+16205829065", url = "http://demo.twilio.com/docs/voice.xml")        ##  get user mob no from session    !!!!
    print(call.sid)


def send_loc():
    pool_request = requests.Session()

    response = pool_request.post(url)
    data = response.json()

    lat = data['location']['lat']
    lng = data['location']['lng']

    map_url = f"https://www.google.com/maps/search/?api=1&query={lat}%2C{lng}"
