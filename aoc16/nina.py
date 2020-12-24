fn = 'fields.txt'

program = open(fn).readlines()

#list of lists for different ranges
data_fields=[]
for line in program:
    field, values = line.split(': ')
    values = values
    ranges = values.strip().replace('-', ' ').split(' ')
    data_fields.append(ranges[0:2])
    data_fields.append(ranges[3:5])

print(data_fields)

data_fields=[]
for line in program:
    field, values = line.split(': ')
    groups = values.split(' or ')
    for group in groups:
        rng = [int(x) for x in group.split('-')]
        data_fields.extend(list(range(rng[0], rng[1]+1)))
        
data_fields = set(data_fields)
print(data_fields)


fn2='nearby_tickets.txt'

nearby_tickets = open(fn2).readlines()

#list of lists for different tickets
tickets=[]
for line in nearby_tickets:
    ticket = line.strip().split(',')
    tickets.append(ticket)
    
print(tickets)

#Checking if each value of ticket falls in field ranges
invalids=[]

for i in tickets:
    print('ticket:', i)
    for j in i:
        print('   item:', j)
        for r in data_fields:
            if int(r[0]) <= int(j) <= int(r[1]):
                continue
            else:
                invalids.append(int(j))
print(invalids)

#Counting invalids, if all fields(40) invalid then keep
final=[]
for k in invalids:
    if invalids.count(k)==40:
        final.append(k)
print(final)

#Get unique invalids
final_set = set(final)

#Finding error rate
print(sum(final_set))
