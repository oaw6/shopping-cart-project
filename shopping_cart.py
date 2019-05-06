# shopping_cart.py
import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#Variable set-up section
cart_product = 0
product_list = []
#product_list = [2, 12, 6, 16, 6] Test List
final_list = []
pretax_total = 0.00

#Introduction to Program
print("Welcome to the Bag-It-Up Grocery check-out interface. Please follow the directions below:")
print("-----------------------------------------------------------------------------------------")

#User inputs id numbers for products in their shopping cart
while cart_product != "null":
    cart_product = input("Please type the item identification number of one of your products. After you have finished, type 'DONE': ")
    if cart_product == "DONE":
        print("Thank you! Your receipt will appear below.")
        break
    product_list.append(int(cart_product))
print("The items in your cart have the following identification numbers:", product_list)

#Product Lookup Loop
for product_id in product_list:
    product_id_match = [product for product in products if product["id"] == product_id]
    if product_id_match != []:
        final_list.append(product_id_match)

#Convert float values to USD format
def to_usd(price_float):
    return "$" + str("%0.2f" % price_float)

#Receipt Creation and Calculations
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("Owen's Bag-It-Up Grocery")
print("-------------------------------------------------------")
print("Website: http://www.bagitup.com")
print("Phone: 202-555-1789")
print("Date and Time of Purchase:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("-------------------------------------------------------")
print("Items Purchased:")
for purchased_product in final_list:
    #print("+  " + str(purchased_product[0]["name"]) + "..... $" + str("%0.2f" % purchased_product[0]["price"]))
    print("+  " + str(purchased_product[0]["name"]) + "..... " + to_usd(purchased_product[0]["price"]))
    pretax_total = pretax_total + purchased_product[0]["price"]
print("-------------------------------------------------------")
#print("Cart Subtotal..... $" + str("%0.2f" % pretax_total))
print("Cart Subtotal..... " + to_usd(pretax_total))
taxes = pretax_total * 0.08875                                  #Tax Calculation
#print("+  Sales Tax (8.875%)..... $" + str("%0.2f" % taxes))
print("+  Sales Tax (8.875%)..... " + to_usd(taxes))
final_total = pretax_total + taxes                              #Total Calculation
#print("Total..... $" + str("%0.2f" % final_total))
print("Total..... " + to_usd(final_total))
print("-------------------------------------------------------")
print("Thank you for shopping with us!")
print("-------------------------------------------------------")
print("-------------------------------------------------------")
print("-------------------------------------------------------")