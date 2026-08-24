#create a shopping cart program
items = input("enter the items you want to buy: ")
price = float(input("enter the price of the items: "))
quantity = int(input("enter the quantity of the items: "))
total_price = price * quantity
print(f"the total price of {quantity} {items} is {total_price}")