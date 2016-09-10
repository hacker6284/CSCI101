import random
roll = raw_input("Would you like to roll?(y/n)\n")
if roll == "y":
    roll = 1
    while roll == 1:
        s = int(raw_input("How many sides?\n"))
        d = random.randint(1,s)
        print d
        if d == s:
            print "Critical Hit!"
        if d == 1:
            print "Critical Fail!"
        if raw_input("Roll again?(y/n)") == "y":
            roll = 1
        else:
            print "Damn"
            roll = 0
else: print "Damn"
