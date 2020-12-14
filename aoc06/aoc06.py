from string import ascii_lowercase

total1 = total2 = 0
for group in open('input.txt').read().split('\n\n'):
    # start with empty set for answer to Part 1
    combined = set()

    # start with complete set for answer to Part 2
    common = set(ascii_lowercase)

    for person in group.split():
        combined = combined.union(set(person))
        common   = common.intersection(set(person))
    total1 += len(combined)
    total2 += len(common)

print('Part 1:', total1)
print('Part 2:', total2)