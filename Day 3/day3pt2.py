import re
f = open("input.txt")

lines = f.readlines()

sum = 0
symbols = "!@#$%^&*()/_+=-\\"
gearNums = {}
for i in range(len(lines)):
    line = lines[i].strip()
    for number in re.compile('\\d+').finditer(line):
        startPos = number.start()
        endPos = number.end()  # end is exclusive
        number = int(number.group())
        # diagonals
        if startPos != 0:
            if i != len(lines) - 1 and lines[i+1][startPos-1] == "*":  # bottom left diagonal
                gearNums[(i+1, startPos-1)] = gearNums.get((i+1, startPos-1), []) + [number]
            if i != 0 and lines[i-1][startPos-1] == "*":  # top left diagonal
                gearNums[(i-1, startPos - 1)] = gearNums.get((i - 1, startPos - 1), []) + [number]

        if endPos != len(line):
            if i != len(lines) - 1 and lines[i+1][endPos] == "*":  # bottom right diagonal
                gearNums[(i+1, endPos)] = gearNums.get((i+1, endPos), []) + [number]
            if i != 0 and lines[i-1][endPos] == "*":  # top right diagonal
                gearNums[(i - 1, endPos)] = gearNums.get((i - 1, endPos), []) + [number]

        for j in range(startPos, endPos):
            # looking up and down
            if i != len(lines) - 1 and lines[i+1][j] == "*":
                gearNums[(i+1, j)] = gearNums.get((i+1, j), []) + [number]
            if i != 0 and lines[i-1][j] == "*":
                gearNums[(i-1, j)] = gearNums.get((i-1, j), []) + [number]
        # looking left and right
        if startPos != 0 and lines[i][startPos-1] == "*":
            gearNums[(i, startPos-1)] = gearNums.get((i, startPos-1), []) + [number]
        if endPos != len(line) and lines[i][endPos] == "*":
            gearNums[(i, endPos)] = gearNums.get((i, endPos), []) + [number]

for value in gearNums.values():
    if len(value) == 2:
        ratio = 1
        for val in value:
            ratio *= val
        sum += ratio
print(sum)




