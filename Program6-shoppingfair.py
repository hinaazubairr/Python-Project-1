# Program # 6: shoppingfair.py
# Project: shopping for science fair supplies

# Alex has $25 to complete her experiment.
# The price of each item is: Flowerpot = $4, Pack of flower seeds=$1, Bag of soil = $5
# Plus 6% sales tax which is 0.06 added to the items in Alex's shopping cart.

# Cost of each shopping item
Flowerpot_price = 4.00 
Flower_seeds_price=1.00 
soil_price = 5.00

#sales tax
sales_tax = 0.06

#Ask the user to provide the quantity of the shopping items
Flowerpot = int(input("How many flower pots:?"))
Flower_seeds = int(input("How many flower seeds:?"))
soil = int(input("How many bags of soil:?"))

#calculae the cost of items
cost_of_items = ((Flowerpot*Flowerpot_price)+(Flower_seeds*Flower_seeds_price)+(soil*soil_price))

# calculate the cost of items plus tax
total_cost = cost_of_items + (cost_of_items*sales_tax)

print(total_cost)