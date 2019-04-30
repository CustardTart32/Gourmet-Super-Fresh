from stock import Stock
from system import System
import pytest



# check Real stock and System Stock
# Should be identical if no other stock is given to system
def test_initial_stock():
    stock = Stock().get_stock()
    system_stock = System().get_stock().get_stock()
    for item in system_stock:
        assert(system_stock[item] == stock[item])

## checking updates in system_stock with original stock + updating amout
def test_successful_update_stock():
    system_stock = System().get_stock()
    stock = Stock()
    for item in system_stock.get_stock():
        system_stock.update_item(item,20)
        assert(system_stock.get_item_stock(item) == stock.get_item_stock(item) + 20)
