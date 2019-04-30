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
	success,ID = system.confirm_order(system.get_order(ID))
	assert(success == True)
	assert(ID == 1)
	system.update_status(1)


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
	success,ID = system.confirm_order(system.get_order(ID))
	assert(success == True)
	assert(ID == 2)

	ID = system.generate_id()
	assert(ID == 3)
	system.new_order(ID)
	for i in range(5):
		system.add_to_order(Drink("Coke can"),ID)
		system.add_to_order(Side("Cookie"),ID)

	assert(system.get_order(ID).total_price() == 20)
	success,ID = system.confirm_order(system.get_order(ID))
	assert(success == True)
	assert(ID == 3)
	system.update_status(3)

	return system 


def test_check_order_ID_1(system_fixture):
	assert(system_fixture.check_status(1) == True)
	assert(system_fixture.check_status(2) == False)
	assert(system_fixture.check_status(3) == True)

	assert(len(system_fixture.get_orders()) == 1)
	assert(len(system_fixture.get_completed()) == 2)

def test_check_order_invalid_ID(system_fixture):
	with pytest.raises(InvalidID) as err:
		system_fixture.check_status(4)

	with pytest.raises(InvalidID) as err:
		system_fixture.check_status('abc')

def test_check_order_after_update(system_fixture):
	assert(system_fixture.check_status(2) == False)

	system_fixture.update_status(2)
	assert(system_fixture.check_status(2) == True)

	assert(len(system_fixture.get_orders()) == 0)
	assert(len(system_fixture.get_completed()) == 3)









