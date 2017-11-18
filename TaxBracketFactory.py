from TaxBracket import *
from TaxBrackets import *
from TaxSystem import *
from DeductionConfiguration import *
import json


def buildTaxCutsAndJobsActSystem():
	brackets = []

	brackets.append(TaxBracket(0,0,12000.0,0))
	brackets.append(TaxBracket(1,12000.0,45000.0,.12))
	brackets.append(TaxBracket(2,45000.0,200000.0,.25))
	brackets.append(TaxBracket(3,200000.0,500000.0,.35))
	brackets.append(TaxBracket(4,500000.0,float("inf"),.396))

	cccSingleBrackets = TaxBrackets(brackets)

	brackets = []

	brackets.append(TaxBracket(0,0,24000.0,0))
	brackets.append(TaxBracket(1,24000.0,90000.0,.12))
	brackets.append(TaxBracket(2,90000.0,260000.0,.25))
	brackets.append(TaxBracket(3,260000.0,1000000.0,.35))
	brackets.append(TaxBracket(4,1000000.0,float("inf"),.396))

	cccMarriedBrackets = TaxBrackets(brackets)

	cccBrackets = {
		'single'  : cccSingleBrackets,
		'married' : cccMarriedBrackets
	}

	deductionConfiugrations = {}

	deductionConfiugrations['standardDeductionSingle']   = DeductionConfiguration('standardDeductionSingle', deductionAllowed=0, message='The standard deduction is per-se not allowed in this tax plan, however there is a new 0\% bracket that is similar to a standard deduction.')
	deductionConfiugrations['standardDeductionMarried']  = DeductionConfiguration('standardDeductionMarried', deductionAllowed=0, message='The standard deduction is per-se not allowed in this tax plan, however there is a new 0\% bracket that is similar to a standard deduction.')
	deductionConfiugrations['personalExemption']         = DeductionConfiguration('personalExemption', staticDeductionAmount=4150, staticDeductionDelta=-1, message='You are not allowed to take a personal exemption in this tax plan, however you can take exemptions for your dependents.')
	deductionConfiugrations['stateAndLocalTaxDeduction'] = DeductionConfiguration('stateAndLocalTaxDeduction', deductionAllowed=0, message='You are not allowed to deduct state and local taxes in this plan.')
	deductionConfiugrations['itemizedDeductions']        = DeductionConfiguration('itemizedDeductions', message='If you itemize your deductions, you cannot take the standard deduction')

	messages = []

	messages.append('The House plan does not allow you to take a personal exemption for yourself, but you can still take them for your dependents. We have reduced the number of personal exemptions you requested by 1')

	#cccTaxSystem = TaxSystem('TaxCutsAndJobsActHouse', cccBrackets, standardDeductions, 4150, 0, 0)
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

	messages = []

	messages.append('The tax brackets used are based on the 2018 tax brackets.')

	currentTaxSystem = TaxSystem('Current2018System', bracketsArray, deductionConfiugrations, messages)

	return currentTaxSystem
