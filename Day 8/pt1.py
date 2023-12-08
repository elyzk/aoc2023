import re
f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

instructions = lines[0]
network = {}

for line in lines[2:]:
    node = re.match('\\w{3}', line).group()
    connections = re.findall('\\w{3}', line)[1:]

    network[node] = connections

found = False
cur = "AAA"
idx = 0
steps = 0

while not found:
    if instructions[idx] == "L":
        cur = network[cur][0]
    else:
        cur = network[cur][1]
    steps += 1
    if cur == "ZZZ":
        found = True
    idx = (idx + 1) % len(instructions)

print(steps)
