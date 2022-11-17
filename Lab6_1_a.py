# A program that finds sum of numbers from 1 to 100 using while loop

def main():
    sum_of_numbers = 0
    num = int(input("Enter a value to be the first number in summation: "))
    num_2 = int(input("Enter a value to be the last number in summation: "))
    print(f"The sum of numbers from {num}",end=' ')  # this print statement has been placed here so that the value of num printed is the original value.
          
    while num <= num_2:
        sum_of_numbers = sum_of_numbers + num
        num = num + 1
    print(f"to {num_2} is {sum_of_numbers}")

main()

    
