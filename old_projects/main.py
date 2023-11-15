with open("demofile.txt", "rb+") as f:
    print(f.read(5))  # Read the first 5 bytes of the file
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    (f.seek(0))  # Go to the 0th byte of the file
    print(f.read(10))  # Read the first 10 bytes of the file
    (f.seek(0))  # Go to the 0th byte of the file
    print(f.readline())  # Read the first line of the file
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    (f.seek(0))  # Go to the 0th byte of the file
    print(f.readlines())  # Read all the lines of the file
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    (f.seek(0))  # Go to the 0th byte of the file
    print(f.tell())  # Print the current position of the file pointer
    (f.seek(-51, 2))  # Go to the 51st byte from the end of the file
    print(f.tell())  # Print the current position of the file pointer
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    print(f.read(50))  # Read the last 50 bytes of the file
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
