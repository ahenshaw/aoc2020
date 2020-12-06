
def part1(data):
    ''' Count the occurrences of the key letter in the string.
        Increment the valid count if the count falls within the
        required range.'''

    valid = 0
    for low, high, letter, string in data:
        valid += low <= string.count(letter) <= high
    print('Part1:', valid)

def part2(data):
    ''' Check that the key letter occurs in one-and-only one of
        the two index positions specified in the code.
        If so, increment the valid count.'''

    valid = 0
    for low, high, letter, string in data:
        valid += (string[low-1] == letter) ^ (string[high-1] == letter)
    print('Part2:', valid)

# read and parse the input
data = []
for line in open('input.txt'):
    rule, letter, string = line.strip().split(' ')
    low, high = map(int, rule.split('-'))
    letter = letter[0]
    data.append((low, high, letter, string))

part1(data)
part2(data)

