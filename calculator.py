#Python program for calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    print("\n===== Calculator =====\n")
    first_num = int(input("Enter the First Number: "))
    second_num = int(input("Enter the Second Number: "))

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        result = add(first_num, second_num)
        print(f"\nAddition of {first_num} and {second_num} is: {result}")
    elif choice == 2:
        result = subtract(first_num, second_num)
        print(f"\nSubtraction of {second_num} from {first_num} is: {result}")
    elif choice == 3:
        result = multiply(first_num, second_num)
        print(f"\nMultiplication of {first_num} and {second_num} is: {result}")
    elif choice == 4:
        result = divide(first_num, second_num)
        print(f"\nDivison of {first_num} from {second_num} is: {result}")
    elif choice == 5:
        print("\n Exiting from calculator.")
        break
    else:
        print("\n Please enter the valid choice.")
