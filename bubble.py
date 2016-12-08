contenders = []
inp = []
while "done" not in inp:
    inp = [raw_input("Enter the Contender: ")]
    if "done" not in inp:
        contenders += [inp]
length = len(contenders)
print contenders
j = 0
while j < length -1:
    i = length -1
    while i > 0:
        if contenders[i][0] not in contenders[i-1]:
            better = int(raw_input("Is %s better than %s? 1 for yes, 0 for no"%(contenders[i][0],contenders[i-1][0])))
            if better == 0:
                contenders[i-1] += [contenders[i][0]]
            else:
                contenders[i] += [contenders[i-1][0]]
                temp = contenders [i-1]
                contenders [i-1] = contenders[i]
                contenders [i] = temp
        i -= 1
    j += 1
for i in contenders:
    print i[0],
