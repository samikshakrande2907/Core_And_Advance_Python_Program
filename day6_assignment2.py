# Write a python program to check whether a number is palindrome or not?
# Define the function to check if a number is a palindrome
def is_palindrome(num):
    original_num = num  # Store the original number
    reversed_num = 0  # Initialize the variable to store the reversed number
    
    while num > 0:
        # Get the last digit of the number
        digit = num % 10
        # Add the digit to the reversed number
        reversed_num = reversed_num * 10 + digit
        # Remove the last digit from the original number
        num = num // 10
    
    # Check if the original number is equal to the reversed number
    if original_num == reversed_num:
        return True  # It's a palindrome
    else:
        return False  # It's not a palindrome

# Call the function with a number
number = 121
result = is_palindrome(number)

# Display the result
if result:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


'''output
121 is a palindrome.'''

