class TaxBracket:

	def __init__(self, order, start, end, percent):
		self.start = start;
		self.end = end;
		self.percent = percent;
		self.order = order;
	
	def calcTaxedAmount(self, totalIncome):
		totalIncome = float(totalIncome)
		taxedAmount = 0;
		if totalIncome > self.end:
			taxedAmount = (self.end - self.start) * self.percent;
		elif totalIncome < self.start:
			taxedAmount = 0;
		else:
			taxedAmount = (totalIncome - self.start) * self.percent;

		results = {
			'order'       : self.order,
			'start'       : self.start,
			'end'         : self.end,
			'percent'     : self.percent,
			'taxedAmount' : taxedAmount
		}

		return results
