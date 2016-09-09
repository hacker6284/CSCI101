word = "Strengths"
guesses = []
guesscount = 10
while guesscount > 0:
    for letter in word:
        if letter in guesses:
            print letter
        print "_"
    print "Guessed:"
    print guesses
    guesses.extend([raw_input("Guess a letter: ")])
    guesscount -= 1
