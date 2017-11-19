from TaxBracket import *
from TaxBrackets import *
from TaxSystem import *
from DeductionConfiguration import *
import json


def buildTaxCutsAndJobsActSystem():
	brackets = []

	brackets.append(TaxBracket(0,0.0,45000.0,.12))
	brackets.append(TaxBracket(1,45000.0,200000.0,.25))
	brackets.append(TaxBracket(2,200000.0,500000.0,.35))
	brackets.append(TaxBracket(3,500000.0,float("inf"),.396))

	cccSingleBrackets = TaxBrackets(brackets)

	brackets = []

	brackets.append(TaxBracket(0,0.0,90000.0,.12))
	brackets.append(TaxBracket(1,90000.0,260000.0,.25))
	brackets.append(TaxBracket(2,260000.0,1000000.0,.35))
	brackets.append(TaxBracket(3,1000000.0,float("inf"),.396))

	cccMarriedBrackets = TaxBrackets(brackets)

	cccBrackets = {
		'single'  : cccSingleBrackets,
		'married' : cccMarriedBrackets
	}

	deductionConfiugrations = {}

	deductionConfiugrations['standardDeductionSingle']   = DeductionConfiguration('standardDeductionSingle', staticDeductionAmount=12200, deductionAllowed=1, message='You can only take the standard deduction if you do not itemize deductions.')
	deductionConfiugrations['standardDeductionMarried']  = DeductionConfiguration('standardDeductionMarried', staticDeductionAmount=24400, deductionAllowed=1, message='You can only take the standard deduction if you do not itemize deductions.')
	deductionConfiugrations['personalExemption']         = DeductionConfiguration('personalExemption', deductionAllowed=0, staticDeductionAmount=0, message='There are no personal exemptions under this plan.')
	deductionConfiugrations['stateAndLocalTaxDeduction'] = DeductionConfiguration('stateAndLocalTaxDeduction', deductionAllowed=0, message='You are not allowed to deduct state and local taxes in this plan.')
	deductionConfiugrations['itemizedDeductions']        = DeductionConfiguration('itemizedDeductions', message='If you itemize your deductions, you cannot take the standard deduction')
	deductionConfiugrations['propertyTaxDeduction']      = DeductionConfiguration('propertyTaxDeduction', maxDeduction=10000, message='There is a $10,000 limit on property tax deductions under this plan')
	deductionConfiugrations['tuitionWaverDeduction']     = DeductionConfiguration('tuitionWaverDeduction', deductionAllowed=0, message='In this tax plan, any waved tuition is considered income.')

	messages = []

	messages.append('There are no personal exemptions under the house bill')

	cccTaxSystem = TaxSystem('TaxCutsAndJobsActHouse', cccBrackets, deductionConfiugrations, messages)

	return cccTaxSystem

def buildCurrent2018System():
	brackets = []

	brackets.append(TaxBracket(0,0,9526.0,.10))
	brackets.append(TaxBracket(1,9526.0,38700.0,.15))
	brackets.append(TaxBracket(2,38700.0,93700.0,.25))
	brackets.append(TaxBracket(3,93700.0,195450.0,.28))
	brackets.append(TaxBracket(4,195450.0,424950.0,.33))
	brackets.append(TaxBracket(5,424950.0,426700.0,.35))
	brackets.append(TaxBracket(6,426700.0,float("inf"),.396))

	singleBrackets = TaxBrackets(brackets)

	brackets = []

	brackets.append(TaxBracket(0,0,19050.0,.10))
	brackets.append(TaxBracket(1,19050.0,77400.0,.15))
	brackets.append(TaxBracket(2,77400.0,156150.0,.25))
	brackets.append(TaxBracket(3,156150.0,237950.0,.28))
	brackets.append(TaxBracket(4,237950.0,424950.0,.33))
	brackets.append(TaxBracket(5,424950.0,480050.0,.35))
	brackets.append(TaxBracket(6,480050.0,float("inf"),.396))

	marriedBrackets = TaxBrackets(brackets)

	bracketsArray = {
		'single'  : singleBrackets,
		'married' : marriedBrackets
	}

	deductionConfiugrations = {}

	deductionConfiugrations['standardDeductionSingle']   = DeductionConfiguration('standardDeductionSingle', staticDeductionAmount = 6500)
	deductionConfiugrations['standardDeductionMarried']  = DeductionConfiguration('standardDeductionMarried', staticDeductionAmount = 13000)
	deductionConfiugrations['personalExemption']         = DeductionConfiguration('personalExemption', staticDeductionAmount=4150)
	deductionConfiugrations['stateAndLocalTaxDeduction'] = DeductionConfiguration('stateAndLocalTaxDeduction', deductionAllowed=1)
	deductionConfiugrations['itemizedDeductions']        = DeductionConfiguration('itemizedDeductions', message='If you itemize your deductions, you cannot take the standard deduction')
	deductionConfiugrations['propertyTaxDeduction']      = DeductionConfiguration('propertyTaxDeduction')
	deductionConfiugrations['tuitionWaverDeduction']     = DeductionConfiguration('tuitionWaverDeduction', message='In this tax plan, any waved tuition is not considered incom')

	messages = []

	messages.append('The tax brackets used are based on the 2018 tax brackets.')

	currentTaxSystem = TaxSystem('Current2018System', bracketsArray, deductionConfiugrations, messages)

	return currentTaxSystem
