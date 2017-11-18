from TaxBrackets import *;

class TaxSystem:
	
	#def __init__(self, name, brackets, standardDeduction, personalExemptionAmount, personalExemptionAllowed=1, stateAndLocalTaxDeductionAllowed=1):
	def __init__(self, name, brackets, deductionConfigurations, messages=[]):
		self.name = name
		self.brackets = brackets
		self.deductionConfigurations = deductionConfigurations
		self.messages = messages
		#self.standardDeduction = standardDeduction
		# self.personalExemptionAmount = personalExemptionAmount
		# self.personalExemptionAllowed = personalExemptionAllowed
		# self.stateAndLocalTaxDeductionAllowed = stateAndLocalTaxDeductionAllowed

	def calcTaxedAmount(self, income, status, itemizedDeductionsRequested=0, stateAndLocalTaxDeductionRequested=0, credits=0, personalExemptionsRequested=0):

		# if self.stateAndLocalTaxDeductionAllowed == 0:
		# 	stateAndLocalTaxDeduction = 0


		deductions = {}

		deductions['stateAndLocalTaxDeduction'] = self.deductionConfigurations['stateAndLocalTaxDeduction'].calcDeduction(float(stateAndLocalTaxDeductionRequested))
		deductions['personalExemption'] = self.deductionConfigurations['personalExemption'].calcDeduction(numberRequested=personalExemptionsRequested)

		if (itemizedDeductionsRequested == 0):
			if status == 'single':
				deductions['standardDeduction'] = self.deductionConfigurations['standardDeductionSingle'].calcDeduction()
			elif status == 'married':
				deductions['standardDeduction'] = self.deductionConfigurations['standardDeductionMarried'].calcDeduction()
		else:
			deductions['itemizedDeduction'] = self.deductionConfigurations['itemizedDeductions'].calcDeduction(float(itemizedDeductionsRequested))


		taxableIncome = float(income)

		# print('From TaxSystem/calcTaxedAmount:')
		# print('   Deductions:')
		# print('      type: ' + str(type(deductions)))
		# print()

		for name, deduction in deductions.items():
			taxableIncome -= deduction['amountDeducted']


# 		deductionsFromPersonalExemptions = (float(personalExemptions) * float(self.personalExemptionAmount))

# #		standardDeduction = float(self.standardDeduction[status])
# 		if status == 'single':
# 			standardDeductionConfiguration = self.deductionConfigurations['standardDeductionSingle']
# 		else if status == 'married':
# 			standardDeductionConfiguration = self.deductionConfigurations['standardDeductionMarried']

# 		taxableIncome = float(income)
# 		taxableIncome -= self.deductionConfigurations['itemizedDeductions'].calcDeduction(float(itemizedDeductionsRequested))
# 		taxableIncome -= standardDeductionConfiguration.calcDeduction()
# 		taxableIncome -= deductionsFromPersonalExemptions
# 		taxableIncome -= float(stateAndLocalTaxDeduction)

		bracketResults = self.brackets[status].calcTaxedAmountForBrackets(taxableIncome)
		taxedAmountFromBrackets = bracketResults['taxedAmountFromBrackets']
		taxedAmountAfterCredits = taxedAmountFromBrackets - float(credits)



		results = {}
		results['taxSystem'] = self.name
		results['deductions'] = deductions
		results['income'] = income
		results['status'] = status
		# results['itemizedDeductionsRequested'] = itemizedDeductionsRequested
		# results['stateAndLocalTaxDeduction'] = stateAndLocalTaxDeduction
		# results['standardDeduction'] = standardDeduction
		results['credits'] = credits
		# results['personalExemptions'] = personalExemptions
		# results['deductionsFromPersonalExemptions'] = deductionsFromPersonalExemptions
		results['taxableIncome'] = taxableIncome
		results['taxedAmountFromBrackets'] = taxedAmountFromBrackets
		results['taxedAmountAfterCredits'] = taxedAmountAfterCredits
		results['bracketResults'] = bracketResults
		results['messages'] = self.messages

		return results
