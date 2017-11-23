import json

class CreditConfiguration:
	def __init__(self, name, creditAllowed=1, maxCredit=float('inf'), maxIncome={'single': float('inf'), 'married': float('inf')}, phaseOut=0, phaseOutAmount={'excedingAmount': float('inf'), 'reductionInCredit': 0}, staticCreditAmount=0, staticCreditDelta = 0, message = ''):
		self.name = name
		self.creditAllowed = creditAllowed
		self.maxCredit = float(maxCredit)
		self.staticCreditAmount = float(staticCreditAmount)
		self.staticCreditDelta = float(staticCreditDelta)
		self.phaseOut = phaseOut
		self.phaseOutAmount = phaseOutAmount
		self.maxIncome = maxIncome
		self.message = message

	def calcCredit(self, amountRequested=0, numberRequested=1, income=0, status='single'):
		amountCredited = 0

		#Dedtermine if this is a static Credit
		if(self.staticCreditAmount == 0):
			numberCredited = 0
		else:
			numberCredited = numberRequested + self.staticCreditDelta

		if (numberCredited < 0):
			numberCredited = 0

		# print('From CreditConfiguration/calcCredit')
		# print('  Calculating Credit ' + self.name)
		# print('  CreditConfig ' + json.dumps(self.__dict__))

		# For Credits with phase outs, reduce the credit per number requested by the phase out reduction in credit for every phaseOutExceding amount about the max income.
		creditPerNumberRequested = self.staticCreditAmount
		if (self.phaseOut == 1 and income > self.maxIncome[status]):
			creditPerNumberRequested -= ((income - self.maxIncome[status]) % self.phaseOutAmount['excedingAmount']) * self.phaseOutAmount['reductionInCredit']

		# Calculate Credit Amount
		if self.creditAllowed != 0:
			if self.staticCreditAmount != 0:
				amountCredited = numberCredited * creditPerNumberRequested
			else:
				if amountRequested > self.maxCredit:
					amountCredited = self.maxCredit
				else: 
					amountCredited = amountRequested
		else:
			numberCredited = 0


		# Build Return Dictionary
		results = {}
		results['name'] = self.name
		results['message'] = self.message
		results['creditAllowed'] = self.creditAllowed
		results['maxCredit'] = str(self.maxCredit)
		results['staticCreditAmount'] = self.staticCreditAmount
		results['creditPerNumberRequested'] = creditPerNumberRequested
		results['staticCreditDelta'] = self.staticCreditDelta
		results['amountRequested'] = amountRequested
		results['amountCredited'] = amountCredited
		results['numberCredited'] = numberCredited

		# print('   Results: ' + json.dumps(results))
		# print('   Results type ' + str(type(results)))
		# print()

		return results