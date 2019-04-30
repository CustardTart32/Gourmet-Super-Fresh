from menu_items import MenuItem
from mains import Main, Wrap, Burger, SingleBurger, DoubleBurger, TripleBurger
from sides import Side
from drinks import Drink
from order import Order
from system import System
import pytest

# Tests for US1, US2, US3 (Adding mains, side, drinks to order)

@pytest.fixture
def system():

    system = System()

    ID = system.generate_id()

    system.new_order(ID)

    return system

def test_successful_single_burger(system):
    burger = SingleBurger()
    burger.add_ingredient("Sesame bun", 1)
    burger.add_ingredient("Muffin bun", 1)
    burger.add_ingredient("Beef patty", 1)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 2)
    assert(burger.num_patties() == 1)
    assert(burger.get_price() == 5)
    assert(burger.is_valid_main())

    assert(len(system.get_orders()) == 1)
    assert(len(system.get_order(1).get_order_list()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)

    assert(system.get_order(1).total_price() == 5)

def test_successful_double_burger(system):
    burger = DoubleBurger()
    burger.add_ingredient("Sesame bun", 1)
    burger.add_ingredient("Muffin bun", 2)
    burger.add_ingredient("Vegetarian patty", 1)
    burger.add_ingredient("Beef patty", 1)
    burger.add_ingredient("Onions", 1)
    burger.add_ingredient("Tomatoes", 2)
    burger.add_ingredient("Swiss cheese", 1)
    burger.add_ingredient("Cheddar cheese", 1)
    burger.add_ingredient("BBQ sauce", 2)
    burger.add_ingredient("Aioli sauce", 4)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 3)
    assert(burger.num_patties() == 2)
    assert(burger.get_price() == 12.7)
    assert(burger.is_valid_main())

    assert(len(system.get_orders()) == 1)
    assert(len(system.get_order(1).get_order_list()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)

    assert(system.get_order(1).total_price() == 12.7)

def test_successful_triple_burger(system):
    burger = TripleBurger()
    burger.add_ingredient("Muffin bun", 4)
    burger.add_ingredient("Chicken patty", 3)
    burger.add_ingredient("Cheddar cheese", 2)
    burger.add_ingredient("Swiss cheese", 1)
    burger.add_ingredient("Tomato sauce", 1)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 4)
    assert(burger.num_patties() == 3)
    assert(burger.get_price() == 14.2)
    assert(burger.is_valid_main())

    assert(len(system.get_orders()) == 1)
    assert(len(system.get_order(1).get_order_list()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)

    assert(system.get_order(1).total_price() == 14.2)

def test_successful_wrap(system):
    wrap = Wrap()
    wrap.add_ingredient("Chicken patty", 1)
    wrap.add_ingredient("Cheddar cheese", 3)
    wrap.add_ingredient("Aioli sauce", 1)

    system.add_to_order(wrap, 1)

    assert(wrap.num_patties() == 1)
    assert(wrap.get_price() == 5.7)
    assert(wrap.is_valid_main())

    assert(len(system.get_orders()) == 1)
    assert(len(system.get_order(1).get_order_list()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)

    assert(system.get_order(1).total_price() == 5.7)

def test_single_not_enough_buns(system):
    burger = SingleBurger()
    burger.add_ingredient("Muffin bun", 1)
    burger.add_ingredient("Beef patty", 1)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 1)
    assert(burger.num_patties() == 1)
    assert(burger.get_price() == 4)
    assert(len(burger.get_errors()) == 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)


def test_double_not_enough_buns(system):
    burger = DoubleBurger()
    burger.add_ingredient("Muffin bun", 2)
    burger.add_ingredient("Vegetarian patty", 1)
    burger.add_ingredient("Beef patty", 1)
    burger.add_ingredient("Onions", 1)
    burger.add_ingredient("Tomatoes", 2)
    burger.add_ingredient("Swiss cheese", 1)
    burger.add_ingredient("Cheddar cheese", 1)
    burger.add_ingredient("BBQ sauce", 2)
    burger.add_ingredient("Aioli sauce", 4)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 2)
    assert(burger.num_patties() == 2)
    assert(burger.get_price() == 11.7)
    assert(len(burger.get_errors()) == 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)

def test_triple_not_enough_buns(system):
    burger = TripleBurger()
    burger.add_ingredient("Chicken patty", 3)
    burger.add_ingredient("Cheddar cheese", 2)
    burger.add_ingredient("Swiss cheese", 1)
    burger.add_ingredient("Tomato sauce", 1)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 0)
    assert(burger.num_patties() == 3)
    assert(burger.get_price() == 10.2)
    assert(len(burger.get_errors()) == 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)


def test_single_not_enough_patties(system):
    burger = SingleBurger()
    burger.add_ingredient("Sesame bun", 1)
    burger.add_ingredient("Muffin bun", 1)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 2)
    assert(burger.num_patties() == 0)
    assert(burger.get_price() == 3)
    assert(len(burger.get_errors()) == 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)


def test_double_not_enough_patties(system):
    burger = DoubleBurger()
    burger.add_ingredient("Sesame bun", 1)
    burger.add_ingredient("Muffin bun", 2)
    burger.add_ingredient("Beef patty", 1)
    burger.add_ingredient("Onions", 1)
    burger.add_ingredient("Tomatoes", 2)
    burger.add_ingredient("Swiss cheese", 1)
    burger.add_ingredient("Cheddar cheese", 1)
    burger.add_ingredient("BBQ sauce", 2)
    burger.add_ingredient("Aioli sauce", 4)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 3)
    assert(burger.num_patties() == 1)
    assert(burger.get_price() == 10.7)
    assert(len(burger.get_errors()) == 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)


def test_triple_not_enough_patties(system):
    burger = TripleBurger()
    burger.add_ingredient("Muffin bun", 4)
    burger.add_ingredient("Cheddar cheese", 2)
    burger.add_ingredient("Swiss cheese", 1)
    burger.add_ingredient("Tomato sauce", 1)

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 4)
    assert(burger.num_patties() == 0)
    assert(burger.get_price() == 8.2)
    assert(len(burger.get_errors()) == 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)


def test_wrap_not_enough_patties(system):
    wrap = Wrap()
    wrap.add_ingredient("Cheddar cheese", 3)
    wrap.add_ingredient("Aioli sauce", 1)

    system.add_to_order(wrap, 1)

    assert(wrap.num_patties() == 0)
    assert(wrap.get_price() == 3.7)
    assert(len(wrap.get_errors()) == 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)


def test_single_no_patties_no_buns(system):
    burger = SingleBurger()

    system.add_to_order(burger, 1)

    assert(burger.num_buns() == 0)
    assert(burger.num_patties() == 0)
    assert(burger.get_price() == 1)
    assert(len(burger.get_errors()) == 2)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 0)

    assert(system.get_order(1).total_price() == 0)


def test_successful_sides(system):
    side1 = Side("Small fries")
    side2 = Side("Cookie")

    system.add_to_order(side1, 1)
    system.add_to_order(side2, 1)

    assert(side1.get_price() == 2.5)
    assert(side1.get_name() == "Small fries")
    assert(side2.get_price() == 2)
    assert(side2.get_name() == "Cookie")

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 2)

    assert(system.get_order(1).total_price() == 4.5)

def test_successful_drink(system):
    drink1 = Drink("Fanta can")
    drink2 = Drink("Water bottle")

    system.add_to_order(drink1, 1)
    system.add_to_order(drink2, 1)

    assert(drink1.get_price() == 2)
    assert(drink1.get_name() == "Fanta can")
    assert(drink2.get_price() == 4)
    assert(drink2.get_name() == "Water bottle")

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 2)

    assert(system.get_order(1).total_price() == 6)

def test_multiple_items(system):

    side1 = Side("Small fries")
    side2 = Side("Cookie")

    burger = SingleBurger()
    burger.add_ingredient("Sesame bun", 1)
    burger.add_ingredient("Muffin bun", 1)
    burger.add_ingredient("Beef patty", 1)

    wrap = Wrap()
    wrap.add_ingredient("Chicken patty", 1)
    wrap.add_ingredient("Cheddar cheese", 3)
    wrap.add_ingredient("Aioli sauce", 1)

    drink1 = Drink("Fanta can")
    drink2 = Drink("Water bottle")

    system.add_to_order(drink1, 1)
    system.add_to_order(drink2, 1)
    system.add_to_order(wrap, 1)
    system.add_to_order(burger, 1)
    system.add_to_order(side1, 1)
    system.add_to_order(side2, 1)

    assert(len(system.get_orders()) == 1)
    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 6)

    assert(system.get_order(1).total_price() == 21.2)

def test_multiple_orders(system):

    system.new_order(system.generate_id())

    drink1 = Drink("Fanta can")
    drink2 = Drink("Water bottle")

    system.add_to_order(drink1, 1)
    system.add_to_order(drink2, 1)

    side1 = Side("Small fries")
    side2 = Side("Cookie")

    system.add_to_order(side1, 2)
    system.add_to_order(side2, 2)

    assert(system.get_order(1).get_status() == False)
    assert(system.get_order(1).get_confirmed() == False)
    assert(len(system.get_order(1).get_order_list()) == 2)
    assert(system.get_order(1).total_price() == 6)

    assert(system.get_order(2).get_status() == False)
    assert(system.get_order(2).get_confirmed() == False)
    assert(len(system.get_order(2).get_order_list()) == 2)
    assert(system.get_order(2).total_price() == 4.5)

    assert(len(system.get_orders()) == 2)
