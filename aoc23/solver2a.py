from cups import Cups
from time import perf_counter

data = '284573961'  # input         
# data = '389125467'  # test
start = perf_counter()
cups = Cups()
for x in data:
    cups.append(int(x))
mincup = 1
maxcup = 1_000_000
for x in range(10, maxcup+1):
    cups.append(x)

for i in range(10_000_000):
    current = cups.head
    # print(f'---- Move {i+1} ----')
    if (i % 100000) == 0:
        print(i)
    pickup = cups.cut(current)
    # print(f'pickup: {pickup}')
    dest = current - 1
    while True:
        if dest < mincup:
            dest = maxcup
        if dest not in pickup:
            break
        dest -= 1
    # print(f'dest: {dest}')
    cups.insert(dest, pickup)
    cups.rotate()
    # print(cups)

while cups.head != 1:
    cups.rotate()
a = cups.get(cups.head)
b = cups.get(a)
print('Part 2:', a*b)
print(perf_counter() - start)

