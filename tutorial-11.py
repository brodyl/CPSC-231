import sys

if len(sys.argv) != 2:
    print("You must provide one file name.")
else:
    file_name = sys.argv[1]
    try:
        file = open(file_name, "r")

        for line in file:
            print(line)

        file.close()

    except:
        print("Cannot open file.")
