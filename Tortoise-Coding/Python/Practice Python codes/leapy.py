# Python program to check if a year is a leap year
try:
    year = int(input("Enter a year: "))

    # Check for leap year
    # Century year (divisible by 100 and 400 is a leap year)
    if (year % 400 == 0):
        print("{0} is a leap year".format(year))
    # Non-century year divisible by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))
    # If not satisfying any leap year conditions
    else:
        print("{0} is not a leap year".format(year))
except ValueError:
    print("Invalid input. Please enter a valid year.")

