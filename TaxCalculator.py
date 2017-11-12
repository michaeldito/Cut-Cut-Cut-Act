import json;
from TaxBracketFactory import *
from TaxSystem import *
def calculateTaxes(income, status, deductions=0, stateAndLocalTaxDeduction=0, credits=0, personalExemptions=1):
	taxCutsAndJobsActTaxSystem = buildTaxCutsAndJobsActSystem()
	currentTaxSystem = buildCurrent2018System()

	taxCutsAndJobsActResults = taxCutsAndJobsActTaxSystem.calcTaxedAmount(income, status, deductions, stateAndLocalTaxDeduction, credits, personalExemptions)
	currentSystemResults = currentTaxSystem.calcTaxedAmount(income, status, deductions, stateAndLocalTaxDeduction, credits, personalExemptions)

	results = {}

	results['savingsUnderNewPlan'] = currentSystemResults['taxedAmountAfterCredits'] - taxCutsAndJobsActResults['taxedAmountAfterCredits']
	results['TaxCutsAndJobsActHouse'] = taxCutsAndJobsActResults
	results['Current2018System'] = currentSystemResults

	jsonData = json.dumps(results)
	return jsonData
