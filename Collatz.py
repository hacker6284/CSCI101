i = int(raw_input("Enter a positive integer value: "))
hail = [i]
length = 1
inc = 0
dec = 0
while (i>1):
    if (i%2 == 0):
        i = i/2
        dec = dec + 1
    else:
        i = 3*i+1
        inc = inc + 1
    length = length + 1
    hail.append(i)
for j in hail:
    print j,
print "\nHailstone sequence length for %d is %d with %d increases and %d decreases."%(hail[0],length,inc,dec)
