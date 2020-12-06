required = set('byr iyr eyr hgt hcl ecl pid'.split())

def validate(fields):
    if not 1920 <= int(fields['byr']) <= 2002: return False
    if not 2010 <= int(fields['iyr']) <= 2020: return False
    if not 2020 <= int(fields['eyr']) <= 2030: return False

    if fields['ecl'] not in 'amb blu brn gry grn hzl oth'.split(): return False
    if len(fields['pid']) != 9: return False

    height = int(fields['hgt'][:-2])
    units  = fields['hgt'][-2:]
    if units == 'cm':
        if not (150 <=height <= 193): return False
    elif units == 'in': 
        if not (59 <=height <= 76): return False
    else: return False

    hcl = fields['hcl']
    if hcl[0] != '#': return False
    for c in hcl[1:]:
        if c not in '0123456789abcdef': return False

    return True

##### Load data ####
data = open('input.txt').read()
data = data.split('\n\n')

##### Part 1 #####
count = 0
for passport in data:
    pairs = passport.split()
    fields = set([x.split(':')[0] for x in pairs])
    count +=  not(required - fields)
print('Part 1:', count)

# ##### Part 2 #####
count = 0
for passport in data:
    pairs  = passport.split()
    fields = dict([x.split(':') for x in pairs])
    keys   = set(fields)
    if not(required - keys):
        count += validate(fields)

print('Part 2:', count)