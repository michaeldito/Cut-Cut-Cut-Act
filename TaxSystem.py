from TaxBrackets import *;

class TaxSystem:
	
	def __init__(self, name, brackets, deductionConfigurations, messages=[]):
		self.name = name
		self.brackets = brackets
		self.deductionConfigurations = deductionConfigurations
		self.messages = messages

	def calcTaxedAmount(self, income, status, itemizedDeductionsRequested=0, stateAndLocalTaxDeductionRequested=0, propertyTaxDeductionRequested=0, tuitionWaved=0, personalExemptionsRequested=0, credits=0):

		deductions = {}

		income = float(income) + float(tuitionWaved);

		deductions['personalExemption'] = self.deductionConfigurations['personalExemption'].calcDeduction(numberRequested=personalExemptionsRequested)

		print('bool a: ' + str(itemizedDeductionsRequested != 0))
		print('bool b: ' + str(self.deductionConfigurations['itemizedDeductions'].deductionAllowed == 1))
		print('bool c: ' + str(stateAndLocalTaxDeductionRequested != 0))
		print('bool d: ' + str(self.deductionConfigurations['stateAndLocalTaxDeduction'].deductionAllowed == 1))
		print('bool e: ' + str(propertyTaxDeductionRequested != 0))
		print('bool f: ' + str(self.deductionConfigurations['propertyTaxDeduction'].deductionAllowed == 1))

		itemizingDeductions = (itemizedDeductionsRequested != 0 and self.deductionConfigurations['itemizedDeductions'].deductionAllowed == 1) or (stateAndLocalTaxDeductionRequested != 0 and self.deductionConfigurations['stateAndLocalTaxDeduction'].deductionAllowed == 1) or (propertyTaxDeductionRequested != 0 and self.deductionConfigurations['propertyTaxDeduction'].deductionAllowed == 1)

		itemizedDeduction = self.deductionConfigurations['itemizedDeductions'].calcDeduction(float(itemizedDeductionsRequested));
		stateAndLocalTaxDeduction = self.deductionConfigurations['stateAndLocalTaxDeduction'].calcDeduction(float(stateAndLocalTaxDeductionRequested))
		propertyTaxDeduction = self.deductionConfigurations['propertyTaxDeduction'].calcDeduction(float(propertyTaxDeductionRequested))
		
		if status == 'single':
			standardDeduction = self.deductionConfigurations['standardDeductionSingle'].calcDeduction()
		elif status == 'married':
			standardDeduction = self.deductionConfigurations['standardDeductionMarried'].calcDeduction()

		totalItemizedDeductions = itemizedDeduction['amountDeducted'] + stateAndLocalTaxDeduction['amountDeducted'] + propertyTaxDeduction['amountDeducted']

		print('itemized deduction amount ' + str(totalItemizedDeductions))
		print('standard deduction amount ' + str(standardDeduction['amountDeducted']))

		if (itemizingDeductions):
			itemizingDeductions = standardDeduction['amountDeducted'] < totalItemizedDeductions
		

		print('itemizingDeductions ' + str(itemizingDeductions));

		if (itemizingDeductions):
			deductions['itemizedDeduction'] = itemizedDeduction
			deductions['stateAndLocalTaxDeduction'] = stateAndLocalTaxDeduction
			deductions['propertyTaxDeduction'] = propertyTaxDeduction
		else:
			deductions['standardDeduction'] = standardDeduction


		taxableIncome = float(income)

		# print('From TaxSystem/calcTaxedAmount:')
		# print('   Deductions:')
		# print('      type: ' + str(type(deductions)))
		# print()

		for name, deduction in deductions.items():
			taxableIncome -= deduction['amountDeducted']

		bracketResults = self.brackets[status].calcTaxedAmountForBrackets(taxableIncome)
		taxedAmountFromBrackets = bracketResults['taxedAmountFromBrackets']
		taxedAmountAfterCredits = taxedAmountFromBrackets - float(credits)

		results = {}
		results['taxSystem'] = self.name
		results['deductions'] = deductions
		results['income'] = income
		results['status'] = status
		results['credits'] = credits
		results['taxableIncome'] = taxableIncome
		results['taxedAmountFromBrackets'] = taxedAmountFromBrackets
		results['taxedAmountAfterCredits'] = taxedAmountAfterCredits
		results['bracketResults'] = bracketResults
		results['messages'] = self.messages

		return results
