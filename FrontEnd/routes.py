from flask import render_template, request, redirect, url_for, abort, Flask
from server import app,system

from src.order import Order
from src.menu_items import MenuItem
from src.sides import Side
from src.mains import Main,Wrap,SingleBurger,DoubleBurger,TripleBurger,Burger
from src.drinks import Drink
from src.stock import Stock
from src.errors import *


@app.route('/', methods=["GET", "POST"])
def home():
    if (request.method == "POST"):
        #order = system.new_order()
        ID = system.generate_id()

        if request.form["start"] == "Get started":
            return render_template('welcome.html', start=True, ID=ID)

    return render_template('welcome.html')


@app.route('/burgers/custom/<ID>', methods = ['GET', 'POST'])
def burger(ID):

    items = system.get_main_list()

    if (request.method == 'POST'):

        if (system.get_order(int(ID)) == None):
            system.new_order(int(ID))

        if (request.form['burger_tier'] == 'single'):
            burger = SingleBurger()
        elif (request.form['burger_tier'] == 'double'):
            burger = DoubleBurger()
        elif (request.form['burger_tier'] == 'triple'):
            burger = TripleBurger()

        for ingredient in items:
            if (int(request.form[ingredient]) != 0):
                burger.add_ingredient(ingredient, int(request.form[ingredient]))


        if (burger.is_valid_main() == False):
            errors = burger.get_errors()
            return render_template('burger.html', items=items, errors=errors, ID=ID, form=request.form)

        else:
            system.add_to_order(burger, int(ID))
            return render_template('item_confirm.html', item="Custom Burger", ID=ID)

    return render_template('burger.html', items=items, ID=ID)

@app.route('/selection/<main>/<ID>', methods = ['GET', 'POST'])
def selection(ID, main):

    if (request.method == 'POST'):

        if (request.form["type"] == "Custom Burger"):
            return redirect(url_for("burger", ID=ID, main=main))

        elif (request.form["type"] == "Custom Wrap"):
            return redirect(url_for("wrap", ID=ID, main=main))

        elif (request.form["type"] == "Python2 Burger"):
            burger = DoubleBurger()

            burger.add_ingredient("Beef patty", 2)
            burger.add_ingredient("Cheddar cheese", 2)
            burger.add_ingredient("BBQ sauce", 2)
            burger.add_ingredient("Muffin bun", 3)

            if (system.get_order(int(ID)) == None):
                system.new_order(int(ID))

            system.add_to_order(burger, int(ID))

            return render_template('item_confirm.html', item="Python2 Burger", ID=ID)

        elif (request.form["type"] == "Python3 Burger"):
            burger = TripleBurger()

            burger.add_ingredient("Beef patty", 3)
            burger.add_ingredient("Cheddar cheese", 3)
            burger.add_ingredient("BBQ sauce", 3)
            burger.add_ingredient("Sesame bun", 4)

            if (system.get_order(int(ID)) == None):
                system.new_order(int(ID))

            system.add_to_order(burger, int(ID))

            return render_template("item_confirm.html", item="Python3 Burger", ID=ID)

        elif (request.form["type"] == "George's Burger"):
            burger = DoubleBurger()

            burger.add_ingredient("Beef patty", 1)
            burger.add_ingredient("Chicken patty", 1)
            burger.add_ingredient("Swiss cheese", 2)
            burger.add_ingredient("Sesame bun", 3)
            burger.add_ingredient("Onions", 3)
            burger.add_ingredient("Tomato sauce", 2)
            burger.add_ingredient("Lettuce", 2)

            if (system.get_order(int(ID)) == None):
                system.new_order(int(ID))

            system.add_to_order(burger, int(ID))

            return render_template("item_confirm.html", item="George's Burger", ID=ID)

        elif (request.form["type"] == "Beef Wrap"):
            wrap = Wrap()


            wrap.add_ingredient("Beef patty", 1)
            wrap.add_ingredient("Lettuce", 3)
            wrap.add_ingredient("Onions", 3)
            wrap.add_ingredient("Tomatoes", 3)
            wrap.add_ingredient("BBQ sauce", 1)

            if (system.get_order(int(ID)) == None):
                system.new_order(int(ID))

            system.add_to_order(wrap, int(ID))

            return render_template("item_confirm.html", item="Beef Wrap", ID=ID)

        elif (request.form["type"] == "Chicken Wrap"):
            wrap = Wrap()


            wrap.add_ingredient("Chicken patty", 1)
            wrap.add_ingredient("Lettuce", 3)
            wrap.add_ingredient("Onions", 3)
            wrap.add_ingredient("Tomatoes", 3)
            wrap.add_ingredient("BBQ sauce", 1)

            if (system.get_order(int(ID)) == None):
                system.new_order(int(ID))

            system.add_to_order(wrap, int(ID))

            return render_template("item_confirm.html", item="Chicken Wrap", ID=ID)

        elif (request.form["type"] == "Vegetarian Wrap"):
            wrap = Wrap()


            wrap.add_ingredient("Vegetarian patty", 1)
            wrap.add_ingredient("Lettuce", 3)
            wrap.add_ingredient("Onions", 3)
            wrap.add_ingredient("Tomatoes", 3)
            wrap.add_ingredient("BBQ sauce", 1)

            if (system.get_order(int(ID)) == None):
                system.new_order(int(ID))

            system.add_to_order(wrap, int(ID))


        return render_template("item_confirm.html", item="Vegetarian Wrap", ID=ID)

    return render_template('selection.html', ID=ID, main=main)


@app.route('/wraps/custom/<ID>', methods=['GET', 'POST'])
def wrap(ID):
    items = system.get_main_list()

    if (request.method == 'POST'):

        if (system.get_order(int(ID)) == None):
            system.new_order(int(ID))

        wrap = Wrap()

        for ingredient in items:
            if ("bun" not in ingredient):
                if (int(request.form[ingredient]) != 0):
                    wrap.add_ingredient(ingredient, int(request.form[ingredient]))


        if (wrap.is_valid_main() == False):
            errors = wrap.get_errors()
            return render_template('wrap.html', items=items, errors=errors, ID=ID, form=request.form)

        else:
            system.add_to_order(wrap, int(ID))
            return render_template('item_confirm.html', item="Custom Wrap", ID=ID)

    return render_template('wrap.html', items=items, ID=ID)

@app.route('/side/<ID>', methods=["GET","POST"])
def sides(ID):
    sidelist = system.get_sidelist()

    if request.method == "POST":

        if (system.get_order(int(ID)) == None):
            system.new_order(int(ID))

        for side in sidelist:
            for i in range(int(request.form[side])):
                system.add_to_order(Side(side), int(ID))


        return render_template('item_confirm.html', item="Sides", ID=ID)

    return render_template('sides.html',sidelist=sidelist, ID=ID)



@app.route('/drink/<ID>', methods=["GET","POST"])
def drinks(ID):
    drinklist = system.get_drinklist()

    if request.method == 'POST':

        if (system.get_order(int(ID)) == None):
            system.new_order(int(ID))

        for drink in drinklist:
            for i in range(int(request.form[drink])):
                system.add_to_order(Drink(drink),int(ID))

        return render_template('item_confirm.html', item="Drinks", ID = ID)

    return render_template('drinks.html',drinklist = drinklist, ID=ID)


@app.route('/order/<ID>', methods = ['GET','POST'])
def order(ID):
	customer_order = system.get_order(int(ID))
	if customer_order is None:
		return redirect(url_for('error', ID = ID))

	mains = []
	sides = {}
	drinks = {}
	main_type = []
	order_items = customer_order.get_order_list()
	total_price = customer_order.total_price()

	for item in order_items:
		if (isinstance(item,Drink)):
			if (item.get_name() in drinks):
				drinks[item.get_name()] += 1
			else:
				drinks[item.get_name()] = 1
		elif (isinstance(item,Side)):
			if (item.get_name() in sides):
				sides[item.get_name()] += 1
			else:
				sides[item.get_name()] = 1
		else:
			mains.append(item.get_ingredients())
			main_type.append(item.type_main())

	if (request.method == 'POST'):
		try:
			success, customer_ID = system.confirm_order(customer_order)

		except OrderError as err:
			success = err.get_message()

		if success != True:
			return render_template('order.html', ID = ID, mains = mains, main_type = main_type,
				sides = sides, drinks = drinks, price = total_price, errors = success)
		else:
			return render_template('order_confirmed.html', ID = ID)

	return render_template('order.html', ID = ID, mains = mains, main_type = main_type,
		sides = sides, drinks = drinks, price = total_price)


@app.route('/status/<ID>', methods = ["GET","POST"])
def status_enter(ID):
	if request.method == 'POST':
		check_id = request.form['ID']
		return redirect(url_for('status', ID = ID, id = check_id))
	else:
		return render_template('order_input.html', ID = ID)


@app.route('/status/<ID>/<id>', methods = ['GET','POST'])
def status(ID,id):
	try:
		status = system.check_status(int(id))

	except InvalidID as err:
		order_is_ready = err.get_message()
		return render_template('check_order.html',ID = ID, id = id, ready = order_is_ready)

	order = system.get_order(int(id))
	if order is None:
		order = system.get_completed_order(int(id))

	if (order.get_confirmed() == False):
		order_is_ready = 'No order exists for ID of ' + id
	elif (system.check_status(int(id)) == True):
		order_is_ready = True
	else:
		order_is_ready = False

	return render_template('check_order.html',ID = ID, id = id, ready = order_is_ready)


@app.route('/error/<ID>')
def error(ID):
    return render_template('error.html', ID = ID)

@app.route('/staff')
def staff():
    return render_template('staff.html')


@app.route('/staff/orders',methods = ['GET','POST'])
def staff_orders():
    orders = system.get_orders()
    confirmed_orders = []

    for order in orders:
        if (order.get_confirmed()):
            confirmed_orders.append(order)


    if request.method == "POST":
        if "Complete" in request.form:
            c_order_id = request.form.get("Order")
            if c_order_id == None:

                return render_template('staff_orders.html', orders= confirmed_orders)

            system.update_status(int(c_order_id))

            for order in confirmed_orders:
                if (order.get_ID() == int(c_order_id)):
                    confirmed_orders.remove(order)
                                
            return render_template('staff_orders.html', orders= confirmed_orders)

    return render_template('staff_orders.html',orders = confirmed_orders)


@app.route('/staff/stock', methods = ['GET','POST'])
def staff_stocks():
    stocks = system.get_stock().get_stock()
    if request.method == "POST":
        for key in stocks:
            system.get_stock().update_item(key,int(request.form[key]))
        return render_template('staff_stocks.html',stocks=stocks)

    return render_template('staff_stocks.html',stocks=stocks)
