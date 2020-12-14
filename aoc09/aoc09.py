from time import perf_counter

# fn, backtrack = 'input.txt', 25
fn, backtrack = 'test.txt', 5

def part1(numbers, backtrack):
    index = backtrack
    while True:
        target = numbers[index]
        window = sorted(numbers[index-backtrack:index])
        found = False
        for i in range(len(window)-1):
            if window[i] > target:
                return target
            for j in range(i+1, len(window)):
                if window[j] > target: 
                    return target
                if target == window[i] + window[j]:
                    found = True
                    break
            if found:
                break
        else:
            return target
        index += 1

def part2(numbers, target):
    for i in range(len(numbers)-1):
        if numbers[i] > target:
            continue
        total = numbers[i]
        for j in range(i+1, len(numbers)):
            total += numbers[j]
            if total == target:
                partition = sorted(numbers[i:j+1])
                return partition[0] + partition[-1]
            if total > target:
                break


# parse the input data
numbers = [int(x) for x in open(fn)]

start = perf_counter()
target = part1(numbers, backtrack) 
print(perf_counter()-start)

print('Part 1:', target)

print('Part 2:', part2(numbers, target))
