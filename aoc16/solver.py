fn = "input.txt"
# fn = "test.txt"
# fn = "test1.txt"
from collections import defaultdict

def part1(data):
    pass

def part2(data):
    pass

# parse the data
data = []
seats = []
mode = True
for line in open(fn):
    if ' or ' in line:
        left, right = line.split(': ')
        groups = right.split(' or ')
        for group in groups:
            rng = [int(x) for x in group.split('-')]
            data.append(range(rng[0], rng[1]+1))
    if ',' in line:
        if mode:
            mode = False
            continue
        l = [int(x) for x in line.split(',')]
        seats.extend(l)
total = 0
for seat in seats:
    if not any([seat in x for x in data]):
        total += seat
print(total)


# parse the data
data = []
tickets = []
mode = True
desc = {}
for line in open(fn):
    if ' or ' in line:
        left, right = line.split(': ')
        g = []
        groups = right.split(' or ')
        for group in groups:
            rng = [int(x) for x in group.split('-')]
            data.append(range(rng[0], rng[1]+1))
            g.extend(list(data[-1]))
        desc[left] = g
    if ',' in line:
        l = [int(x) for x in line.split(',')]
        if mode:
            mode = False
            my_ticket = l
        else:
            tickets.append(l)
total = 0
valid = []
for ticket in tickets:
    dirty = False
    for info in ticket:
        if not any([info in x for x in data]):
            dirty = True
    if not dirty:
        valid.append(ticket)
# print(my_ticket)
# print(desc)
fields = {}
for key, value in desc.items():
    # print(key, value)
    for p in range(len(tickets[0])):
        fields[(key, p)] = True
    for nearby in valid:
        # print('    ', nearby)
        for pos, x in enumerate(nearby):
            # print('        ', pos, x, x in value)
            if x not in value:
                fields[(key, pos)] = False
                # print('            Field', pos, "can't be", key)



possible = defaultdict(set)
for (d, pos), m in fields.items():
    if m:
        possible[d].add(pos)

known = dict()
while possible:
    drop = set()
    for key, ps in possible.items():
        if len(ps) == 1:
            field = ps.pop()
            known[key] = field
            # print('found', key, 'is field', field)
            for key, ps in possible.items():
                ps.discard(field)
                if len(ps) == 0:
                    drop.add(key)
    for x in drop:
        del possible[x]

print(known)

p = 1
for key, field in known.items():
    if key.startswith('departure'):
        p *= my_ticket[field]
print('Answer:', p)






