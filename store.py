# Programmer : Alexander Walker
# Description : This program asks the user to enter the amount of items their buying and the price. It then gives
#back the subtotal, tax, and total of all the products purchased.

#Counters to keep track of info and number of items.
counter = 0
item_num = 1
subtotal = 0

#User inputs how many items their buying here.
items = int(input("How many items are you purchasing? "))

#While the counter is less then items, it will keep asking for the price of each item.
while (counter < items):
    price = input(f"Enter item {item_num} price: ")
    
    #Adds points to the counters.
    subtotal = price + subtotal
    item_num += 1
    counter += 1

#Finds the tax and total.
tax = subtotal * 0.13
total = tax + subtotal

#Prints out the tax and total.
print(f"\nSubtotal: ${subtotal:,.2f}")
print(f"Tax: ${tax:,.2f}")
print(f"Total: ${total:,.2f}")
    

