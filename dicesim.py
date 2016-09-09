import random
roll = raw_input("Would you like to roll?(y/n)\n")
if roll == "y":
    roll = 1
    while roll == 1:
        s = input("How many sides?\n")
        print random.randint(1,s)
        if raw_input("Roll again?(y/n)") == "y":
            roll = 1
        else:
            print "Damn"
            roll = 0
else: print "Damn"
