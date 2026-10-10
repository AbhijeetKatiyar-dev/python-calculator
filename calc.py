#Basic calculator program in Python
def cal_sum(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return None
    return a / b


while True:
    print("\n<----- Calculator ----->")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 5:
        print("You have exited the calculator.")
        break

    if choice not in [1, 2, 3, 4]:
        print("Wrong input. Choose between 1 and 5.")
        continue

    try:
        a = float(input("Enter your first number: "))
        b = float(input("Enter your second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == 1:
        print("Result:", cal_sum(a, b))
    elif choice == 2:
        print("Result:", subtract(a, b))
    elif choice == 3:
        print("Result:", multiplication(a, b))
    elif choice == 4:
        result = division(a, b)
        if result is None:
            print("Error: Cannot divide by zero.")
        else:
            print("Result:", result)
