import re
f = open("input.txt");

sum = 0
lines = f.readlines();
for line in lines:
    digits = list(map(int, re.findall(r'\d', line)))
    cal = digits[0] * 10 + digits[-1]
    sum += cal

print(sum)