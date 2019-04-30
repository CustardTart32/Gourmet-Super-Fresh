from src.order import Order
from src.menu_items import MenuItem
from src.sides import Side
from src.mains import Main,Wrap,SingleBurger,DoubleBurger,TripleBurger,Burger
from src.drinks import Drink
from src.stock import Stock
from src.errors import *


class System():
    def __init__(self,stock=None):

        if stock is None:
            self._stock = Stock()
        else:
            self._stock = stock

        self._orders = []
        self._completed = []
        #self._curr_id = 0

    def check_status(self,ID):
        order = self.get_order(ID)
        completed_order = self.get_completed_order(ID)
        if (order is None and completed_order is None):
            raise InvalidID("No order exists for ID of:" + str(ID))

        if order is None:
            return True
        else:
            return False

    def get_orders(self):
        return self._orders

    def get_completed(self):
        return self._completed

    def get_completed_order(self,ID):
        for order in self._completed:
            if (order.get_ID() == ID):
                return order

        return None

    def get_stock(self):
        return self._stock

    def update_status(self,ID):
        updating_order = self.get_order(ID)
        updating_order.set_status(True)
        self._completed.append(updating_order)
        self.remove_order(ID)

    def get_order(self,ID):
        for order in self._orders:
            if (order.get_ID() == ID):
                return order

        return None

    def generate_id(self):
        ID = len(self._orders) + len(self._completed) + 1
        #self._curr_id += 1
        return ID


    def new_order(self, id):
        new_order = Order()

        new_order.set_ID(id)
        self._orders.append(new_order)

        return new_order


    def remove_order(self,ID):
        self._orders.remove(self.get_order(ID))


    def update_stock(self,item,quantity):
        self._stock.update_item(item,quantity)


    def max_allowed(self, item):
        return self._stock.get_item_stock(item)

    def check_stocks(self,order, stocks):
        errors = []
        order_list = order.get_order_list()

        for item in order_list:
            if (isinstance(item,Wrap)):
                stocks['Wrap'] -= 1

            if (isinstance(item,Main)):
                for ingredient in item.get_ingredients():
                    stocks[ingredient] -= item.get_ingredients()[ingredient]

            elif (item.get_name() == "Small fries"):
                 stocks["Fries"] -= 75

            elif (item.get_name() == "Medium fries"):
                stocks["Fries"] -= 125

            elif (item.get_name() == "Large fries"):
                stocks["Fries"] -= 175

            elif (item.get_name() == "Small orange juice"):
                stocks["Orange juice"] -= 250

            elif (item.get_name() == "Medium orange juice"):
                stocks["Orange juice"] -= 450

            elif (item.get_name() == "Large orange juice"):
                stocks["Orange juice"] -= 600

            elif (item.get_name() == "Nuggets 3P"):
                stocks["Nuggets"] -= 3

            elif (item.get_name() == "Nuggets 6P"):
                stocks["Nuggets"] -= 6

            elif (item.get_name() == "Small chocolate sundae"):
                stocks["Chocolate sundae"] -= 200

            elif (item.get_name() == "Medium chocolate sundae"):
                stocks["Chocolate sundae"] -= 300

            elif (item.get_name() == "Large chocolate sundae"):
                stocks["Chocolate sundae"] -= 380

            elif (item.get_name() == "Small strawberry sundae"):
                stocks["Strawberry sundae"] -= 200

            elif (item.get_name() == "Medium strawberry sundae"):
                stocks["Strawberry sundae"] -= 300

            elif (item.get_name() == "Large strawberry sundae"):
                stocks["Strawberry sundae"] -= 380

            else:
                stocks[item.get_name()] -= 1


        for item in stocks:
            if (stocks[item] < 0):
                    errors.append('Amount of ' + item + ' selected exceeds existing stock amount. Please create a new order')

        if (len(errors) != 0):
            return False, stocks, errors
        else:
            return True, stocks, errors

    def confirm_order(self,my_order):
        valid_order, stock_copy, errors = self.check_stocks(my_order,self._stock.get_stock().copy())
        if valid_order == False:
            raise OrderError(errors)
        if (len(my_order.get_order_list()) == 0):
            raise OrderError("Your order has no items.")

        my_order.set_confirmed(True)
        #self._orders.append(my_order)
        self._stock.set_stock(stock_copy)
        return True, my_order.get_ID()

    def add_to_order(self, item, ID):
        order = self.get_order(ID)
        order.add_item(item)

    def get_main_list(self):
        burger = SingleBurger()

        ingredients = []

        for ingredient in burger.get_ingredient_prices():
            ingredients.append(ingredient)

        return ingredients

    def get_sidelist(self):
        eg_side = Side("Small fries")
        sidelist = []

        for key,value in eg_side._side_prices.items():
            sidelist.append(key)
        return sidelist


    def get_drinklist(self):
        eg_drink = Drink("Coke can")
        drinklist = []

        for key,value in eg_drink._drink_prices.items():
            drinklist.append(key)
        return drinklist
