import json
from TaxBracketFactory import *
from TaxSystem import *
def calculateTaxes(income, status, itemizedDeductions=0, stateAndLocalTaxDeduction=0, propertyTaxDeduction=0, medicalExpensesDeduction=0, tuitionWaved=0, childDependents=0, nonChildDependents=0):
	taxCutsAndJobsActTaxSystem = buildTaxCutsAndJobsActSystem()
	currentTaxSystem = buildCurrent2018System()

	taxCutsAndJobsActResults = taxCutsAndJobsActTaxSystem.calcTaxedAmount(income, status, itemizedDeductions, stateAndLocalTaxDeduction, propertyTaxDeduction, tuitionWaved, medicalExpensesDeduction, childDependents, nonChildDependents)
	currentSystemResults = currentTaxSystem.calcTaxedAmount(income, status, itemizedDeductions, stateAndLocalTaxDeduction, propertyTaxDeduction, tuitionWaved, medicalExpensesDeduction, childDependents, nonChildDependents)

	results = {}

	results['savingsUnderNewPlan'] = currentSystemResults['taxedAmountAfterCredits'] - taxCutsAndJobsActResults['taxedAmountAfterCredits']
	results['TaxCutsAndJobsActHouse'] = taxCutsAndJobsActResults
	results['Current2018System'] = currentSystemResults

	jsonData = json.dumps(results)
	return jsonData
