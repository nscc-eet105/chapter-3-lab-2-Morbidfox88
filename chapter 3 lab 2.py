#Chad Collard
#Chapter 3 Lab 2
#6/22/25

print ("                       Jane's Stuff Store")


items = int(input ("please enter which items you would like to purchase (1-3): "))


if items == 1:
    print("Item 1 = 1.50")
elif items == 2:
    print("Item 2 = 3.45")
elif items == 3:
    print("Item 3 = 2.00")
else:
    print("please make another selection")

total = 0
for items in range(1, items):
    print(items)
    total += items

print(f"The total is {total}.")
    
    
