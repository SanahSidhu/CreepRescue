import os
from flask import *
import requests
from dotenv import load_dotenv

from twilio.twiml.messaging_response import MessagingResponse
from mainapp.models import chk_user_exist, get_email,user
from mainapp.utils import chatbot, fake_call, send_loc, signup, login_user

load_dotenv()
account_sid = os.getenv("twilio_sid")
auth_token = os.getenv("twilio_token")
key_secret = os.getenv("SECRET_KEY")
geoloc_api_key = os.getenv("geoloc_api_key") 


url = f"https://www.googleapis.com/geolocation/v1/geolocate?key={geoloc_api_key}"


# App configuration
app = Flask(__name__)
app.secret_key = key_secret


path = "crdb.db"
user(path)

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
    print("IN LOGIN")

    if request.method == "POST":
        u_name = request.form.get('Name')
        u_email = request.form.get('Email Id')
        u_num = request.form.get('Mobile No')
        u_pwd = request.form.get('Password')

        print(u_name,u_email,u_name,u_pwd)

        if u_name and u_num:
            print("signup")
            if chk_user_exist(path, u_email):
                print("chk user")
                return render_template("login.html", user_exists=True)
            else:
                print("login success")
                user_data = (u_name,u_email,u_num,u_pwd)
                signup(path, user_data)
                session['user_email'] = u_email
                return render_template("home.html")
        
        if u_email and u_pwd and not u_num:
            print("login")
            if l_res := login_user(path, u_email, u_pwd):
                print(l_res)
                if not isinstance(l_res, str):
                    session['user_email'] = u_email
                    return render_template("home.html")
                else:
                    print("wtff")
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
    print("in chatbot")
    bmsg = request.values.get('Body', '').lower()
    print(bmsg)
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
    print(msg.body(rep))

    return str(resp)
    

@app.route("/chatbot", methods = ["POST","GET"])
def chatbotpage():
    if g.user:
        return render_template("sms.html")
    return render_template("/")


@app.route("/call", methods = ["POST", "GET"])
def call():

    if g.user:
        user_email = g.user
        fake_call(path, user_email, account_sid, auth_token)
        return render_template("call.html")
    return render_template("/")



@app.route("/mapurl", methods = ["POST", "GET"])
def loc():

    if g.user:
        url_link = send_loc(url)
        return render_template("mapurl.html", created_url = True, result = url_link)
    return render_template("/")

