fn = "input.txt"
# fn = "test.txt"

def parse(s):
    for operator in ["*-","+/"]:
        depth = 0
        for p in range(len(s) - 1, -1, -1):
            if s[p] == ')': depth += 1
            if s[p] == '(': depth -= 1
            if not depth and s[p] in operator:
                return [s[p]] + parse(s[:p]) + parse(s[p+1:])
    s = s.strip()
    if s[0] == '(':
        return parse(s[1:-1])
    return [s]

def rpn(eqn):
    stack = []
    for token in reversed(eqn):
        if token in '+-*/':
            a = stack.pop()
            b = stack.pop()
            stack.append(eval(f'{a} {token} {b}'))
        else:
            stack.append(int(token))
    return stack[0]

total = 0
for line in open(fn):
    total += rpn(parse(line))
print(total)
