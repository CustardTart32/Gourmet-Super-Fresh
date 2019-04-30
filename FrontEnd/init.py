from src.system import System

from src.order import Order
from src.menu_items import MenuItem
from src.sides import Side
from src.mains import Main,Wrap,SingleBurger,DoubleBurger,TripleBurger,Burger
from src.drinks import Drink
from src.stock import Stock
from src.errors import *

def bootstrap_system():
    system = System()

    return system
