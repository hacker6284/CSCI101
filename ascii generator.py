string = raw_input("Enter the string: ")
for i in string:
    print bin(ord(i))[2:] + " "
