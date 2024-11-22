import math

user_input = input("Give me a number: ")

try:
    number = float(user_input)
    rounded_number = math.ceil(number)
    print(rounded_number)
except ValueError:
    print("That's not a valid number!")
