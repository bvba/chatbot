
from flask import Flask, jsonify, request
from extern import *

app = Flask(__name__)

@app.route('/')
def temp() :
    return ''

@app.route('/keyboard')
def keyboard() :
    return jsonify(mealTime)

@app.route('/message', methods = ['POST'])
def message() :
    data = request.get_json()
    print(data)
    content = data['content']

    res = dict()
    if content == '아침' or content == '점심' or content == '저녁':
        res['message'] = {'text' : content + 'is selected\nplease choose menu'}
        res['keyboard'] = menu.getKeyboard()
    elif content in koToEng :
        res['message'] = {'text' : content + 'is selected'}
        res['keyboard'] = mealTime
    return jsonify(res)

if __name__ == '__main__' :
    app.debug = True
    app.run(host = '0.0.0.0', port = 1526)
