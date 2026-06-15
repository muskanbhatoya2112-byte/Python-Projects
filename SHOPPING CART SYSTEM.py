# Shopping Cart System

cart = []          # List
categories = set() # Set
prices = {}        # Dictionary


n = int(input("How many items? "))

for i in range(n):
    item = input("Item name: ")
    price = int(input("Price: "))
    category = input("Category: ")

    cart.append(item)
    prices[item] = price
    categories.add(category)


remove_item = input("Enter item to remove: ")
if remove_item in cart:
    cart.remove(remove_item)
    del prices[remove_item]


print("Cart Items:", cart)
print("Categories:", categories)
print("Prices:", prices)


print("Total Bill =", sum(prices.values()))