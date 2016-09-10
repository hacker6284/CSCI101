import math
import random
print math.cos(0)
angle = math.radians(random.randint(0,360))
print math.cos(angle)
print math.floor(math.cos(angle))
for i in range(0,100):
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    print math.fmod(x,y)
    print x % y
