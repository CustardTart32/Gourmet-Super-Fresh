from mains import Main, Wrap, Burger, SingleBurger, DoubleBurger, TripleBurger
from sides import Side
from drinks import Drink
from order import Order
from system import System
import pytest



@pytest.fixture
def system_fixture():
    system = System()

    order = system.new_order(system.generate_id())
    burger = SingleBurger()
    burger.add_ingredient("Sesame bun", 1)
    burger.add_ingredient("Muffin bun", 1)
    burger.add_ingredient("Beef patty", 1)

    order.add_item(burger)
    order.add_item(Drink("Water bottle"))
    order.add_item(Side("Small fries"))
    order.add_item(Side("Nuggets 3P"))

    order2 = system.new_order(system.generate_id())
    burger2 = SingleBurger()
    burger2.add_ingredient("Sesame bun", 1)
    burger2.add_ingredient("Muffin bun", 1)
    burger2.add_ingredient("Beef patty", 1)

    order2.add_item(burger)
    order2.add_item(Drink("Coke Can"))
    order2.add_item(Side("Medium fries"))
    order2.add_item(Side("Nuggets 6P"))

    return system

def test_empty_order():
    system = System()
    assert(len(system.get_orders()) == 0)
    assert(len(system.get_completed()) == 0)

def test_adding_first_order():
    system = System()
    assert(len(system.get_orders()) == 0)
    assert(len(system.get_completed()) == 0)
    order = system.new_order(system.generate_id())
    burger = SingleBurger()
    burger.add_ingredient("Sesame bun", 1)
    burger.add_ingredient("Muffin bun", 1)
    burger.add_ingredient("Beef patty", 1)
    order.add_item(burger)
    order.add_item(Drink("Water bottle"))
    order.add_item(Side("Small fries"))
    order.add_item(Side("Nuggets 3P"))
    success,orderID = system.confirm_order(order)
    assert(success == True)
    assert(orderID == 1)
    assert(len(system.get_orders()) == 1)
    assert(len(system.get_completed()) == 0)

def test_successful_complete_order(system_fixture):
    assert(len(system_fixture.get_orders())==2)
    assert(len(system_fixture.get_completed())==0)
    system_fixture.update_status(1)
    assert(len(system_fixture.get_orders())==1)
    assert(len(system_fixture.get_completed())==1)
    system_fixture.update_status(2)
    assert(len(system_fixture.get_orders())==0)
    assert(len(system_fixture.get_completed())==2)
