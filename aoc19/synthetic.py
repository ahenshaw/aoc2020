def p0(x):
    return p5(p1(p4(x)))

def p1(x):
    try:
        return p3(p2(x))
    except ValueError:
        return p2(p3(x))

def p2(x):
    try:
        return p4(p4(x))
    except ValueError:
        return p5(p5(x))

def p3(x):
    try:
        return p5(p4(x))
    except ValueError:
        return p4(p5(x))

def p4(x):
    if x.startswith('a'):
        return x[1:]
    else:
        raise ValueError

def p5(x):
    if x.startswith('b'):
        return x[1:]
    else:
        raise ValueError

if __name__ == '__main__':
    print(p0('ababbbb'))



