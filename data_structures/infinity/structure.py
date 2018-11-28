

class Infinity(object):
	def __str__(self):
		return "inf"

	def __gt__(self, other):
		return True

	def __ge__(self, other):
		return True

	def __lt__(self, other):
		return False

	def __le__(self, other):
		return False

	def __eq__(self, other):
		return False

	def __ne__(self, other):
		return True


class NegativeInfinity(object):
	def __str__(self):
		return "neg_inf"

	def __gt__(self, other):
		return False

	def __ge__(self, other):
		return False

	def __lt__(self, other):
		return True

	def __le__(self, other):
		return True

	def __eq__(self, other):
		return False

	def __ne__(self, other):
		return True
