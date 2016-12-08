string = raw_input("Enter the string: ")
for i in string:
    print "%08d" %(int(bin(ord(i))[2:])),
