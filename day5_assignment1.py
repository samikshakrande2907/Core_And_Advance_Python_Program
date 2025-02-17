#Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
# Define the div() function with two parameters
def div(num1, num2):
    # Perform the division and return the result
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

# Call the function with two numbers
result = div(10, 2)

# Display the result
print("The result of the division is:", result)

'''output
The result of the division is: 5.0'''
