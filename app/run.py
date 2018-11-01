
#-*-coding: euc-kr -*-

from flask import Flask, request
from Manager import manager

app = Flask(__name__)

@app.route('/')
def index() :
    return '', 200

# get keyboard
@app.route('/keyboard')
def keyboard() :
    return manager.process('keyboard')

# button selected
@app.route('/message', methods = ['POST'])
def message() :
    # data == user_key, type, content
    req = request.get_json()
    return manager.process('message', req)

if __name__ == '__main__' :
    app.debug = True
    app.run(host = '0.0.0.0', port = 1526)
