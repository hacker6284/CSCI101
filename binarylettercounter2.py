def letters(n):
    num = str(bin(n)[2:])
    let = ""
    for d in num:
        if d == "0":
            let = let + "zero"
        elif d == "1":
            let = let + "one"
    return let
num = letters(int(raw_input("Enter Number: ")))
i=1
while len(num) != 13 and len(num) != 18:
    print num, len(num)
    num = letters(int(len(num)))
    i+=1
else:
    print num, len(num)
    print "Finished with length %d after %d iterations"%(len(num),i)
