from itertools import chain, combinations

def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    xs = list(iterable)
    return chain.from_iterable(combinations(xs,n) for n in range(len(xs)+1))

fn = "input.txt"
fn = "test.txt"
# fn = "test2.txt"

def part1():
    # parse the data
    data = []
    mem = {}
    b = 0
    v = 0
    for line in open(fn):
        left, right = line.split(' = ')
        if left == 'mask':
            mask = 0
            bits = 0
            for c in right.strip():
                mask <<= 1
                bits <<= 1
                if c != 'X':
                    bits |= int(c)
                else:
                    mask |= 1
        if left.startswith('mem'):
            addr = int(left[4:-1])
            data  = int(right)
            mem[addr] = data & mask | bits
    print(mem)
    print(sum(mem.values()))


def part2():
    mem = {}
    b = 0
    v = 0
    wild = set()
    for line in open(fn):
        left, right = line.split(' = ')
        if left == 'mask':
            mask = right.strip()
            print(mask)
            bits = 0
            v = 0
            wild = []
            for i, c in enumerate(mask):
                bits <<= 1
                v <<= 1
                if c != 'X':
                    v |= int(c)
                else:
                    bits |= 1
                    wild.append(35-i)
            # print(hex(b), hex(v))
        if left.startswith('mem'):
            val = int(right)
            addr = int(left[4:-1])
            addr |= v
            for x in powerset(wild):
                newaddr = addr
                mask = 0
                for w in wild:
                    if w in x:
                        newaddr |= 1 << w
                        mask |= 1 << w
                    else:
                        newaddr &= ~(1 << w)
                        mask &= ~(1 << w)
                mem[newaddr] = val
    print(mem)
    print(sum(mem.values()))



part1()

# part2()
