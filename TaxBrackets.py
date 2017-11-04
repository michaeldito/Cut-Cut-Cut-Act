from TaxBracket import *;

class TaxBrackets:
	
	def __init__(self, brackets):
		self.brackets = brackets;
		
	def calcTaxedAmount(self, income):
		taxedAmountSum = 0;
		for bracket in self.brackets:
			taxedAmount = bracket.calcTaxedAmount(income);
			taxedAmountSum += taxedAmount;
			print taxedAmount;
		
		return taxedAmountSum;
		
