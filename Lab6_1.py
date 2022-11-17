# A program that finds sum of numbers from 1 to 100 using for loop

def main():
    sum_of_numbers = 0
    a = int(input("Enter value to be the first number in summtion: "))
    b = int(input("Enter value to be the last number in summation: "))
    
    for i in range(a,b+1):
        sum_of_numbers = sum_of_numbers + i

    print(f"The sum of numbers from {a} to {b} is {sum_of_numbers}")

main()
