# Defining a list of weekdays
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Asking the user for the day number
day_number = int(input("Enter the day number: "))

# Finding the corresponding day name using modulo operation
day_name = weekdays[day_number % 7]

# Printing the day name With  2 conditions
if day_number >= 0:
    print(f"The day name for day number {day_number} is {day_name}.")
    
else:
    print("Input Error! The Day Number must be positive! Try Again!")

    

