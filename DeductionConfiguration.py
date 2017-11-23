import json

class DeductionConfiguration:
	def __init__(self, name, deductionAllowed=1, maxDeduction=float("inf"), staticDeductionAmount=0, staticDeductionDelta=0, message=''):
		self.name = name
		self.deductionAllowed = deductionAllowed
		self.maxDeduction = float(maxDeduction)
		self.staticDeductionAmount = float(staticDeductionAmount)
		self.staticDeductionDelta = float(staticDeductionDelta)
		self.message = message

	def calcDeduction(self, amountRequested=0, numberRequested=1):
		amountDeducted = 0

		if(self.staticDeductionAmount == 0):
			numberDeducted = 0
		else:
			numberDeducted = numberRequested + self.staticDeductionDelta

		if (numberDeducted < 0):
			numberDeducted = 0

		# print('From DeductionConfiguration/calcDeduction')
		# print('  Calculating Deduction ' + self.name)
		# print('  DeductionConfig ' + json.dumps(self.__dict__))

		if self.deductionAllowed != 0:
			if self.staticDeductionAmount != 0:
				amountDeducted = numberDeducted * self.staticDeductionAmount
			else:
				if amountRequested > self.maxDeduction:
					amountDeducted = self.maxDeduction
				else: 
					amountDeducted = amountRequested
		else:
			numberDeducted = 0

		results = {}
		results['name'] = self.name
		results['message'] = self.message
		results['deductionAllowed'] = self.deductionAllowed
		results['maxDeduction'] = str(self.maxDeduction)
		results['staticDeductionAmount'] = self.staticDeductionAmount
		results['staticDeductionDelta'] = self.staticDeductionDelta
		results['amountRequested'] = amountRequested
		results['amountDeducted'] = amountDeducted
		results['numberDeducted'] = numberDeducted

		# print('   Results: ' + json.dumps(results))
		# print('   Results type ' + str(type(results)))
		# print()

		return results