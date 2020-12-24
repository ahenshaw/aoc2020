from collections import defaultdict
fn = "input.txt"

def game(start_sequence, limit):
    spoken = defaultdict(list)

    for i in range(limit):
        if i < len(start_sequence):
            last = start_sequence[i]
        else:
            when = spoken[last]
            last = 0 if len(when) < 2 else when[-1] - when[-2]
        spoken[last].append(i)
    print('Answer:', last)


data = list(map(int, open(fn).read().split(',')))
game(data, 2020)
game(data, 30_000_000)
