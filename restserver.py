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
	incoming = request.get_json(force=True)
	print(incoming)
	try:
		income = float(incoming['income'])
		status = incoming['status']
		deductions = float(incoming['deductions'])
		stateAndLocalTaxDeduction = float(incoming['stateAndLocalTaxDeduction'])
		credits = float(incoming['credits'])
		personalExemptions = float(incoming['personalExemptions'])

		result = calculateTaxes(income, status, deductions, stateAndLocalTaxDeduction, credits, personalExemptions)
		print result
		return Response(response="No luck",status=200, mimetype="application/text")
		return Response(response=result, status=200, mimetype="application/json")
	except:
		print('Bad json data')
		return Response(response="No luck",status=200, mimetype="application/text")
