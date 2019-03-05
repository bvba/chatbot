
# -*-coding: euc-kr -*-

from flask import Flask, request
from Manager import manager

app = Flask(__name__)


@app.route('/')
def index() :
    return 'hello', 200

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

@app.route('/friend', methods = ['POST'])
def addFriend() :
    req = request.get_json()
    return manager.process('addFriend', req)

@app.route('/friend/<user_key>', methods = ['DELETE'])
def removeFriend(user_key) :
    return manager.process('removeFriend', user_key)

@app.route('/chat_room/<user_key>', methods = ['DELETE'])
def exitChatRoom(user_key) :
    return manager.process('exitChatRoom', user_key)

if __name__ == '__main__' :
    app.debug = False
    app.run(host = '0.0.0.0', port = 1526)
