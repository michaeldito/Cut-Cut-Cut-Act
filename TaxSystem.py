from TaxBrackets import *;

class TaxSystem:
	
	def __init__(self, name, brackets, standardDeduction, personalExemptionAmount, personalExemptionAllowed=1, stateAndLocalTaxDeductionAllowed=1):
		self.name = name
		self.brackets = brackets
		self.standardDeduction = standardDeduction
		self.personalExemptionAmount = personalExemptionAmount
		self.personalExemptionAllowed = personalExemptionAllowed
		self.stateAndLocalTaxDeductionAllowed = stateAndLocalTaxDeductionAllowed

	def calcTaxedAmount(self, income, status, deductions=0, stateAndLocalTaxDeduction=0, credits=0, personalExemptions=0):
		if self.personalExemptionAllowed == 0:
			if personalExemptions > 0:
				personalExemptions -= 1

		if self.stateAndLocalTaxDeductionAllowed == 0:
			stateAndLocalTaxDeduction = 0

		deductionsFromPersonalExemptions = (float(personalExemptions) * float(self.personalExemptionAmount))

		standardDeduction = float(self.standardDeduction[status])

		taxableIncome = float(income)
		taxableIncome -= float(deductions)
		taxableIncome -= standardDeduction
		taxableIncome -= deductionsFromPersonalExemptions
		taxableIncome -= float(stateAndLocalTaxDeduction)

		bracketResults = self.brackets[status].calcTaxedAmountForBrackets(taxableIncome)
		taxedAmountFromBrackets = bracketResults['taxedAmountFromBrackets']
		taxedAmountAfterCredits = taxedAmountFromBrackets - float(credits)
		results = {}
		results['taxSystem'] = self.name
		results['income'] = income
		results['status'] = status
		results['deductions'] = deductions
		results['stateAndLocalTaxDeduction'] = stateAndLocalTaxDeduction
		results['standardDeduction'] = standardDeduction
		results['credits'] = credits
		results['personalExemptions'] = personalExemptions
		results['deductionsFromPersonalExemptions'] = deductionsFromPersonalExemptions
		results['taxableIncome'] = taxableIncome
		results['taxedAmountFromBrackets'] = taxedAmountFromBrackets
		results['taxedAmountAfterCredits'] = taxedAmountAfterCredits
		results['bracketResults'] = bracketResults

		return results
