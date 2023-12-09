import re
f = open("input.txt")

lines = f.readlines()

s = 0
for line in lines:
    nums = list(map(int, re.findall("-?\\d+", line)))[::-1]
    cur = nums
    allDiffs = [nums]
    nextNum = 0
    done = False
    while not done:
        done = True
        if len(cur) > 1:
            diffs = []
            for i in range(1, len(cur)):
                diffs.append(cur[i] - cur[i-1])
                if cur[i] - cur[i-1] != 0:
                    done = False
            cur = diffs
            allDiffs.append(diffs)
    for i in range(len(allDiffs)):
        # print(f'Line {lines.index(line)}: {allDiffs[i]}')
        nextNum += allDiffs[i][-1]
    print(nextNum)
    s += nextNum

print(s)