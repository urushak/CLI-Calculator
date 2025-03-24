# Function to multiply two numbers
def multiply_numbers(num1, num2):
    return num1 * num2

# Taking input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calling the function and storing the result
result = multiply_numbers(number1, number2)

# Displaying the result
print(f"The product of {number1} and {number2} is {result}")
