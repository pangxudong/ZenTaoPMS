import requests
from flask import Flask

app = Flask(__name__)

@app.route("/lanhu")
def lanhu():
        form = {'email':'xudongpang@hotmail.com','password':'xxxx'}
        res = requests.post('https://lanhuapp.com/api/account/login', data=form)
        return res.json()
