# parse the input dat
program = open('input.txt').readlines()

def run(program):
    ip = 0
    acc = 0
    done = set()
    flag = False
    while True:
        if ip in done:  
            break
        done.add(ip)
        try:
            ins = program[ip]
        except IndexError:
            return ip, acc, True
        op, offset = ins.split()
        offset = int(offset)
        if op == 'nop':
            ip += 1
        elif op == 'acc':
            ip += 1
            acc += offset
        elif op == 'jmp':
            ip += offset
    return(ip, acc, flag)


ip, acc, flag = run(program)
print('Part 1:', acc)

for i, line in enumerate(program):
    newp = program[:]
    if line.startswith('nop'):
        newp[i] = newp[i].replace('nop', 'jmp')
    elif line.startswith('jmp'):
        newp[i] = newp[i].replace('jmp', 'nop')
    else:
        continue
    ip, acc, flag = run(newp)
    if flag:
        break
    
    
print('Part 2:', acc)