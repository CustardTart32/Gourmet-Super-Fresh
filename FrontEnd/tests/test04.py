from menu_items import MenuItem
from mains import Main, Wrap, Burger, SingleBurger, DoubleBurger, TripleBurger
from order import Order
from system import System
from stock import Stock
from errors import *
from sides import Side 
from drinks import Drink 

import pytest

@pytest.fixture
def system_fixture():
	system = System()

	ID = system.generate_id()
	assert(ID == 1)
	system.new_order(ID)

	burger = SingleBurger()
	burger.add_ingredient("Sesame bun", 1)
	burger.add_ingredient("Muffin bun", 1)
	burger.add_ingredient("Beef patty", 1)
	burger.add_ingredient("Lettuce",3)
	burger.add_ingredient("Tomatoes",2)
	system.add_to_order(burger,ID)
	system.add_to_order(Drink('Water bottle'),ID)
	system.add_to_order(Side("Cookie"),ID)

	assert(system.get_order(ID).total_price() == 13.5)

	ID = system.generate_id()
	assert(ID == 2)
	system.new_order(ID)

	burger = DoubleBurger()
	burger.add_ingredient("Sesame bun", 2)
	burger.add_ingredient("Muffin bun", 1)
	burger.add_ingredient("Beef patty", 2)
	burger.add_ingredient("Lettuce",3)
	burger.add_ingredient("Tomatoes",2)
	burger.add_ingredient("BBQ sauce",2)
	system.add_to_order(burger,ID)
	
	system.add_to_order(Drink('Coke can'),ID)
	system.add_to_order(Side("Medium fries"),ID)

	assert(system.get_order(ID).total_price() == 17.4)

	ID = system.generate_id()
	assert(ID == 3)
	system.new_order(ID)
	for i in range(20):
		system.add_to_order(Drink("Coke can"),ID)
		system.add_to_order(Side("Cookie"),ID)


	ID = system.generate_id()
	assert(ID == 4)
	system.new_order(ID)

	wrap = Wrap()
	wrap.add_ingredient("Chicken patty", 1)
	wrap.add_ingredient("Cheddar cheese", 3)
	wrap.add_ingredient("Aioli sauce", 1)
	system.add_to_order(wrap,ID)

	assert(system.get_order(ID).total_price() == 5.7)

	return system 


def test_single_successful_booking(system_fixture):
	order = system_fixture.get_order(1)
	success,ID = system_fixture.confirm_order(order)
	assert(success == True)
	assert(ID == 1)

	assert(order.get_status() == False)
	assert(order.get_confirmed() == True)
	assert(order.total_price() == 13.5)


def test_single_successful_booking_with_stock(system_fixture):
	order = system_fixture.get_order(1)
	success,ID = system_fixture.confirm_order(order)

	assert(system_fixture.get_stock().get_item_stock("Sesame bun") == 14)
	assert(system_fixture.get_stock().get_item_stock("Muffin bun") == 14)
	assert(system_fixture.get_stock().get_item_stock("Beef patty") == 4)
	assert(system_fixture.get_stock().get_item_stock("Lettuce") == 7)
	assert(system_fixture.get_stock().get_item_stock("Tomatoes") == 8)

	assert(system_fixture.get_stock().get_item_stock("Water bottle") == 9)
	assert(system_fixture.get_stock().get_item_stock("Cookie") == 9)

def test_mulitple_succesful_bookings(system_fixture):
	order = system_fixture.get_order(1)
	success,ID = system_fixture.confirm_order(order)
	assert(success == True)
	assert(ID == 1)

	assert(order.get_status() == False)
	assert(order.get_confirmed() == True)
	assert(order.total_price() == 13.5)

	order = system_fixture.get_order(2)
	success,ID = system_fixture.confirm_order(order)
	assert(success == True)
	assert(ID == 2)

	assert(order.get_status() == False)
	assert(order.get_confirmed() == True)
	assert(order.total_price() == 17.4)

	order = system_fixture.get_order(4)
	success,ID = system_fixture.confirm_order(order)	

	assert(success == True)
	assert(ID == 4)	

	assert(order.get_status() == False)
	assert(order.get_confirmed() == True)
	assert(order.total_price() == 5.7)

def test_mulitple_successful_bookings_with_stock(system_fixture):
	order = system_fixture.get_order(1)
	success,ID = system_fixture.confirm_order(order)

	order = system_fixture.get_order(2)
	success,ID = system_fixture.confirm_order(order)

	order = system_fixture.get_order(4)
	success,ID = system_fixture.confirm_order(order)

	assert(system_fixture.get_stock().get_item_stock("Sesame bun") == 12)
	assert(system_fixture.get_stock().get_item_stock("Muffin bun") == 13)
	assert(system_fixture.get_stock().get_item_stock("Beef patty") == 2)
	assert(system_fixture.get_stock().get_item_stock("Chicken patty") == 4)
	assert(system_fixture.get_stock().get_item_stock("Lettuce") == 4)
	assert(system_fixture.get_stock().get_item_stock("Tomatoes") == 6)
	assert(system_fixture.get_stock().get_item_stock("BBQ sauce") == 8)
	assert(system_fixture.get_stock().get_item_stock("Cheddar cheese") == 7)
	assert(system_fixture.get_stock().get_item_stock("Aioli sauce") == 9)
	assert(system_fixture.get_stock().get_item_stock("Wrap") == 14)

	assert(system_fixture.get_stock().get_item_stock("Water bottle") == 9)
	assert(system_fixture.get_stock().get_item_stock("Cookie") == 9)

	assert(system_fixture.get_stock().get_item_stock("Coke can") == 9)
	assert(system_fixture.get_stock().get_item_stock("Fries") == 9875)



def test_unsuccesful_booking(system_fixture):
	order = system_fixture.get_order(3)
	with pytest.raises(OrderError) as err:
		success,ID = system_fixture.confirm_order(order)
	
	#assert(err.value == ['Coke can is out of stock. Please order a different item', 'Cookie is out of stock. Please order a different item'] )
	#assert(err.get_message()[1] == "Cookie is out of stock. Please order a different item")
	#assert(len(err.get_message()) == 2)
	#assert(err)

	assert(system_fixture.get_stock().get_item_stock("Coke can") == 10)
	assert(system_fixture.get_stock().get_item_stock("Cookie") == 10)





