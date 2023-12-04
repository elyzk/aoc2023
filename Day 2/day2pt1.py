import re

f = open("input.txt")

lines = f.readlines()

mins = {"red": 12, "green": 13, "blue": 14}

sum = 0
for line in lines:
    line = line.strip()
    id = re.search(r'\d+', line).group(0)
    games = re.split(r':|;', line)[1:]

    possible = True
    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            num, color = cube.split()
            if int(num) > mins[color]:
                possible = False
                break
        if not possible:
            break
    if possible:
        sum += int(id)
print(sum)