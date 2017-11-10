from TaxBrackets import *;

class TaxSystem:
	
	def __init__(self, name, brackets, standardDeductions, personalExemptionAmount, personalExemptionAllowed=1):
		self.name = name
		self.brackets = brackets
		self.standardDeductions = standardDeductions
		self.personalExemptionAmount = personalExemptionAmount
		self.personalExemptionAllowed = personalExemptionAllowed

	def calcTaxedAmount(self, income, status, deductions=0, credits=0, personalExemptions=0):
		print('standardDeductions: ' + str(self.standardDeductions))
		print('personalExemptions: ' + str(personalExemptions))
		if self.personalExemptionAllowed == 0:
			if personalExemptions > 0:
				personalExemptions -= 1

		taxableIncome = float(income) - float(deductions) - float(self.standardDeductions[status]) - (float(personalExemptions) * float(self.personalExemptionAmount))
		bracketResults = self.brackets[status].calcTaxedAmountForBrackets(taxableIncome)
		taxedAmountFromBrackets = bracketResults['taxedAmountFromBrackets']
		taxedAmountAfterCredits = taxedAmountFromBrackets - float(credits)
		results = {}
		results['taxSystem'] = self.name
		results['income'] = income
		results['status'] = status
		results['deductions'] = deductions
		results['credits'] = credits
		results['personalExemptions'] = personalExemptions
		results['taxableIncome'] = taxableIncome
		results['taxedAmountFromBrackets'] = taxedAmountFromBrackets
		results['taxedAmountAfterCredits'] = taxedAmountAfterCredits
		results['bracketResults'] = bracketResults

		return results
