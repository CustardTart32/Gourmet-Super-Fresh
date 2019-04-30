from menu_items import MenuItem

class Drink(MenuItem):
	def __init__(self,name):
		super().__init__()
		self._name = name

	def get_price(self):
		return self._drink_prices[self._name]

	def get_name(self):
		return self._name

	def __eq__(self,other):
		return self.get_name() == other.get_name()
