# Gourmet-Super-Fresh
A website for a fictional Burger Joint to receive and handle online orders. 

To run the website on your local machine, please navigate to the FrontEnd directory and run "python run.py" using your command line.  

Details regarding the assignment are shown below. 

# Background

Your consultancy firm has been called in to Australia’s largest burger food chain GourmetBurgers for a new software project.   The client is interested in developing an online self-service ordering application.    The client feels that such a system would provide faster delivery of meals to customers, enable customers to build their own gourmet creations which would result in improving the revenue at the different franchises of the food chain.

# Preliminary Requirements

The online application offers three types of services:

 1. Customers - Place Online Orders
 2. Staff - Service Online Orders
 3. Staff  - Maintain Inventory

### 1. Customer - Online Orders

**Mains**
At any GourmetBurger outlet, a customer can create two types of mains, a burger or a wrap and order their gourmet creation.  For each selected main, a customer can choose:

1. type and number of buns (e.g., 3 sesame buns for a double burger or 2 muffin buns for a standard single burger) - the number of buns cannot exceed the maximum allowable     limit (e.g., if only single, double and triple burgers are permitted, then the customer cannot choose more than 4 buns)
3. type and number of patties (e.g., 2 chicken patties, vegetarian, beef). here again, customers are restricted to the maximum allowable patties
 4. other ingredients of their choice such as tomato, lettuce, tomato sauce, cheddar cheese, swiss cheese etc.
Each of the mains (burger or wrap) has a base price, and each ingredient carries an additional price, so once a customer has completed their gourmet creation, the net price of their created main will be calculated based on the chosen ingredients and displayed to the customer.

**Sides and Drinks**
Besides the main, a customer can (optionally) order sides (e.g., a 6 pack nuggets, 3 pack nuggets, fries (small, medium, large)) and drink(s) of their choice.

Once, a customer has completed their selection (main, side and drink), they can checkout to complete their order. At this point, they will be issued with an order-id.  At any point in time, the customer should be able to check if their order is ready to be collected using their order-id.  The customer can check the status of their order at any point to see if their order is completed.

### 2. Staff - Service Orders

The staff can view the current orders at any point in time.  Once a customer's order has been cooked, they will update the status of the order to indicate that the order is available for pickup by the customer.  The customer should be able to see this change in status at their end when they refresh their page. This order will now disappear from staff orders menu.

### 3. Staff - Maintain Inventory
Staff will also be responsible for maintaining the inventory of their various ingredients.   Periodically, they will refill their stock.  As a customer places an order (e.g. a double burger with 2 chicken patties and cheddar cheese) will result in the inventory levels being decremented accordingly.  At any point in time, if a particular ingredient is not available, the customer will not be able to select the particular item to their order.
Burgers, wraps, nuggets are all stocked in whole quantities.
Bottled drinks are stocked in either cans (375 ml) or bottles (600 ml) and drinks such as orange juice will be served in varying sizes (e.g., a small = 250 ml, a medium = 450 ml etc).
Sides such as fries will need to be stocked by weight (in gms). For example, a small fries = 75g, a medium fries = 125 g and if a customer orders a medium fries, this would reduce the inventory levels by 125g.

## Implementation Guidelines

-   Keeping mind that an Agile Software Development style has been chosen for this project, your team will be required to build and deliver the project in iterations. Each iteration will deliver a part of the requirements of the project during which the team members are expected to carry out all the SDLC activities, namely analysis, design, coding and testing. At the end of the iteration, you (as a team) will demonstrate to your lab class the functionality implemented during that iteration cycle. Your team must bear in mind that project requirements may be subject to change and enhancements to functionalities may be made at the end of the iteration. You will need to carefully design the solution for your current iteration, such that the solution is extensible to accommodate these changes. Deliverable for each iteration will be outlined at the start of each iteration cycle.

-   For this project, no sophisticated authentication is required to be implemented. When the URL of the online app  is specified, e.g.,  [http://localhost:8080/],  this should launch a dashboard that prompts the user to order a mains, side or drink

-   Any kind of persistence mechanism may be used (e.g., Python’s  **pickle**) to store the inventory items

-   This project must be designed using  **object-oriented design**  principles and implemented using  **Python/Flask/Jinja2**. It is recommended that students build their front-end using HTML and CSS only. No other CSS frameworks (e.g. Material CSS, Bootstrap, etc.) to be used for building the UI of the application.

-   What has been provided to you is a problem statement; a set of high-level requirements from the customer. Your team must analyse the problem statement and go through a process of eliciting more formal requirements to develop the final set of user-stories and acceptance tests.   You will need to have a visioning exercise with your customer, to determine the complete range of burgers/wraps and ingredients available for selection to the customer along with any additional constraints to orders.This must be elicited as part of your requirements analysis.

-   The model solution demonstrated in the lectures was only a guide to demonstrate “one” possible way of implementing the customer’s requirements. You are required to design your solution and present in week 10.

-   At the end of each deliverable (weeks 4, 7, & 10) tutors will check the team’s GitHub repositories to ensure that all members of the team have contributed equally to the project and appropriate branches are created by each team member.  There will additionally be an anonymous peer assessment among team members at the week end, where each team member has the opportunity to rate other team members for their contribution to the group project.
