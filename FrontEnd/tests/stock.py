class Stock():

    # Fries stocked by weight, in g:
    # Small: 75g
    # Medium: 125g
    # Large: 175g
    #
    # Juices served in varying sizes, stocked in mL:
    # Small: 250mL
    # Medium:450mL
    # Large: 650mL
    #
    # Sundaes served in varying sizes, stocked in mL
    # Small: 200mL
    # Medium: 300mL
    # Large: 380mL

    def __init__(self):
        self._stock = {
        "Sesame bun": 15,
        "Muffin bun": 15,
        "Wrap": 15,
        "Chicken patty": 5,
        "Beef patty": 5,
        "Vegetarian patty": 5,
        "Lettuce": 10,
        "Onions": 10,
        "Tomatoes": 10,
        "Swiss cheese": 10,
        "Cheddar cheese": 10,
        "Tomato sauce": 10,
        "BBQ sauce": 10,
        "Aioli sauce": 10,
        "Coke can": 10,
        "Coke bottle": 10,
        "Sprite can": 10,
        "Sprite bottle": 10,
        "Fanta can": 10,
        "Fanta bottle": 10,
        "Water bottle": 10,
        "Orange juice": 10000,
        "Fries": 10000,
        "Nuggets": 50,
        "Cookie": 10,
        "Chocolate sundae": 10000,
        "Strawberry sundae": 10000
        }

    def update_item(self, item, quantity):
        self._stock[item] += quantity

    def get_item_stock(self, item):
        return self._stock[item]

    def get_stock(self):
        return self._stock

    def set_stock(self, stock):
        self._stock = stock
