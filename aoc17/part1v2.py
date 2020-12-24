from itertools import product
fn = "input.txt"
# fn = "test.txt"

def neighbors(index):
    dims = len(index)
    for offset  in product(*[(-1, 0, 1)]*dims):
        if any(offset):
            yield tuple((a + b for a,b in zip(index, offset)))

CYCLES = 6
# parse the input data
active = set()
w = z = 0
for y, line in enumerate(open(fn)):
    for x, c in enumerate(line):
        if c == '#':
            active.add((x, y, z, w))

CYCLES = 6
for i in range(CYCLES):
    inactive = set()
    new_active = set()
    for index in active:
        counter = 0
        for n in neighbors(index):
            if n in active:
                counter += 1
            else:
                inactive.add(n)
        if 2 <= counter <= 3:
            new_active.add(n)
    for index in inactive:
        counter = 0
        for n in neighbors(index):
            counter += n in active
        if counter == 3:
            new_active.add(n)
    active = new_active
    print(i+1, len(active))
