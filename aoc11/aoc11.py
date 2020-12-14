import numpy as np
from time import perf_counter
from copy import deepcopy
fn = 'input.txt'
# fn = 'test.txt'
# fn = 'small.txt'

def part1(n):
    print(n)
    pass

def part2(n):
    pass

def around(grid, r, c):
    occ = []
    for y in (-1, 0, 1):
        ry = r+y
        if ry < 0:
            continue
        for x in (-1, 0, 1):
            cx = c+x
            if cx < 0: 
                continue
            if x==0 and y==0:
                continue
            try:
                occ.append(grid[r+y][c+x])
            except IndexError:
                occ.append('.')
    return occ

def cansee(grid, r, c, rows, cols):
    occ = []
    cr = r; cc = c
    seen = []
    for i in range(3):
        row = [False for j in range(3)]
        seen.append(row)
    seen[1][1] = True

    circle = 0
    while True:
        circle += 1
        for y in [-1, 0, 1]:
            rx = r + y*circle
            if rx < 0 or rx >= rows:
                for j in (0, 1, 2):
                    seen[y+1][j]=True
                continue

            for x in [-1, 0, 1]:
                cx = c + x*circle
                if cx < 0 or cx >= cols:
                    for i in (0, 1, 2):
                        seen[i][x+1]=True
                    continue
                if rx == r and cx == c:
                    continue
                if not seen[y+1][x+1]:
                    try:
                        seat = grid[rx][cx]
                    except IndexError:
                        pass #print(rows, cols, rx, cx)
                    else:
                        if seat in 'L#':
                            occ.append(seat)
                            seen[y+1][x+1] = True
                # if r == 0 and c ==2:
                #     print(circle, rx, cx, seen)
                # print('   ', y, x, seen)
        if  all([item for sublist in seen for item in sublist]):
            break
    return occ


    


def cycle(grid):
    nextg = deepcopy(grid)
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            # occ = around(grid, r, c)
            occ = around(grid, r, c)
            seat = grid[r][c] 
            if seat == 'L' and '#' not in occ:
                nextg[r][c] = '#'
            if seat == '#' and occ.count('#') >= 4:
                nextg[r][c] = 'L'

    return nextg

def cycle2(grid):
    nextg = deepcopy(grid)
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            occ = cansee(grid, r, c, rows, cols)
            seat = grid[r][c] 
            if seat == 'L' and '#' not in occ:
                nextg[r][c] = '#'
            if seat == '#' and occ.count('#') >= 5:
                nextg[r][c] = 'L'

    return nextg

def pp(grid):
    for row in grid:
        print(''.join(row))

def test(a, b):
    rows = len(a)
    cols = len(a[0])
    for r in range(rows):
        for c in range(cols):
            if a[r][c] != b[r][c]:
                return False
    return True
# parse the input data
# numbers = [int(x) for x in open(fn)]
grid =  [list(line.strip())  for line in  open(fn)]
pp(grid)
# while True:
#     ng = cycle(grid)
#     if test(ng, grid):
#         break
#     grid = ng
#     # print()
#     # pp(grid)
# pp(ng)
# count = 0
# for row in ng:
#     count += row.count('#')
# print(count)


while True:
    ng = cycle2(grid)
    if test(ng, grid):
        break
    grid = ng
    # print()
    # pp(grid)

count = 0
for row in ng:
    count += row.count('#')
print(count)

# start = perf_counter()
# part1(numbers)
# part2(numbers)