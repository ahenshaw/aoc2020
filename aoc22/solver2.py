from logging import basicConfig, info, debug, log, DEBUG, INFO
basicConfig(level=INFO, format='%(message)s')
fn = "input.txt"
# fn = "test.txt"
# fn = "test2.txt"

info(f'Input file name: {fn}')
p1 = 'Player 1'
p2 = 'Player 2'

def play(cards, game):
    played1 = set()
    played2 = set()
    cp1 = cards[p1]
    cp2 = cards[p2]
    
    round = 1
    while cp1 and cp2:
        debug(f'-- Round {round} Game {game}')
        debug(f'{p1} deck: {cp1}')
        debug(f'{p2} deck: {cp2}')
        if tuple(cp1) in played1:
            debug('short circuit on', p1)
            return p1, cp1
        if tuple(cp2) in played2:
            debug('short circuit on', p2)
            return p1, cp1
        played1.add(tuple(cp1))
        played2.add(tuple(cp2))
        c1 = cp1.pop(0)
        c2 = cp2.pop(0)
        debug(f'{p1} plays: {c1}')
        debug(f'{p2} plays: {c2}')
        if len(cp1) >= c1 and len(cp2) >= c2:
            debug('playing sub game')
            newcards = {p1:cp1[:c1], p2:cp2[:c2]}
            winner, _ = play(newcards, game+1)
            if winner == p1:
                cards[p1].extend([c1,c2])
            else:
                cards[p2].extend([c2,c1])
        elif c1 > c2 :
            debug(p1, 'wins\n')
            cards[p1].extend([c1,c2])
        elif c2 > c1:
            debug(p2, 'wins\n')
            cards[p2].extend([c2,c1])
        round += 1
    if len(cp2) > len(cp1):
        debug(f'{p2} is winner')
        return p2, cp2
    else:
        debug(f'{p1} is winner')
        return p1, cp1

blocks = open(fn).read().split('\n\n')
cards = {}
for block in blocks:
    lines = block.split('\n')
    cards[lines[0][:-1]] = [int(x) for x in lines[1:] if x]

debug(f'{cards}')
winner, cards = play(cards, 1)
score = 0
for i, c in enumerate(reversed(cards)):
    score += (i+1)* c
print(score)