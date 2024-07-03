def add(num1, num2):
    return num1 + num2
 
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
 
def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error! Division by zero!"

def get_numeric_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")

select = None
while select not in [1, 2, 3, 4]:
    select = int(input("Select operations from 1, 2, 3, 4: "))
    if select not in [1, 2, 3, 4]:
        print("Invalid selection! Please choose from 1, 2, 3, 4.")

number_1 = get_numeric_input("Enter first number: ")
number_2 = get_numeric_input("Enter second number: ")

if select == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif select == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif select == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif select == 4:
    print(number_1, "/", number_2, "=", divide(number_1, number_2))