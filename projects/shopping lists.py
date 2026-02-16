print("Welcome to Amazon Shopping Complex")
print("--------------------------------------")

cart = {}
total_price = 0

num = int(input("Enter the quantity of items: "))

# Adding items
for i in range(num):
    item = input("Enter your item: ")
    price = int(input("Enter the price: "))
    cart[item] = price
    total_price += price

print("\nYour cart items are:", cart)

# Removing items
remove = input("\nDo you want to remove any item? (y/n): ")

if remove.lower() == 'y':
    remove_item = input("Enter item to remove: ")

    if remove_item in cart:
        total_price -= cart[remove_item]
        del cart[remove_item]
        print(remove_item, "removed successfully ✅")
    else:
        print("Item not found in cart ❌")

print("-----------------------------------------")

# Final Cart Display
print("\nFinal Items in Cart:")
for item, price in cart.items():
    print(f"{item} → ₹{price}")

print("\nTotal Bill =", total_price)

print("\nVisit again 😊")
