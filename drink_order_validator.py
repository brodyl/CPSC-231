'''
Author: Brody Wells
UCID:   xxxxxxxx
Date:   Sept 26, 2024

Example Exercise - Drink order validator

Demonstrates how you can use dictionarys to convert users input to in values to make comparisons easier.

Simple system to ask user for two drink orders, then validates the inputs and determines which order is larger
'''

# Function to validate the users input for the size of their drink order
def validate_order_input(str):
    valid_sizes = ["Small", "Medium", "Large"]

    # Checking if the input is in the allowed list of inputs
    if str not in valid_sizes:
        print("That's not a valid size.")
        exit()


# Prompt for the users first order
order_1_input = input("What size of drink for the first order? [Small, Medium, or Large] ")
# Validate their input
validate_order_input(order_1_input)

# Prompt for the users second order
order_2_input = input("What size of drink for the second order? [Small, Medium, or Large] ")
# Validate their input
validate_order_input(order_2_input)

# Dictionary to map month name to month number
order_size_numbers = {
    "Small":2, "Medium":5, "Large":10
}

# Convert the string inputs to an int value using our dictionsry
order_1_size = order_size_numbers[order_1_input]
order_2_size = order_size_numbers[order_2_input]

# Output which order is larger
if order_1_size == order_2_size:
    print("The orders are the same size")
elif order_1_size > order_2_size:
    print("Order one is larger than order two")
else:
    print("Order two is larger than order one")

# Demonstrate how we can pad an int value with leading zeros
# '02' means pad the integer to a size of 2 characters, and use 0's as the padding character.
print(f"order one has a size of: {order_1_size:01}")
print(f"order one has a size of: {order_1_size:02}")
print(f"order one has a size of: {order_1_size:03}")
print(f"order one has a size of: {order_1_size:-4}")



