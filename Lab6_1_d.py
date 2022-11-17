# A program that increments by 2 a value entered by user upto an endpoint defined by user and sums the numbers.

def main():
    num_1 = int(input("Enter the first value: "))
    num_2 = int(input("Enter the last value: "))
    sum_of_numbers = 0

    for numbers in range(num_1, num_2 + 1, 2): # The value 2 makes the increments. # num_2 + 1 ensures if start is an even number, the last value is also included.
        #print(numbers)
        sum_of_numbers = sum_of_numbers + numbers
    print(f"Sum of the numbers is {sum_of_numbers}")

main()
