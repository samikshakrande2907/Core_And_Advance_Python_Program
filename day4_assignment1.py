# Get the year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year using the leap year rule
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")

'''output
 " Enter a year: 2024"
2024 is a Leap Year.
"Enter a year: 2023"
2023 is not a Leap Year'''
