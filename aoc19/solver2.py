import re
fn = "input.txt"
fn = "test.txt"

visited = set()

def make_single(group):
    parens = 0
    code = '    return '
    for c in reversed(group.split()):
        code += f'p{c}('
        parens += 1
    code += 'x'+')'*parens
    return code

def make_group(line):
    left, right = line.split(' | ')
    return f'''    try:
    {make_single(left)}
    except ValueError:
    {make_single(right)}

'''

def make_leaf(c):
    return f'''    if x=='$': return ''
    if x.startswith('{c}'):
        return x[1:]
    else:
        raise ValueError

'''

def gen(rules, index):
    code = f'def p{index}(x):\n    used.add({index})\n'
    line = rules[index]
    if not line[0].isdigit():
        return code + make_leaf(line[0])
    elif '|' in line:
        return code + make_group(line)
    else:
        return code + make_single(line)+'\n\n'
    return code

# parse the input
block, code = open(fn).read().split('\n\n')
rules = {}
for line in block.split('\n'):
    index, rule = line.split(': ')
    if rule.startswith('"'):
        rule = rule[1]
    rules[int(index)] = rule

rules[8] = '42 | 42 8'
rules[11] = '42 31 | 42 11 31'

# # build the program
with open('syn.py', 'w') as fh:
    fh.write('used = set()\n')
    for key in sorted(rules):
        fh.write(gen(rules, key))

from syn import p0, used

count = 0
passed = []
for i, line in enumerate(code.split('\n')):
    try:
        leftover = p0(line+'$')
    except ValueError:
        pass
    else:
        if not leftover:
            # print(repr(line))
            # print(f"{i:2} {sorted(used)}")
            passed.append((len(line), line))
            count += 1
print()
print(count)
for l, line in sorted(passed):
    print(f"{l:3} {line}")
