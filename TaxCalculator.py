import json;
from TaxBracketFactory import *
from TaxSystem import *
def calculateTaxes(income, status, deductions=0, credits=0, personalExemptions=1):
	taxCutsAndJobsActTaxSystem = buildTaxCutsAndJobsActSystem()
	currentTaxSystem = buildCurrent2018System()

	taxCutsAndJobsActResults = taxCutsAndJobsActTaxSystem.calcTaxedAmount(income, status, deductions, credits, personalExemptions)
	currentSystemResults = currentTaxSystem.calcTaxedAmount(income, status, deductions, credits, personalExemptions)

	results = {}

	results['savingsUnderNewPlan'] = currentSystemResults['taxedAmountAfterCredits'] - taxCutsAndJobsActResults['taxedAmountAfterCredits']
	results['Tax Cuts And Jobs Act'] = taxCutsAndJobsActResults
	results['Current 2018 System'] = currentSystemResults

	return results

	jsonData = json.dumps(results)
	return jsonData
