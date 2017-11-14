from TaxBracket import *;

class TaxBrackets:
	
	def __init__(self, brackets):
		self.brackets = brackets
		
	def calcTaxedAmountForBrackets(self, income):
		taxedAmountSum = 0
		results = []
		for bracket in self.brackets:
			bracketResults = bracket.calcTaxedAmount(income)
			taxedAmountSum += bracketResults['taxedAmount']
			results.append(bracketResults)
		
		return {
			'taxedAmountFromBrackets' : taxedAmountSum,
			'resultsFromBrackets'   : results
		}
		
