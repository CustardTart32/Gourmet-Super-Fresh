from src.menu_items import MenuItem
from src.sides import Side
from src.mains import Main,Wrap,SingleBurger,DoubleBurger,TripleBurger,Burger
from src.drinks import Drink

class Order():

	def __init__(self):
		self._order_list = []
		self._status = False
		self._ID = 0
		self._confirmed = False

	#Add an object to the order
	def add_item(self,item):
		if isinstance(item,Main):
			if (item.is_valid_main() == False):
				return False

		self._order_list.append(item)
		return True

	#Returns total price of an order
	def total_price(self):
		price = 0
		for item in self._order_list:
			price += item.get_price()

		return price

	def get_confirmed(self):
		return self._confirmed

	def set_confirmed(self,status):
		self._confirmed = status

	def get_status(self):
		return self._status

	def set_status(self,status):
		self._status = status

	def get_ID(self):
		return self._ID

	def set_ID(self,ID):
		self._ID = ID

	def get_order_list(self):
		return self._order_list

