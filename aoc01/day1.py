from math      import prod
from itertools import product

def solve(data, n, label):
    for group in product(*(data,)*n):
        if sum(group) == 2020:
            print(f'{label}: {prod(group)}')
            return

data = list(map(int, open('input.txt').readlines()))
solve(data, 2, 'Part 1')
solve(data, 3, 'Part 2')