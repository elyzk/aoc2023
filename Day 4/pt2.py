import re

f = open("input.txt")

lines = [line.strip() for line in f.readlines()]

sum = 0
copies = {}
for line in lines:
    cardData = re.split(r':|\|', line)
    card = int(re.search('\\d+', cardData[0]).group())
    winningNums = [int(m.group()) for m in re.compile('\\d+').finditer(cardData[1])]
    candidates = [int(m.group()) for m in re.compile('\\d+').finditer(cardData[2])]

    numWinners = 0
    for candidate in candidates:
        if candidate in winningNums:
            numWinners += 1
    for i in range(1, numWinners+1):
        copies[card + i] = copies.get(card, 1) + (copies.get(card + i, 1))

for i in range(len(lines)):
    if i+1 not in copies:
        copies[i+1] = 1
for val in copies.values():
    sum += val

print(sum)


