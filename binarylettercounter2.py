import requests
import time

def ifttt(name, value1, value2, value3, key):
    payload = { 'value1' : value1, 'value2' : value2, 'value3' : value3}
    requests.post("https://maker.ifttt.com/trigger/%s/with/key/%s"%(name, key), data=payload)
    
def letters(n):
    num = str(bin(n)[2:])
    let = ""
    for d in num:
        if d == "0":
            let = let + "zero"
        elif d == "1":
            let = let + "one"
    return let

num1 = int(raw_input("Enter First Number: "))
num2 = int(raw_input("Enter Second Number: "))
groupme = raw_input("Send to GroupMe? (y/n)")
if groupme == "y":
    key = raw_input("Enter Key: ")

j=num1
thirteen = 0.0
eighteen = 0.0
while j<=num2:
    orig = j
    num = letters(orig)
    i=1
    while len(num) != 13 and len(num) != 18:
        print num, len(num)
        num = letters(int(len(num)))
        i+=1
    else:
        print num, len(num)
        print "Number %d finished with length %d after %d iterations"%(orig,len(num),i)
        if groupme == "y":
            ifttt("binary", orig, len(num), i, key)
        else:
            print "Okay."
        if len(num) == 13:
            thirteen+=1
        else:
            eighteen+=1
    j+=1
print "%f of the %d numbers finished with length 13 and %f finished with length 18"%(thirteen/(thirteen+18),num2-num1,eighteen/(thirteen+18))
if groupme == "y":
    ifttt("binary2", thirteen/(thirteen+eighteen), num2-num1, eighteen/(thirteen+eighteen), key)
