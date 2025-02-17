#Python Program to Find the Largest Among Three Numbers
# Declare three numbers
num1 = 10
num2 = 25
num3 = 15

# Use an if-elif-else condition to find the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the largest number
print("The largest number among", num1, ",", num2, "and", num3, "is:", largest)

#output

"The largest number among 10 , 25 and 15 is: 25"

