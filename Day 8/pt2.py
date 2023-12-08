import re
import math
from functools import reduce
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

instructions = lines[0]
network = {}
startNodes = []

for line in lines[2:]:
    node = re.match('\\w{3}', line).group()
    connections = re.findall('\\w{3}', line)[1:]

    if node[-1] == "A":
        startNodes.append(node)
    network[node] = connections

found = False
curs = startNodes
idx = 0
steps = 0
nodeSteps = {}

while len(nodeSteps) < len(startNodes):
    for i, cur in enumerate(curs):
        if instructions[idx] == "L":
            curs[i] = network[cur][0]
        else:
            curs[i] = network[cur][1]
        if cur[-1] == "Z":
            nodeSteps[cur] = steps
    steps += 1
    idx = (idx + 1) % len(instructions)


def lcm(arr):
    rtn = reduce(lambda x, y: math.lcm(x, y), arr)
    return rtn


print(lcm(nodeSteps.values()))
