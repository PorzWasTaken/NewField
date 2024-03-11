def calculator():
    first_number = float(input("Enter the first number "))
    operation = input("Enter the operation ")
    second_number = float(input("Enter the second number "))
    

    if operation == "+":
        print(first_number + second_number)

    elif operation == "-":
        print(first_number - second_number)

    elif operation == "*":
        print(first_number * second_number)

    elif operation == "/":
        if second_number != 0:
            print(first_number / second_number)
        else:
            print("Error: Diversion by zero")

calculator()
