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

app = Flask(__name__)


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
    call = client.calls.create(to = os.getenv("my_phone_no"), from_ = "+16205829065", url = "http://demo.twilio.com/docs/voice.xml")             ##        get user mob no from session    !!!!
    print(call.sid)

