def add(a, b):
    result = a + b
    return result

def subtract(a, b):
    result = a - b
    return result

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Select an operation (+ or -): ")

if operation == "+":
    result = add(num1, num2)
    print(f"The sum of {num1} and {num2} is equal to {result}")
elif operation == "-":
    result = subtract(num1, num2)
    print(f"The subtraction of {num1} and {num2} is equal to {result}")
else:
    print("Invalid operation")
