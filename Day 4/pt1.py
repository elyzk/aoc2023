import re

f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

sum = 0
for line in lines:
    card = re.split(r':|\|', line)
    winningNums = [int(m.group()) for m in re.compile('\\d+').finditer(card[1])]
    candidates = [int(m.group()) for m in re.compile('\\d+').finditer(card[2])]

    numWinners = 0
    for candidate in candidates:
        if candidate in winningNums:
            numWinners += 1
    if numWinners > 0:
        sum += 2**(numWinners - 1)

print(sum)


