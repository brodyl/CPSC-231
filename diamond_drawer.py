'''
 Diamond Drawer

 This exercise expects you to draw a diamond shape to the console based on the user input value for edge length
'''

# Ask the user for the edge length
edge_length = int(input("Please enter the edge length for the diamond: "))

row_index = 1    #  n is the current row, which starts at row 1

# First output the right side up triangle
# Loop through each row and print an increasing number of stars (asterix)
#    Each line will be padded with a decreasing number of spaces, in order to align the triangle
while row_index <= edge_length:
    # For each row print correct amount of spaces for padding
    print(" " * (edge_length - row_index), end="")
                                      # if user types 5 for rows:
                                      # row 1 has (5-1) spaces;
                                      # row 2 has (5-2) space;
                                      # row n has (rows-n) spaces

    # For each row print correct number of stars
    print("*" * (row_index * 2 - 1))  # row 1 has 1 star;
                                      # row 2 has 3 stars;
                                      # row n has (n * 2 - 1) stars

    # Increment the while loop counter and repeat
    row_index = row_index + 1


# For the second loop (smaller upside down triangle) we could do the same process but in reverse.
# In this case our upside down triangle will be 1 row smaller,
#   and spaces for padding will increase as number of starts decreases

# Set our row_index to start at max value in this case
row_index = edge_length - 1

# Loop through each row and print an increasing number of stars (asterix)
#    Each line will be padded with a decreasing number of spaces, in order to align the triangle
while row_index >= 1:
    # For each row print correct amount of spaces for padding
    print(" " * (edge_length - row_index), end="")
                                      # if user types 5 for rows:
                                      # row 1 has (5-1) spaces;
                                      # row 2 has (5-2) space;
                                      # row n has (rows-n) spaces

    # For each row print correct number of stars
    print("*" * (row_index * 2 - 1))  # row 1 has 1 star;
                                      # row 2 has 3 stars;
                                      # row n has (n * 2 - 1) stars

    # Decrement the while loop counter and repeat
    row_index = row_index - 1
