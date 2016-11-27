i = int(raw_input("Enter a positive integer value: "))
length = 1
start = i
inc = 0
dec = 0
while (i>1):
    if (i%2 == 0):
        i = i/2
        dec = dec + 1
        length = length + 1
        print i,
    else:
        i = 3*i+1
        inc = inc + 1
        print i,
        length = length + 1
print "\nHailstone sequence length for %d is %d with %d increases and %d decreases."%(start,length,inc,dec)
