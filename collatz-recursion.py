## CollatzRecursion


###
# define your RECURSIVE version of Collatz below this comment so that it runs
# correctly when called from below.
#
# REQUIREMENTS:
#  a) The correct sequence must be printed, all the values on one line.
#  b) Your Collatz function must use recursion.
#  c) Aside from two arguments accepting a positive integer value and the letter
#     F, B, or P; your Collatz function MAY NOT use any other internal or external 
#     variables.
#  d) Your Collatz function may accept only the two arguments described in (c).
#  e) If the second argument is 'F', the sequence should b printed in its
#       naturally generated order.
#     If the second argument is 'B', the sequence should be printed in reverse.
#     If the second argument is 'P', then a palindrome of the sequence values should 
#       be printed (see http://en.wikipedia.org/wiki/Palindrome).  In this case
#       it doesn't matter if your function prints the first value as 1 or the
#       value provided by the user.
###

def Collatz( m, dm):
	if (dm != 'B'):
		print m,
	if (m!=1):
		if (m%2 == 0):
			Collatz( m/2, dm)
		else:
			Collatz( 3*m +1, dm)
	if (dm == 'B'):
		print m,
	elif(dm == 'P' and m!=1):
		print m,
	return m

###
# Do NOT alter Python code below this line
###
m = input( "Enter a positive integer value: " )
displaymode = ''  # initialize to anything not F, B, P
while displaymode not in ['F', 'B', 'P'] :
    displaymode = raw_input( "Choose a display mode:  F=forward, B=backward, P=palindrome: " )

Collatz( m, displaymode )
print 

