from time import perf_counter
from collections import defaultdict
from collections import deque
spoken = defaultdict(deque, maxlen=2)

start = [0,3,6]
tick = perf_counter()
for i,n in enumerate(start):
    spoken[n].append(i)
print(spoken)

last=n
for i in range(len(start), 30_000_000):
    if len(spoken[last]) <2:
        last = 0
    else:
        last = spoken[last][-1] - spoken[last][-2]
    spoken[last].append(i)

print('Part2:', last)
print(perf_counter()-tick)
