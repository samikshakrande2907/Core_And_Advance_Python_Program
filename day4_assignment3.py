#Python Program to Check if a Number is Positive, Negative or zero
# Get the number from the user
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print(num, "is a Positive number.")
elif num < 0:
    print(num, "is a Negative number.")
else:
    print(num, "is Zero.")

'''output 
   Enter a number: 15
15.0 is a Positive number.
Enter a number: -20
-20.0 is a Negative number.'''

