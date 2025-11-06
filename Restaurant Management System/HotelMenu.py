# Defining the menu of restaurant.

menu = {
    'Burger' : 250,
    'Pizza' : 350,
    'Noodles': 150,
    'Ice Cream' : 150,
    'Pasta' : 200,
    'Coffee' : 220,
    'Salad' : 140
}

#Greeting
print("Welcome to python restaurant!")
print("Our Menu list -")
print("Burger = 250 tk\nPizza = 350 tk\nNoodles = 150 tk\nIce Cream = 150 tk\nPasta = 200 tk\nCoffee = 220 tk\nSalad = 140 tk")
print("------------------------------------")

# Prices of orders.
TotalOrder = 0

# Entering the orders

item_1 = input("Enter the item you want to order - ")

if item_1 in menu:
    TotalOrder += menu[item_1]
    print(f"Your item {item_1} is added to the cart.")

else:
    print(f"Your item {item_1} is not available in our restaurant\nPlease order something else!")

print("------------------------------------")

another_order = input("Do you want to add another item ? (Yes/No)\n")

if another_order == "Yes" :
    item_2 = input("Enter the name of another order - ")

    if item_2 in menu:
        TotalOrder += menu[item_2]
        print(f"Your item {item_2} is added to the cart.")
        
    else:
        print(f"Your item {item_2} is not available in our restaurant\nPlease order something else!")

print("------------------------------------")

# Showing the total pay for order
print(f"Your bill is to pay --- {TotalOrder}")
print("------------------------------------")

print("Thank you for ordering from Python Restaurant! Have a great day! 😋")

