
import requests
from flask import *
from twilio.rest import Client
from mainapp.models import add_user, chk_user_exist, chk_user_pwd, get_mob_no

def signup(path: str, data: tuple):
    add_user(path, data)

def login_user(path: str, user_email: str, passw: str):
    
    if chk_user_exist(path, user_email):
        if chk_user_pwd(path,user_email,passw):
            return True
        else:
            return "Incorrect Email or Password. Please try again."
    else:
        return "This user does not exist. Please sign up."


def fake_call(path: str, user_email: str, account_sid:str, auth_token: str):
    client = Client(account_sid,auth_token)
    user_mob = get_mob_no(path, user_email)
    call = client.calls.create(to = user_mob, from_ = "+16205829065", url = "http://demo.twilio.com/docs/voice.xml")


def send_loc(url: str):
    pool_request = requests.Session()

    response = pool_request.post(url)
    data = response.json()

    lat = data['location']['lat']
    lng = data['location']['lng']

    map_url = f"https://www.google.com/maps/search/?api=1&query={lat}%2C{lng}"

    return map_url
