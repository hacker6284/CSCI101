#function for counting letters
def letters(n):
    num = str(bin(n)[2:])
    let = 0
    for d in num:
        if d == "0":
            let = let + 4
        elif d == "1":
            let = let + 3
        else:
            return 0
    return let

#finding fixed point
eighteen = 0.0
thirteen  = 0.0
for i in range(1,1000000):
    cont = 1
    j = i
    while cont == 1:
        let = letters(j)
        if let == 18:
            eighteen += 1
            cont = 0
        elif let == 13:
            thirteen += 1
            cont = 0
        else:
            j = let
            cont = 1
    if i%100000 == 0:
        print i
total = eighteen + thirteen
print "18:"
print 100 * (eighteen / total)
print "13:"
print 100 * (thirteen / total)
