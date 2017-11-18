import sys
import json
from TaxCalculator import *
from DeductionConfiguration import *

def testForCommandLineArguments():
	try:
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

	except:
		print('localtest.py income status deductions stateAndLocalTaxDeduction credits exemptions')

def deductionConfigurationTest():
	allowedDynamicNoLimit = DeductionConfiguration('allowedDynamicNoLimit')
	allowedStaticNoLimit = DeductionConfiguration('allowedStaticNoLimit', staticDeductionAmount=1000, )
	allowedDynamicLimit = DeductionConfiguration('allowedDynamicLimit', maxDeduction=500)
	notAllowedNoLimitStatic = DeductionConfiguration('notAllowedNoLimitStatic', deductionAllowed=0, staticDeductionAmount=1000)
	notAllowedNoLimitDynamic = DeductionConfiguration('notAllowedNoLimitDynamic', deductionAllowed=0)

	print(allowedDynamicNoLimit.calcDeduction(2000))
	print(allowedStaticNoLimit.calcDeduction())
	print(allowedDynamicLimit.calcDeduction(2000))
	print(notAllowedNoLimitStatic.calcDeduction(2000))
	print(notAllowedNoLimitDynamic.calcDeduction(2000))

def taxBracketTest():
	return calculateTaxes(100000, 'single', itemizedDeductions=1000, stateAndLocalTaxDeduction=6000, credits=1000, personalExemptions=1)

print(taxBracketTest())
