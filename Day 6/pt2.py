import re
import math

f = open("input.txt")
time = int(''.join(re.findall('\\d+', f.readline())))
distance = int(''.join(re.findall('\\d+', f.readline())))

b = ((time**2 - 4*distance)**(1/2))/2
minHold = math.floor(time/2 - b + 1)
maxHold = math.ceil(time/2 + b - 1)
numWays = maxHold - minHold + 1

print(numWays)





