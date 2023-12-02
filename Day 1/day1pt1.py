import re

sum = 0
line = input()
while line != "":
    digits = list(map(int, re.findall(r'\d', line)))
    cal = digits[0] * 10 + digits[-1]
    sum += cal
    line = input()

print(sum)