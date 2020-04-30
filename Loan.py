from numpy import long


class Loan:
	def __init__(self, id, loan_amount, country_name, status, time_to_raise, num_lenders_total):
		self.id = int(id)
		self.loan_amount = int(loan_amount)
		self.country_name = country_name
		self.status = status
		self.time_to_raise = int(time_to_raise)
		self.num_lenders_total = int(num_lenders_total)
