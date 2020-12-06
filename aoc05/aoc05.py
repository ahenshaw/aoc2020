table = str.maketrans('FBLR','0101')
seats = [int(x.translate(table), base=2) for x in open('input.txt')]
print('Part 1:', max(seats))
print('Part 2:', set(range(min(seats), max(seats)))-set(seats))