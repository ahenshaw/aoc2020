from collections import defaultdict

#Creating dictonary
containers = defaultdict(set)
for line in open('C:/Users/ninag/OneDrive - Kennesaw State University/Documents/Advent Code/Day7/test.txt'):
    left, right = line.split(' contain ')
    if 'no other' in right:
        continue

    outer_style = str.join(' ', left.split()[:2])
    print(outer_style)

    for item in right.split(', '):
        count, adjective, color, noun = item.split()
        inner_style = (f'{adjective} {color}')
        print('   ', inner_style)
       
        containers[inner_style].add(outer_style)
             
#Finding number of bags that contain shiny gold
parents = set()
def recursive_fn(containers, inner_bag):
    for x in containers[inner_bag]:
        parents.add(x)
        recursive_fn(containers, x)
               
recursive_fn(containers, 'shiny gold')
print(len(parents))       

