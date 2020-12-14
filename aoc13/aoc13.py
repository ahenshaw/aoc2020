from xgcd import xgcd, gcd
from crt import chinese_remainder
from itertools import combinations

fn = 'input.txt'
# fn = 'test.txt'
# fn = 'test2.txt'

def part1(lines):
    t = int(lines[0])
    buses = []
    for bus in lines[1].split(','):
        try:
            x = int(bus)
            buses.append(x)
        except:
            pass

    wait = []
    for x in buses:
        m, l = divmod(t, x)
        w = x * (m + 1) - t 
        wait.append((w, x))
    print(wait)
    a, b = min(wait)
    print('Part 1:', t, a*b)

def part2(lines):
    t = 754018
    # print(t % 67 == 0)
    # print(t % 7 == 6)
    # print(t % 59 == 57)
    # print(t % 61 == 58)
    # print('Part 2:')
    n = []
    a = []
    for i, bus in enumerate(lines[1].split(',')):
        try:
            n1 = int(bus)
            rem = (n1-i)%n1
        except ValueError:
            pass
        else:
            if i==0 or True: #i != n[0]:
                n.append(n1)
                a.append(rem)
            else:
                print('skipping', n[0], n1, rem, i)
    for n1, n2 in combinations(n, 2):
        if gcd(n1, n2) != 1: print('   ', n1, n2)

    print(n)
    print(a)
    result = int(chinese_remainder(n, a))
    for x, y in zip(n, a):
        print(x, result % x, y)
    print(result)

if __name__ == '__main__':
    lines = list(open(fn))
    # part1(lines)
    part2(lines)
    # skipping 479 456
    # skipping 29 6
    # 50744620826
    # n = [41, 37, 13, 17, 373, 19, 479, 29]
    # a = [28, 20, 3, 11, 319, 456, 6]
    # r = int(chinese_remainder(n, a))
    # print(r, len(f"{r}"))
    # print(len('100000000000000'))
