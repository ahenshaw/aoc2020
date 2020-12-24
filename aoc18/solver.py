import tokenize
fn = "input.txt"
# fn = "test.txt"

def part1(fn):
    total = 0
    with open(fn, 'rb') as f:
        tokens = tokenize.tokenize(f.readline)
        stack = []
        opstack = []
        op = None
        for token in tokens:
            if token.type == tokenize.NUMBER:
                stack.append(int(token.string))
            elif token.type == tokenize.OP:
                c = token.string
                if c == '(':
                    stack.append(c)
                elif c == ')':
                    temp = stack.pop()
                    stack.pop()
                    stack.append(temp)
                else:
                    opstack.append(c)
            elif token.type==tokenize.NEWLINE:
                total += stack[0]
                stack = []
                op = None
            if opstack and len(stack) >= 2 and stack[-1] != '(' and stack[-2] != '(':
                op = opstack.pop()
                b = stack.pop()
                a = stack.pop()
                stack.append(eval(f'{a} {op} {b}'))
            # print(token.string, stack)
    print(total)




def part2(data):
    pass

# parse the data
data = []
for line in open(fn):
    data.append(line)

part1(fn)

part2(data)
