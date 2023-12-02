import re

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
wordToNum = {words[i] : nums[i] for i in range(len(nums))}

def convertToNum(str):
    if str in words:
        return wordToNum[str]
    return str

sum = 0
line = input()

matchString = '\d'

for word in wordToNum:
    matchString += '|' + word

matchexp = r'(?=(' + matchString + '))'

while line != "":
    matches = re.finditer(matchexp, line)
    digitStrings = [convertToNum(match.group(1)) for match in matches]
    digits = [int(digit) for digit in digitStrings]
    cal = digits[0] * 10 + digits[-1]
    sum += cal
    line = input()

print(sum)