import re
import math
f = open("input.txt")
times = list(map(int, re.findall('\\d+', f.readline())))
distances = list(map(int, re.findall('\\d+', f.readline())))
numWays = []

for i in range(len(times)):
    time = times[i]
    dist = distances[i]
    b = ((time**2 - 4*dist)**(1/2))/2
    minHold = math.floor(time/2 - b + 1)
    maxHold = math.ceil(time/2 + b - 1)
    numWays.append(maxHold - minHold + 1)

ans = 1
for num in numWays:
    ans *= num

print(ans)




