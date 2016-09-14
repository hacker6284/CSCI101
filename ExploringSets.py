emptySet = set([])
dataSet = set([3, 'A', 7, 'S', 3.14159])

print "emptySet is", emptySet
print "dataSet is", dataSet
emptySet.add("inserted string")
dataSet.remove('A')

print "emptySet is", emptySet
print "dataSet is", dataSet

a = set([1,3])
b = set(['One', 'Three'])

c = a.union(b)
print c

d = c.union(b)
print d

true_or_false = 3 in c
print "3 is in c", true_or_false

print "'FortyTwo' is in d", 'Forty Two' in c

d.remove('FortyTwo')
d.discard('FortyTwo')
print d
