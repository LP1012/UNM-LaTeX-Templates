# Define a function to calculate the square of a number
def square(number):
    return number ** 2

# Input: Get a number from the user
try:
    num = float(input("Enter a number: "))
    result = square(num)
    print(f"The square of {num} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")

