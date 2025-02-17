# Write a python program finding the factorial of a given number using a while loop.
# Define the function to calculate the factorial
def factorial(num):
    result = 1  # Initialize result to 1 (since factorial of 0 and 1 is 1)
    
    # Check if the number is non-negative
    if num < 0:
        return "Factorial does not exist for negative numbers"
    
    # Use a while loop to multiply the result by each number from num down to 1
    while num > 1:
        result *= num
        num -= 1  # Decrease the number by 1 at each iteration
    
    return result

# Call the function with a number
number = 5
result = factorial(number)

# Display the result
print(f"The factorial of {number} is: {result}")


'''output
The factorial of 5 is: 120'''
