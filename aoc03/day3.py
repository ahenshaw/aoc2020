def trees(data, right, down):
    count = row = col = 0
    while row < len(data):
        line = data[row].strip()
        count += line[col % len(line)] == '#'
        col += right
        row += down
    return count

data = list(open('input.txt'))

##### Part 1 #####
print('Part 1:', trees(data, 3, 1))

##### Part 2 #####
product = 1
for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    product *= trees(data, right, down)

print('Part 2:', product)


