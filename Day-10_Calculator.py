# Day 10 Project Calculator

# Addition
def add(n1, n2):
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


# Operations

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    num1 = float(input("What's the first number?: "))

    for operator in operations:
        print(operator)

    keep_going = True

    while keep_going:

        symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculation_symbol = operations[symbol]
        answer = calculation_symbol(num1, num2)
        print(f"Your current result is : {answer}")
        continue_calculation = input(f"Do you want to continue calculating on {answer} type 'y' for yes 'n' for no:\n")

        if continue_calculation == 'n':
            start_again = input("Do you want to start again with new numbers? Type y or n\n")
            if start_again == 'y':
                calculator()
            else:
                keep_going = False
        else:
            num1 = answer


calculator()
