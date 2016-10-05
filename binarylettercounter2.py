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
print num
print len(num)
