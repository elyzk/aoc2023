import re

f = open("input.txt")

lines = f.readlines()

sum = 0
for line in lines:
    line = line.strip()
    id = re.search(r'\d+', line).group(0)
    games = re.split(r':|;', line)[1:]

    maxes = {"red": 0, "green": 0, "blue": 0}

    for game in games:
        cubes = game.split(',')
        for cube in cubes:
            num, color = cube.split()
            if int(num) > maxes[color]:
                maxes[color] = int(num)
    power = 1
    for color in maxes:
        power *= maxes[color]
    sum += power

print(sum)