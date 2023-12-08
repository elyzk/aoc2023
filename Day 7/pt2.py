f = open("input.txt")

lines = [line.strip() for line in f.readlines()]
cardBids = {}
typeCards = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
labels = ['J','2', '3', '4', '5','6','7','8','9','T','Q','K','A']

for line in lines:
    cards = line.split(" ")[0]
    bid = int(line.split(" ")[1])
    cardBids[cards] = bid
    type = 0

    cardFreqs = {}
    numJokers = 0
    for c in cards:
        if c == 'J':
            numJokers += 1
        else:
            if c in cardFreqs:
                cardFreqs[c] += 1
            else:
                cardFreqs[c] = 1

    maxFreq = -1
    max = ''
    for card in cardFreqs.keys():
        if cardFreqs[card] > maxFreq:
            maxFreq = cardFreqs[card]
            max = card
    if max != '':
        cardFreqs[max] += numJokers
    else:
        cardFreqs['A'] = numJokers

    if len(cardFreqs) == 5:
        type = 0
    elif len(cardFreqs) == 4:
        type = 1
    elif len(cardFreqs) == 3:
        type = 2
        for freq in cardFreqs.values():
            if freq == 3:
                type = 3
    elif len(cardFreqs) == 2:
        type = 4
        for freq in cardFreqs.values():
            if freq == 4:
                type = 5
    else:
        type = 6
    typeCards[type].append(cards)

cardRanks = {}

totalBefore = 0
for type in typeCards.keys():
    for i in range(len(typeCards[type])):
        firstCard = typeCards[type][i]
        greaterThan = 0
        for j in range(0, len(typeCards[type])):
            if i != j:
                secondCard = typeCards[type][j]
                for idx in range(5):
                    if labels.index(firstCard[idx]) > labels.index(secondCard[idx]):
                        greaterThan += 1
                        break
                    elif labels.index(firstCard[idx]) < labels.index(secondCard[idx]):
                        break
        cardRanks[firstCard] = greaterThan + totalBefore + 1
    totalBefore += len(typeCards[type])

sum = 0
for card in cardRanks.keys():
    sum += cardBids[card] * cardRanks[card]

print(sum)