import random
play = raw_input("Play Guess the Number?(y/n)\n")
while play == "y":
    n = random.randint(1,100)
    win = 0
    while win == 0:
        g = int(raw_input("Input Guess Between 1 and 100:"))
        if g < n:
            print "Higher"
        elif g > n:
            print "Lower"
        elif g > 100:
            print "Between 1 and 100!!"
        elif g < 1:
            print "Between 1 and 100!!"
        elif g == n:
            print "You did it!"
            win = 1
        else:
            print "error"
    play = raw_input("Play Again?(y/n)\n")
print "Damn"
    
