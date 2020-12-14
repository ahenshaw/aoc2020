from collections import defaultdict

# parse the input data
inner_key = defaultdict(set)
outer_key = defaultdict(list)
for rule in open('input.txt'):
    left, right = rule.strip().split('contain')
    outer = ' '.join(left.split()[0:2])
    for item in right.split(', '):
        if 'no other' in item:
            continue
        count, adjective, color, noun = item.strip().split()
        count = int(count)
        inner = f'{adjective} {color}'

        # build two dictionaries that go the opposite ways in
        # the hierarchy: child -> set(parents) and parent -> list(children)
        inner_key[inner].add(outer)
        outer_key[outer].append((count, inner))

def find_parents(target, outer):
    for style in inner_key[target]:
        outer.add(style)
        find_parents(style, outer)

def find_child_count(style):
    total = 1
    for count, child_style in outer_key[style]:
        total += count * find_child_count(child_style)
    return total

TARGET = 'shiny gold'
outer = set()
find_parents(TARGET, outer)
print('Part 1:', len(outer))

total = find_child_count(TARGET)
print('Part 2:', total-1)