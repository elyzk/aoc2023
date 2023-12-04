import re
f = open("input.txt")

lines = f.readlines()

sum = 0
symbols = "!@#$%^&*()/_+=-\\"
for i in range(len(lines)):
    line = lines[i].strip()
    for number in re.compile('\\d+').finditer(line):
        startPos = number.start()
        endPos = number.end()  # end is exclusive
        foundSymbol = False

        # diagonals
        if startPos != 0:
            if i != len(lines) - 1:  # bottom left diagonal
                if lines[i+1][startPos-1] in symbols:
                    foundSymbol = True
            if i != 0:  # top left diagonal
                if lines[i-1][startPos-1] in symbols:
                    foundSymbol = True

        if endPos != len(line):
            if i != len(lines) - 1:  # bottom right diagonal
                if lines[i+1][endPos] in symbols:
                    foundSymbol = True
            if i != 0:  # top right diagonal
                if lines[i-1][endPos] in symbols:
                    foundSymbol = True

        for j in range(startPos, endPos):
            # looking up and down
            if i != len(lines) - 1:
                if lines[i + 1][j] in symbols:
                    foundSymbol = True
                    break
            if i != 0:
                if lines[i - 1][j] in symbols:
                    foundSymbol = True
                    break
        # looking left and right
        if startPos != 0:
            if lines[i][startPos - 1] in symbols:
                foundSymbol = True
        if endPos != len(line):
            if lines[i][endPos] in symbols:
                foundSymbol = True

        if foundSymbol:
            sum += int(number.group())

print(sum)




