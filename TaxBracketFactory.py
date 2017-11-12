from TaxBracket import *
from TaxBrackets import *
from TaxSystem import *

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

	standardDeductions = {}
	standardDeductions['single'] = 0
	standardDeductions['married'] = 0


	cccTaxSystem = TaxSystem('TaxCutsAndJobsActHouse', cccBrackets, standardDeductions, 4150, 0, 0)

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

	standardDeductions = {}
	standardDeductions['single'] = 6500
	standardDeductions['married'] = 13000

	currentTaxSystem = TaxSystem('Current2018System', bracketsArray, standardDeductions, 4150)

	return currentTaxSystem
