
'''
Example script which will 
(1) Open a text file
(2) Encrypt the contents using the ROT13 Cipher
(3) Overwrite the contents of teh file with the encrypted string

This is only one way you could solve this problem. Whichever way you solve 
the problem, ensure you always use try/except blocks when opening files on 
the computer
'''

filename = "paragrdaph.txt"
new_string = ""                         # Empty string to hold the new encrypted text
read_succesful = False                  # Flag to check if the file was read succesfully

try:
    with open(filename, "r") as fileHandler:

        char = fileHandler.read(1)
        while char:
            if "a" <= char <= "m" or "A" <= char <= "M":
                num = ord(char) + 13    # Add 13 to the ASCII code of char if it's from [a-m] or [A-M]
                new_string += chr(num)  # Add the new character to the new string

            elif "n" <= char <= "z" or "N" <= char <= "Z":
                num = ord(char) - 13    # Subtract 13 from the ASCII code of char if it's from [n-z] or [N-Z]
                new_string += chr(num)  # Add the new character to the new string

            else:
                new_string += char      # Add the original character to the new string
                
            char = fileHandler.read(1)  # Read the next character from the file.
                                        # If there is no character then our while loop will stop

    # [with open("paragraph.txt", "r") as fileHandler] automatically closes the fileHandler when completed
    # But if using other methods of opening the file you would have to explicitly close the file like so:
    # fileHandler.close()

    read_succesful = True               # If we reach this line it means we've successfully encrypted the file
                                        # But we have not overwritten the file yet

except:
    print(f"Error attempting to read the file {filename}")


# Try to write the new encrypted string to the same file
# but only if we've successully encrypted it in the previous step
if (read_succesful):
    try:
        # Overwrite the text file with the new string
        # I will demonstrate a different method to open/close a file if not using the [with ... as ...] method
        fileHandler = open(filename, "w")
        fileHandler.write(new_string)       # Overwrite with the modified content
        fileHandler.close()                 # Always ensure a file is closed when finished

        print("Done!")

    except:
        print(f"Error attempting to write to file {filename}")
