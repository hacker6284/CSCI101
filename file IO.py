f = file("test.txt", "w")
f.write("Hello file!\n")
f.write("Good-bye file.\n")
f.write("\nA third sentence on the fourth line of the file.\m")
f = file("test.txt", "w")
f.readline()
line2 = f.readline()
emptyline = f.readline()
line3 = f.readline()
f.readline()
f.readline()
f.readline()
print line2
print emptyline
print line3
f.close()
