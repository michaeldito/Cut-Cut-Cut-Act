class TaxBracket:

	def __init__(self, start, end, percent):
		self.start = start;
		self.end = end;
		self.percent = percent;
	
	def calcTaxedAmount(self, totalIncome):
		if totalIncome > self.end:
			return (self.end - self.start) * self.percent;
		elif totalIncome < self.start:
			return 0;
		else:
			return (totalIncome - self.start) * self.percent;
		
