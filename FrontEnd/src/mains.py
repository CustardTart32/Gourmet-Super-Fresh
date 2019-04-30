from src.menu_items import MenuItem
from abc import abstractproperty,abstractmethod

class Main(MenuItem):
    def __init__(self):
        super().__init__()
        self._ingredients = {}
        self._errors = []

    #Valid order will not check for stock - this will be handled in the front end
    @abstractmethod
    def is_valid_main(self):
        pass

    @abstractmethod
    def type_main(self):
        pass


    #Adds an ingredient to the order
    def add_ingredient(self, ingredient, quantity):
        self._ingredients[ingredient] = quantity

    #Counts number of patties in burger/wrap
    def num_patties(self):
        patties = 0

        for ingredient in self._ingredients:
            if "patty" in ingredient:
                patties += self._ingredients[ingredient]

        return patties

    #Returns price of any ingredient in a main; used for displaying to customer
    def get_ingredient_price(self, ingredient):
        return self._ingredient_prices[ingredient]


    #Returns price list of main ingredients; used for displaying to customer
    def get_ingredient_prices(self):
        return self._ingredient_prices

    #Returns list of ingredients in a main
    def get_ingredients(self):
        return self._ingredients

    def get_num_ingredients(self, ingredient):
        return self._ingredients[ingredient]

    #Returns total price of the burger/wrap
    def get_price(self):
        price = 0

        for ingredient,value in self._ingredients.items():
            price += self._ingredient_prices[ingredient] * value

        return round(price + self._base_price, 2)

    #Return dictionary of errors for Main, used to display error to customer
    def get_errors(self):
        return self._errors

    def __eq__(self, other):
        return self.get_ingredients() == other.get_ingredients()
    def get_name(self):
        return self.type_main(),self.get_ingredients()

class Wrap(Main):

    def __init__(self):
        super().__init__()
        self._base_price = 2

    #Checks 1 patty has been added
    def is_valid_main(self):

        if self.num_patties() == 0:
            self._errors.append("Please select more than 0 patties")

        if self.num_patties() > 1:
            self._errors.append("Please select only 1 patty")

        if self._errors:
            return False
        else:
            return True

    def type_main(self):
        return 'Wrap'

class Burger(Main):

    def __init__(self):
        super().__init__()

    #Counts number of buns in burger
    def num_buns(self):
        buns = 0

        for ingredient in self._ingredients:
            if "bun" in ingredient:
                buns += self._ingredients[ingredient]

        return buns

    @abstractmethod
    def is_valid_main(self):
        pass

    @abstractmethod
    def type_main(self):
        pass


class SingleBurger(Burger):

    def __init__(self):
        super().__init__()
        self._base_price  = 1

    def is_valid_main(self):

        if self.num_buns() != 2:
            self._errors.append("Please select 2 buns for a single burger")

        if self.num_patties() != 1:
            self._errors.append("Please select 1 patty for a single burger")

        if self._errors:
            return False
        else:
            return True

    def type_main(self):
        return "Single Burger"



class DoubleBurger(Burger):

    def __init__(self):
        super().__init__()
        self._base_price = 2

    def is_valid_main(self):

        if self.num_buns() != 3:
            self._errors.append("Please select 3 buns for a double burger")

        if self.num_patties() != 2:
            self._errors.append("Please select 2 patties for a double burger")

        if self._errors:
            return False
        else:
            return True

    def type_main(self):
        return "Double Burger"



class TripleBurger(Burger):

    def __init__(self):
        super().__init__()
        self._base_price = 2.5

    def is_valid_main(self):

        if self.num_buns() != 4:
            self._errors.append("Please select 4 buns for a triple burger")

        if self.num_patties() != 3:
            self._errors.append("Please select 3 patties for a triple burger")

        if self._errors:
            return False
        else:
            return True

    def type_main(self):
        return "Triple Burger"
