'''
	REST API to calculate your taxes, using the cutcutcutact algorithm
'''

import json
from flask import Flask, Response, request
from flask_cors import CORS
from TaxCalculator import calculateTaxes

app = Flask(__name__)
CORS(app)

@app.route("/cutcutcut", methods=['POST', 'GET'])
def doTaxes():
	print('json:')
	print(request.get_json(force=True))
	print('data:')
	print(request.get_data())
	try:
		income = float(request.get_json()['income'])
		status = request.get_json()['status']
		deductions = float(request.get_json()['deductions'])
		stateAndLocalTaxDeduction = float(request.get_json()['stateAndLocalTaxDeduction'])
		credits = float(request.get_json()['credits'])
		personalExemptions = float(request.get_json()['personalExemptions'])


		response_content = calculateTaxes(income, status, deductions, stateAndLocalTaxDeduction, credits, personalExemptions)
		return Response(response=response_content, status=200, mimetype="application/text")
	except:
		print('Bad json data')
		return Response(response="No luck",status=200, mimetype="application/text")
