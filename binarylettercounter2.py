import requests

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
orig = int(raw_input("Enter Number: "))
num = letters(orig)
i=1
while len(num) != 13 and len(num) != 18:
    print num, len(num)
    num = letters(int(len(num)))
    i+=1
else:
    print num, len(num)
    print "Number %d finished with length %d after %d iterations"%(orig,len(num),i)

groupme = raw_input("Send to GroupMe? (y/n)")
if groupme == "y":
    key = raw_input("Enter Key: ")
    ifttt("binary", orig, len(num), i, key)
else:
    print "Okay."
