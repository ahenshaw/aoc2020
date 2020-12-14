from time import perf_counter
from itertools import combinations 

fn = 'C:/Users/ninag/OneDrive - Kennesaw State University/Documents/Advent Code/Day9/input.txt'
fn = 'input.txt'
program = open(fn).readlines()

program
start = perf_counter()
data=[]
for line in program:
    number = line.strip('\n')
    number = int(number)
    data.append(number)

for z in range(25,len(data)):
    combn =  set(sum(x) for x in combinations(data[z-25:z],2))
    if not data[z] in combn:
        target = data[z]
print(perf_counter()-start)
print(target)
