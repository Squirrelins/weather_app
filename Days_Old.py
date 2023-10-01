# Ask for input of persons perday as Month, Day, Year then calculate the age in days to today.
# Then print the age in days to the screen.

# Import the datetime module
import datetime as dt

# Ask for input of persons perday as Month, Day, Year
print("Please enter your birthdate as Month, Day, Year using numbers only.")
print("For example: 1, 1, 2000 for January 1st, 2000")
month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Year: "))

# Ask for confrimation of birthdate
print("Your birthdate is", month, "/", day, "/", year)
confirm = input("Is this correct? (Y/N): ")
if confirm == "Y" or confirm == "y":
    print("Thank you")
else: 
    print("Please restart the program and enter your birthdate again.")
    exit()
    

# Calculate the age in days to today
birthdate = dt.date(year, month, day)
today = dt.date.today()
age = today - birthdate
age_days = age.days

# Print the age in days to the screen
print("Your birthdate is", birthdate, "which makes you", age_days, "days old")

# Do you want to know months old?
months_old = age_days / 30.4375
print("You are", months_old, "months old")

# Do you want to know years old?
years_old = age_days / 365.25
print("You are", years_old, "years old")

# Do you want to know hours old?
hours_old = age_days * 24
print("You are", hours_old, "hours old")

# Do you want to know minutes old?
minutes_old = hours_old * 60
print("You are", minutes_old, "minutes old")

# Do you want to know seconds old?
seconds_old = minutes_old * 60
print("You are", seconds_old, "seconds old")

# Do you want to know milliseconds old?
milliseconds_old = seconds_old * 1000
print("You are", milliseconds_old, "milliseconds old")

# End of program