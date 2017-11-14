class TaxBracket:

	def __init__(self, order, start, end, percent):
		self.start = start;
		self.end = end;
		self.percent = percent;
		self.order = order;
	
	def calcTaxedAmount(self, totalIncome):
		totalIncome = float(totalIncome)
		taxedAmount = 0;
		incomeInBracket = 0;
		if totalIncome > self.end:
			incomeInBracket = self.end - self.start
		elif totalIncome < self.start:
			incomeInBracket = 0
		else:
			incomeInBracket = totalIncome - self.start

		taxedAmount = incomeInBracket * self.percent

		results = {
			'order'       : self.order,
			'start'       : self.start,
			'end'         : str(self.end),
			'percent'     : self.percent,
			'taxedAmount' : taxedAmount,
			'incomeInBracket' : incomeInBracket
		}

		return results
