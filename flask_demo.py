import json
import requests
from flask import Flask, request
from flask import make_response

app = Flask(__name__)

@app.route("/lanhu")
def lanhu():
        username = request.args.get('username')
        msg = "no such user " + username
        with open('lanhu_conf.json') as json_file:
            data = json.load(json_file)
            if username in data:
                form = data[username]
                res = requests.post('https://lanhuapp.com/api/account/login', data=form)
                rst = make_response(res.json())
                rst.headers['Access-Control-Allow-Origin'] = '*'
                return rst, 201
            else:
                return msg, 201

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
