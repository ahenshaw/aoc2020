import re
fn = "input.txt"
# fn = "test.txt"

def expand(rules, index, depth=0):
    # print('   '*depth, index)
    patterns = []
    for group in rules[index].split(' | '):
        pattern = '('
        for c in group.split():
            if c.isdigit():
                pattern += expand(rules, int(c), depth+1)
            else:
                pattern += c
        pattern += ')'
        patterns.append(pattern)
    return '(' + '|'.join(patterns) + ')'

# parse the input
block, code = open(fn).read().split('\n\n')
rules = {}
for line in block.split('\n'):
    index, rule = line.split(': ')
    if rule.startswith('"'):
        rule = rule[1]
    rules[int(index)] = rule

# build the regex
expanded = expand(rules, 0)
regex = re.compile(expanded)

count = 0
for line in code.split('\n'):
    m = regex.fullmatch(line)
    if m:
        count += 1
print(count)