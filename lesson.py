# Write a function that converts celcius to fehrenheit. convert_celcius_2_fahrenheit


def convert_celcius_2_fahrenheit(c):
    return ((c * 9) / 5) + 32


c = float(
    input("Enter the temperature in celcius: ")
)  # Ask for the temperature in celcius:
f = convert_celcius_2_fahrenheit(c)
print("The temperature in fahrenheit is: ", f)
