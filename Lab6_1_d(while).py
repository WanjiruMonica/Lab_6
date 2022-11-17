# A program that increments by 2 value given by user
# Upto an endpoint specified by user
# Then sums the values
# Using while loop.

def main():
    num_1 = int(input("Enter the first value: "))
    num_2 = int(input("Enter the last value: "))
    sum_of_numbers = 0
    
    while num_1 <= num_2:
        sum_of_numbers = sum_of_numbers + num_1
        num_1 = num_1 + 2
    print(f"The sum of the numbers is {sum_of_numbers}")
        

main()
