from abc import ABC, abstractmethod

class MenuItem(ABC):

    def __init__(self):

        self._ingredient_prices = {
        "Sesame bun": 1,
        "Muffin bun": 1,
        "Chicken patty": 2,
        "Beef patty": 2,
        "Vegetarian patty": 2,
        "Lettuce": 0.5,
        "Onions": 0.5,
        "Tomatoes": 0.5,
        "Swiss cheese": 0.5,
        "Cheddar cheese": 0.5,
        "Tomato sauce": 0.2,
        "BBQ sauce": 0.2,
        "Aioli sauce": 0.2
        }

        self._drink_prices = {
        "Coke can": 2,
        "Coke bottle": 3.5,
        "Sprite can": 2,
        "Sprite bottle": 3.5,
        "Fanta can": 2,
        "Fanta bottle": 3.5,
        "Water bottle": 4,
        "Small orange juice": 2.5,
        "Medium orange juice": 3,
        "Large orange juice": 3.5,
        }

        self._side_prices = {
        "Small fries": 2.5,
        "Medium fries": 3.5,
        "Large fries": 4,
        "Nuggets 3P": 2.5,
        "Nuggets 6P": 4.5,
        "Cookie": 2,
        "Small chocolate sundae": 2,
        "Medium chocolate sundae": 3,
        "Large chocolate sundae": 3.5,
        "Small strawberry sundae": 2,
        "Medium strawberry sundae": 3,
        "Large strawberry sundae": 3.5
        }

    @abstractmethod
    def get_price(self):
        pass
