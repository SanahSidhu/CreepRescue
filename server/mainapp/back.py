import json
import os
from flask import *
import requests
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from server.mainapp.models import chk_user_exist, get_email, get_mob_no
from server.mainapp.utils import chatbot, fake_call, send_loc, signup

load_dotenv()
account_sid = os.getenv("twilio_sid")
auth_token = os.getenv("twilio_token")
key_secret = os.getenv("SECRET_KEY")
geoloc_api_key = os.getenv("geoloc_api_key") 


url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={geoloc_api_key}"


# App configuration
app = Flask(__name__)
app.secret_key = key_secret


path = ""


@app.before_request
def security():
    g.user = None
    if 'user_email' in session:
        emails = get_email(path)
        try:
            useremail = [
                email for email in emails if email[0] == session["user_email"]
            ][0]
            g.user = useremail
        except Exception as e:
            print(e)


@app.route("/", methods = ["GET","POST"])
def login():
    """
    Login Page
    """
    session.pop("user_email", None)

    if request.method == "POST":
        u_name = request.form.get('name')
        u_email = request.form.get('email')
        u_num = request.form.get('mob_no')
        u_pwd = request.form.get('password')


        if u_name and u_num:
            if chk_user_exist(path, u_email):
                return render_template("login.html", user_exists=True)
            else:
                data = (u_name,u_email,u_num,u_pwd)
                signup(path,data)
                return render_template("login.html",success=True)
        
        if u_email and u_pwd and not u_num:
            if l_res := login(path, u_email, u_pwd):
                if not isinstance(l_res, str):
                    return render_template("home.html")
                else:
                    return render_template("login.html", error = l_res)
    else:
        return render_template("login.html")


@app.route("/home", methods=["GET", "POST"])
def index():
    """
    Home Page
    """
    if g.user:
        return render_template("home.html")
    return redirect("/")


@app.route("/sms", methods = ["POST", "GET"])
def chat_bot():
    chatbot()
    render_template("cbot.html")

@app.route("/call", methods = ["POST", "GET"])
def call():
     if g.user:
        user_email = g.user

        fake_call(path, user_email, account_sid, auth_token)
        render_template("call.html")

@app.route("/mapurl", methods = ["POST", "GET"])
def loc():
    url_link = send_loc(url)
    return render_template("mapurl.html", result = url_link)

