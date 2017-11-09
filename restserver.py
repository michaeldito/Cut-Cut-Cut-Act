'''
	REST API to calculate your taxes, using the cutcutcutact algorithm
'''

import json
from flask import Flask, Response, request
from flask_cors import CORS
from cutcutcut import doTaxes

app = Flask(__name__)
CORS(app)

@app.route("/cutcutcut", methods=['POST', 'GET'])
def cutcutcut():
	print('json:')
	print(request.get_json(force=True))
	print('data:')
	print(request.get_data())
	try:
		income = float(request.get_json()['income'])
		status = request.get_json()['status']
		response_content = doTaxes(income, status)
		return Response(response=response_content, status=200, mimetype="application/text")
	except:
		print('Bad json data')
		return Response(response="No luck",status=200, mimetype="application/text")
