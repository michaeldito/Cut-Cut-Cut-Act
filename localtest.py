import sys
import json
from TaxCalculator import *

#try:
argc = len(sys.argv)
income = sys.argv[1]
status = sys.argv[2]
deductions = 0
stateAndLocalTaxDeduction = 0
credits = 0
personalExemptions = 1
if argc > 3:
	deductions = sys.argv[3]
if argc > 4:
	stateAndLocalTaxDeduction = sys.argv[4]
if argc > 5:
	credits = sys.argv[5]
if argc > 6:
	personalExemptions = sys.argv[6]

result = calculateTaxes(income, status, deductions, stateAndLocalTaxDeduction, credits)
print(json.dumps(result))
print()
print('income:     ' + income)
print('status:     ' + status)
print('deductions: ' + str(deductions))
print('credits:    ' + str(credits))
print('savings:    ' + str(result['savingsUnderNewPlan']))
print('old tax:    ' + str(result['Current 2018 System']['taxedAmountAfterCredits']))
print('new tax:    ' + str(result['Tax Cuts And Jobs Act']['taxedAmountAfterCredits']))
print('savings:    ' + str(result['savingsUnderNewPlan']))

#except:
#	print('localtest.py income status deductions credits exemptions')