fn = 'C:/Users/ninag/OneDrive - Kennesaw State University/Documents/Advent Code/Day8/test.txt'
fn = 'input.txt'

program = open(fn).readlines()

data=[]
for line in program:
    instruction, counter = line.split()
    counter = int(counter)
    data.append((instruction, counter))
    

def play(data):
    
   executed=[]
   posit=0
   accum=0
   accumulated=[]

   while posit not in executed and posit<len(data):
        executed.append(posit)
    
        (instruction, counter) = data[posit][0], data[posit][1]    
        if instruction=='acc':
            posit +=1
            accum +=counter
            accumulated.append(counter)
        elif instruction=='jmp':
            posit +=counter
        elif instruction=='nop':
            posit +=1
   
   return(accum, posit in executed) 

acc, flag = play(data)
print(acc)