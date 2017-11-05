'''
	REST API to calculate your taxes, using the cutcutcutact algorithm
'''

import json
from flask import Flask, Response, request
from cutcutcut import doTaxes

app = Flask(__name__)

@app.route("/cutcutcut", methods=['POST', 'GET'])
def cutcutcut():
	income = float(request.get_json()['income'])
	status = request.get_json()['status']
	response_content = doTaxes(income, status)
	return Response(response=response_content, status=200, mimetype="application/text")
