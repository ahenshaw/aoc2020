from time import perf_counter

fn = 'input.txt'
# fn = 'test.txt'
fn = 'small.txt'


# def part1(numbers, chain, prev, target):
#     possible = [x for x in numbers if (x-prev <=3)]
#     if not possible:
#         return chain
#     for i in possible:
#         branch = chain[:]
#         branch.append(i)
#         test = numbers.copy()
#         test.remove(i)
#         result = part1(test, branch, i, target)
#         if len(result)==target:
#             print(result)

def part1(numbers):
    n = sorted(numbers+[max(numbers)+3])
    start = 0
    counts = [0] * 3
    for i in n:
        counts[i - start - 1] += 1
        start = i
    print(counts[0]*(counts[2]))

def part2(n):
    n = sorted(n+[0]+[max(n)+3])
    print(n)
    splits = []
    last = 0
    for i in range(len(n)-1):
        if n[i+1] - n[i] > 1:
            if i-last > 1:
                splits.append(n[last+1:i])
            last = i+1
    prod = 1
    for split in splits:
        nulls = 0 if len(split) < 3 else 1
        prod *= (2**len(split)-nulls)
    print(prod)




# parse the input data
numbers = [int(x) for x in open(fn)]

# start = perf_counter()
part1(numbers)
part2(numbers)