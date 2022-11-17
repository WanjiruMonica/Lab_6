# A program that reads item prices from the user
# Asks the user for the budget
# Sums up prices of the items and stops when total exceeds the budget.


def budget():
    total_money = int(input("Welcome! What is your budget for today? "))
    total_price = 0
    
    while total_price < total_money:
        print(f"Your total is {total_price}")
        print()
        item_name,item_price = input("Item: "), int(input("Price: "))
        total_price = total_price + item_price
        
    print("You have exceeded your budget!") # will print when the condition of the loop is not met.

budget()
        
