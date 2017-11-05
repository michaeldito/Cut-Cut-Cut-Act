from TaxBracket import *;
from TaxBrackets import *;
import sys;

def doTaxes(income, status):
	brackets = [];

	brackets.append(TaxBracket(0,12000.0,0))
	brackets.append(TaxBracket(12000.0,45000.0,.12))
	brackets.append(TaxBracket(45000.0,200000.0,.25))
	brackets.append(TaxBracket(200000.0,500000.0,.35))
	brackets.append(TaxBracket(500000.0,float("inf"),.396))

	cccSingleBrackets = TaxBrackets(brackets);

	brackets = [];

	brackets.append(TaxBracket(0,24000.0,0))
	brackets.append(TaxBracket(24000.0,90000.0,.12))
	brackets.append(TaxBracket(90000.0,260000.0,.25))
	brackets.append(TaxBracket(260000.0,1000000.0,.35))
	brackets.append(TaxBracket(1000000.0,float("inf"),.396))

	cccMarriedBrackets = TaxBrackets(brackets);

	if status == 'single':
		return "For a single person $" + str(income) + ", tax will be $" + str(cccSingleBrackets.calcTaxedAmount(income)) + '\n';
	if status == 'married':
		return "For a #married couple $" + str(income) + ", tax will be $" + str(cccMarriedBrackets.calcTaxedAmount(income)) + '\n';



