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
		itemizedDeductions = float(incoming['itemizedDeductions'])
		stateAndLocalTaxDeduction = float(incoming['stateAndLocalTaxDeduction'])
		propertyTaxDeduction = float(incoming['propertyTaxDeduction'])
		medicalExpensesDeduction = float(incoming['medicalExpensesDeduction'])
		tuitionWaved = float(incoming['tuitionWaved'])
		childDependents = float(incoming['childDependents'])
		nonChildDependents = float(incoming['nonChildDependents'])

		result = calculateTaxes(income, status, itemizedDeductions, stateAndLocalTaxDeduction, propertyTaxDeduction, medicalExpensesDeduction, tuitionWaved, childDependents, nonChildDependents)
		print result
		return Response(response=result, status=200, mimetype="application/json")
	except:
		print('Bad json data')
		return Response(response="No luck",status=200, mimetype="application/text")
