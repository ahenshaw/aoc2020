used = set()
def p0(x):
    used.add(0)
    return p11(p8(x))

def p1(x):
    used.add(1)
    if x=='$': return ''
    if x.startswith('a'):
        return x[1:]
    else:
        raise ValueError

def p2(x):
    used.add(2)
    try:
        return p24(p1(x))
    except ValueError:
        return p4(p14(x))

def p3(x):
    used.add(3)
    try:
        return p14(p5(x))
    except ValueError:
        return p1(p16(x))

def p4(x):
    used.add(4)
    return p1(p1(x))

def p5(x):
    used.add(5)
    try:
        return p14(p1(x))
    except ValueError:
        return p1(p15(x))

def p6(x):
    used.add(6)
    try:
        return p14(p14(x))
    except ValueError:
        return p14(p1(x))

def p7(x):
    used.add(7)
    try:
        return p5(p14(x))
    except ValueError:
        return p21(p1(x))

def p8(x):
    used.add(8)
    try:
        return p42(x)
    except ValueError:
        return p8(p42(x))

def p9(x):
    used.add(9)
    try:
        return p27(p14(x))
    except ValueError:
        return p26(p1(x))

def p10(x):
    used.add(10)
    try:
        return p14(p23(x))
    except ValueError:
        return p1(p28(x))

def p11(x):
    used.add(11)
    try:
        return p31(p42(x))
    except ValueError:
        return p31(p11(p42(x)))

def p12(x):
    used.add(12)
    try:
        return p14(p24(x))
    except ValueError:
        return p1(p19(x))

def p13(x):
    used.add(13)
    try:
        return p3(p14(x))
    except ValueError:
        return p12(p1(x))

def p14(x):
    used.add(14)
    if x=='$': return ''
    if x.startswith('b'):
        return x[1:]
    else:
        raise ValueError

def p15(x):
    used.add(15)
    try:
        return p1(x)
    except ValueError:
        return p14(x)

def p16(x):
    used.add(16)
    try:
        return p1(p15(x))
    except ValueError:
        return p14(p14(x))

def p17(x):
    used.add(17)
    try:
        return p2(p14(x))
    except ValueError:
        return p7(p1(x))

def p18(x):
    used.add(18)
    return p15(p15(x))

def p19(x):
    used.add(19)
    try:
        return p1(p14(x))
    except ValueError:
        return p14(p14(x))

def p20(x):
    used.add(20)
    try:
        return p14(p14(x))
    except ValueError:
        return p15(p1(x))

def p21(x):
    used.add(21)
    try:
        return p1(p14(x))
    except ValueError:
        return p14(p1(x))

def p22(x):
    used.add(22)
    return p14(p14(x))

def p23(x):
    used.add(23)
    try:
        return p1(p25(x))
    except ValueError:
        return p14(p22(x))

def p24(x):
    used.add(24)
    return p1(p14(x))

def p25(x):
    used.add(25)
    try:
        return p1(p1(x))
    except ValueError:
        return p14(p1(x))

def p26(x):
    used.add(26)
    try:
        return p22(p14(x))
    except ValueError:
        return p20(p1(x))

def p27(x):
    used.add(27)
    try:
        return p6(p1(x))
    except ValueError:
        return p18(p14(x))

def p28(x):
    used.add(28)
    return p1(p16(x))

def p31(x):
    used.add(31)
    try:
        return p17(p14(x))
    except ValueError:
        return p13(p1(x))

def p42(x):
    used.add(42)
    try:
        return p14(p9(x))
    except ValueError:
        return p1(p10(x))

