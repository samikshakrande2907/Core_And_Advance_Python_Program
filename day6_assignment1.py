#. Write a python program to reverse a number using a while loop.
# Define the reverse_number function
def reverse_number(num):
    reversed_num = 0  # Initialize the variable to store the reversed number
    while num > 0:
        # Get the last digit of the number
        digit = num % 10
        # Add the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the original number
        num = num // 10
    return reversed_num

# Call the function with a number
result = reverse_number(12345)

# Display the reversed number
print("The reversed number is:", result)

'''output
The reversed number is: 54321'''
