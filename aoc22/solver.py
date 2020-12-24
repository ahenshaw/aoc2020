fn = "input.txt"
# fn = "test.txt"

# parse the data
# data = open(fn).readlines()

# for line in open(fn):
#     pass

p1 = 'Player 1'
p2 = 'Player 2'
blocks = open(fn).read().split('\n\n')
cards = {}
for block in blocks:
    lines = block.split('\n')
    cards[lines[0][:-1]] = [int(x) for x in lines[1:] if x]

print(cards)
round = 0
while cards[p1] and cards[p2]:
    round += 1
    c1 = cards[p1].pop(0)
    c2 = cards[p2].pop(0)
    # print(round, c1, c2)
    if c1 > c2 :
        # print(p1, "wins")
        cards[p1].extend([c1,c2])
    elif c2 > c1:
        # print(p2, "wins")
        cards[p2].extend([c2,c1])
    # print(cards)

score = 0
winner = cards[p1] if cards[p1] else cards[p2]
for i, c in enumerate(reversed(winner)):
    score += (i+1)* c
print(score)