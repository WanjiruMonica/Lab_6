# A program that divides 1.0 by 2 using while loop till it becomes 0.0
# The program also counts how many times the division takes place.

def main():
    x = 1.0
    count = 0

    while x > 0.0: # Using x>0 or x!=0 yields same results as x>0.0
        print(f"{x} divided by 2 is: ",end=' ') # This ensures the first value printed is the original value.
        x = (x/2)
        count = count + 1 # counts how many times 1.0 will be divided to get to 0.0
        print(x)
        
    print(f"The original value has been divided by 2, {count} times")


main()
