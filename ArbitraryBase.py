import math

Basestring = raw_input("Enter the coefficient symbols: ")
x = 1

def Encode(x,string):
	B = len(string)
	output = ""
	if (x>=B):
		output += str(Encode((x-(x%B))/B,string))
	return output + string[(x%B)]
	#else:
		#return output
while (x>=0):
	x = int(raw_input("Enter a non-negative integer to convert: "))
	if (x<0):
		print "Goodbye!"
	else:	
		print "Base %d: %s"%(len(Basestring),Encode(x,Basestring))
