
#-*-coding: euc-kr -*-

from flask import Flask, jsonify, request
from res import *
from Menu import menu

app = Flask(__name__)

@app.route('/')
def temp() :
	return 'god yungoon 차냥해'

@app.route('/keyboard')
def keyboard() :
	return jsonify(mealTimeKeyB)

@app.route('/message', methods = ['POST'])
def message() :
	data = request.get_json()
	content = data['content']

	resp = dict()
	if content in mealTime:
		resp['message'] = {'text' : menu.getMeal(content)}
		resp['keyboard'] = mealTimeKeyB
	return jsonify(resp)

if __name__ == '__main__' :
	app.debug = True
	app.run(host = '0.0.0.0', port = 1526)
