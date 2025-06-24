#Chad Collard
#Chapter 3 Lab 2
#6/22/25

print ("\t\t\t\tJane's Stuff Store")


items = int(input ("please enter which items you would like to purchase (1-3): "))


total = 0
for i in range(items):
    print(f"enter the price of item {i+1}:",end=" ")
    price = float(input())
    total += price
average=total/items    


print(f"The total cost of your items is {total}")
print(f"The average cost of each item is {average}")

    
    
