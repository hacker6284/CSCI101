olda = float( input( "Enter the a element for A: ") )
oldb = float( input( "Enter the b element for A: ") )
oldc = float( input( "Enter the c element for A: ") )
oldd = float( input( "Enter the d element for A: ") )
det = olda*oldd - oldc*oldb
if (det == 0):
    print "The Matrix"
    print "|%10.5f %10.5f|" % (olda, oldb)
    print "|%10.5f %10.5f|" % (oldc, oldd)
    print "is not invertible."
else:
    a = oldd/det
    b = -1*oldb/det
    c = -1*oldc/det
    d = olda/det
    print "The inverse of A (A') is"
    print "|%10.5f %10.5f|" % (a, b)
    print "|%10.5f %10.5f|" % (c, d)
    print "The product of A * A' is"
    print "|%10.5f %10.5f|" % (olda*a+oldb*c, olda*b+oldb*d)
    print "|%10.5f %10.5f|" % (oldc*a+oldd*c, oldc*b+oldd*d)
    
