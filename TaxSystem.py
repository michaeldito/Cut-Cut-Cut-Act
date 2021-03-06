from TaxBrackets import *;

class TaxSystem:
	
	def __init__(self, name, brackets, deductionConfigurations, creditConfigurations, messages=[]):
		self.name = name
		self.brackets = brackets
		self.deductionConfigurations = deductionConfigurations
		self.creditConfigurations = creditConfigurations
		self.messages = messages

	def calcTaxedAmount(self, income, status, itemizedDeductionsRequested=0, stateAndLocalTaxDeductionRequested=0, propertyTaxDeductionRequested=0, medicalExpensesDeductionRequested=0, tuitionWaved=0, childDependents=0, nonChildDependents=0):
		calculationMessages = []

		deductions = {}

		# Add tuition waved to income. For the current tax system, tuition wavers are not considered income and will be removed via a deduction
		income = float(income) + float(tuitionWaved);


		# Calc the personal exemption
		personalExemptionsRequested = 1 + nonChildDependents + childDependents;
		if (status == 'married'):
			personalExemptionsRequested += 1
		deductions['personalExemption'] = self.deductionConfigurations['personalExemption'].calcDeduction(numberRequested=personalExemptionsRequested)

		deductions['tuitionWaverDeduction'] = self.deductionConfigurations['tuitionWaverDeduction'].calcDeduction(tuitionWaved)

		# Determine whether we will be taking the standard deduction, or itemizing deductions
		itemizingDeductions = (itemizedDeductionsRequested != 0 and self.deductionConfigurations['itemizedDeductions'].deductionAllowed == 1) or (stateAndLocalTaxDeductionRequested != 0 and self.deductionConfigurations['stateAndLocalTaxDeduction'].deductionAllowed == 1) or (propertyTaxDeductionRequested != 0 and self.deductionConfigurations['propertyTaxDeduction'].deductionAllowed == 1) or (medicalExpensesDeductionRequested != 0 and self.deductionConfigurations['medicalExpensesDeduction'].deductionAllowed == 1)

		itemizedDeduction = self.deductionConfigurations['itemizedDeductions'].calcDeduction(float(itemizedDeductionsRequested));
		stateAndLocalTaxDeduction = self.deductionConfigurations['stateAndLocalTaxDeduction'].calcDeduction(float(stateAndLocalTaxDeductionRequested))
		propertyTaxDeduction = self.deductionConfigurations['propertyTaxDeduction'].calcDeduction(float(propertyTaxDeductionRequested))

		# Medical Expenses can only be deducted if they are greater than 10% of income
		if (float(medicalExpensesDeductionRequested) > 0.1 * income):
			medicalExpensesDeduction = self.deductionConfigurations['medicalExpensesDeduction'].calcDeduction(float(medicalExpensesDeductionRequested))
			calculationMessages.append('You have enough medical expenses to get the medical expenses deduction if it is allowed in this tax system.')
		else:
			medicalExpensesDeduction = self.deductionConfigurations['medicalExpensesDeduction'].calcDeduction(0)
			calculationMessages.append('You do not have enough medical expenses to get the medical expenses deduction.')

		print('Medical Expenses deduction ' + str(medicalExpensesDeduction['amountDeducted']))


		if status == 'single':
			standardDeduction = self.deductionConfigurations['standardDeductionSingle'].calcDeduction()
		elif status == 'married':
			standardDeduction = self.deductionConfigurations['standardDeductionMarried'].calcDeduction()

		totalItemizedDeductions = itemizedDeduction['amountDeducted'] + stateAndLocalTaxDeduction['amountDeducted'] + propertyTaxDeduction['amountDeducted'] + medicalExpensesDeduction['amountDeducted']

		print('itemized deduction amount ' + str(totalItemizedDeductions))
		print('standard deduction amount ' + str(standardDeduction['amountDeducted']))

		if (itemizingDeductions):
			itemizingDeductions = standardDeduction['amountDeducted'] < totalItemizedDeductions
		

		print('itemizingDeductions ' + str(itemizingDeductions));

		# Build deductions
		if (itemizingDeductions):
			calculationMessages.append('Your itemized deductions are greater than the standard deduction, so we are itemizing your deductions.')
			deductions['itemizedDeduction'] = itemizedDeduction
			deductions['stateAndLocalTaxDeduction'] = stateAndLocalTaxDeduction
			deductions['propertyTaxDeduction'] = propertyTaxDeduction
			deductions['medicalExpensesDeduction'] = medicalExpensesDeduction
		else:
			calculationMessages.append('The standard deduction is greater than your itemized deductions, so we are taking the standard deduction.')
			deductions['standardDeduction'] = standardDeduction


		# Calculate taxable income by subtracting deductions from income
		taxableIncome = float(income)

		# print('From TaxSystem/calcTaxedAmount:')
		# print('   Deductions:')
		# print('      type: ' + str(type(deductions)))
		# print()

		for name, deduction in deductions.items():
			taxableIncome -= deduction['amountDeducted']

		# Calc the amount of tax based on taxable income and the tax brackets

		bracketResults = self.brackets[status].calcTaxedAmountForBrackets(taxableIncome)
		taxedAmountFromBrackets = bracketResults['taxedAmountFromBrackets']

		# Subtract tax credits from taxed amount after brackets. 
		credits = {}

		familyTaxCreditNumberRequested = 1 + nonChildDependents;
		if (status == 'married'):
			familyTaxCreditNumberRequested += 1


		credits['childTaxCredit'] = self.creditConfigurations['childTaxCredit'].calcCredit(numberRequested=childDependents, income=income, status=status)
		credits['familyTaxCredit'] = self.creditConfigurations['familyTaxCredit'].calcCredit(numberRequested=familyTaxCreditNumberRequested, income=income, status=status)
		
		taxedAmountAfterCredits = taxedAmountFromBrackets

		for name, credit in credits.items():
			taxedAmountAfterCredits -= credit['amountCredited']

		if (taxedAmountAfterCredits < 0):
			taxedAmountAfterCredits = 0

		results = {}
		results['taxSystem'] = self.name
		results['taxSystemMessages'] = self.messages
		results['calculationMessages'] = calculationMessages
		results['income'] = income
		results['status'] = status
		results['deductions'] = deductions
		results['taxableIncome'] = taxableIncome
		results['bracketResults'] = bracketResults
		results['taxedAmountFromBrackets'] = taxedAmountFromBrackets
		results['credits'] = credits
		results['taxedAmountAfterCredits'] = taxedAmountAfterCredits

		return results
