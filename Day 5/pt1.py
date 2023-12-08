import re
f = open("input.txt")

seeds = list(map(int, re.findall("\\d+", f.readline())))
soils = []
fertilizers = []
waters = []
lights = []
temps = []
humidities = []
locations = []

f.readline()
def convert(starts, ends):
    f.readline()

    # numbers
    line = f.readline().strip()
    startEnd = {}

    while line.strip():
        numbers = list(map(int, re.findall("\\d+", line)))
        startEnd[(numbers[1], numbers[1] + numbers[2])] = numbers[0] - numbers[1]
        line = f.readline().strip()

    for start in starts:
        rangeFound = False
        for range in startEnd.keys():
            if range[0] <= start < range[1]:
                ends.append(start + startEnd[range])
                rangeFound = True
        if not rangeFound:
            ends.append(start)

convert(seeds, soils)
convert(soils, fertilizers)
convert(fertilizers, waters)
convert(waters, lights)
convert(lights, temps)
convert(temps, humidities)
convert(humidities, locations)
print(min(locations))



