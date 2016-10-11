sum = 0
i = 1
j = 2
while j<4000000:
    if j%2 == 0:
        sum +=j
    temp = i
    i = j
    j = i + temp
print sum
