import math

Basestring = raw_input("Enter the coefficients: ")
x = int(raw_input("Enter a non-negative integer to convert: "))

def Encode(x,i,string):
	B = len(string)
	output = ""
	if (x>=B**i):
		output += str(Encode(x-(x%B**(i+1)),i+1,string))
		return output + string[(x%B**(i+1))/B**i]
	else:
		return output
if (x>=0):
	print "Base %d: %s"%(len(Basestring),Encode(x,0,Basestring))
else:
	print "Goodbye!"
