import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
# parse the input data
cm = {}
for rule in open('test.txt'):
    left, right = rule.strip().split('contain')
    adjective, color, noun = left.split()
    parent = f'{adjective} {color}'
    cm[parent]=color
    G.add_node(parent)
    for item in right.split(', '):
        if 'no other' in item:
            continue
        count, adjective, color, noun = item.strip().split()
        count = int(count)
        child = f'{adjective} {color}'
        G.add_node(child)
        cm[child] = color
        G.add_edge(parent, child)

TARGET = 'shiny gold'
pos = nx.circular_layout(G, scale=2)
colors =  [cm[x] for x in G.nodes()]
pos[TARGET] = [0.0, 0.0]

fig, ax = plt.subplots()
nx.draw(G, with_labels=True, pos=pos, node_size=6000, font_size=10, node_color=colors)
fig.set_facecolor('beige')
plt.show()

print(len(nx.dfs_tree(G.reverse(), source=TARGET).nodes()) - 1)

# find_parents(TARGET, outer)
# print('Part 1:', len(outer))

# total = find_children(TARGET)
# print('Part 2:', total-1)