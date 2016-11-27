import math

Basestring = raw_input("Enter the coefficient symbols: ")
x = int(raw_input("Enter a non-negative integer to convert: "))

def Encode(x,string):
	B = len(string)
	output = ""
	if (x>=B):
		output += str(Encode((x-(x%B))/B,string))
	return output + string[(x%B)]
	#else:
		#return output
if (x>=0):
	print "Base %d: %s"%(len(Basestring),Encode(x,Basestring))
else:
	print "Goodbye!"
