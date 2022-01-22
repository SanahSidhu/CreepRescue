import json
from flask import *
import requests
from twilio.twiml.messaging_response import MessagingResponse

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