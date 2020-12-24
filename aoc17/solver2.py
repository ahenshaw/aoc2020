from copy import deepcopy

fn = "input.txt"
# fn = "test.txt"

def part1(data):
    pass

def part2(data):
    pass

class Grid:
    def __init__(self):
        self.g = {}
        self.min_x = 100000
        self.max_x = -100000
        self.min_y = 100000
        self.max_y = -100000
        self.min_z = 100000
        self.max_z = -100000
        self.min_w = 100000
        self.max_w = -100000

    def set(self, x, y, z, w, c):
        # if c == '#':
        self.min_x = min(self.min_x, x-1)
        self.min_y = min(self.min_y, y-1)
        self.min_z = min(self.min_z, z-1)
        self.min_w = min(self.min_w, w-1)

        self.max_x = max(self.max_x, x+1)
        self.max_y = max(self.max_y, y+1)
        self.max_z = max(self.max_z, z+1)
        self.max_w = max(self.max_w, w+1)
        self.g[x,y,z, w] = c
    
    def get(self, x, y, z, w):
        try:
            return self.g[x, y, z, w]
        except KeyError:
            return '.'

    def neighbors(self, x, y, z, w):
        cells = []
        for u in range(-1, 2):
            for v in range(-1, 2):
                for wz in range(-1, 2):
                    for ww in range(-1, 2):
                        if (u,v,wz,ww) != (0, 0, 0, 0):
                            x1 = x + u
                            y1 = y + v
                            z1 = z + wz
                            w1 = w + ww
                            c = self.get(x1, y1, z1, w1)
                            if c == '#':
                                cells.append(c)
        return cells

    def iter(self):
        for w in range(self.min_w, self.max_w+1):
            for z in range(self.min_z, self.max_z+1):
                for y in range(self.min_y, self.max_y+1):
                    for x in range(self.min_x, self.max_x+1):
                        yield x, y, z, w

    def print(self):
        for z in range(self.min_z, self.max_z):
            print('\nz=', z-1000)
            for y in range(self.min_y, self.max_y):
                line = []
                for x in range(self.min_x, self.max_x):
                    line.append(self.get(x, y, z))
                print(''.join(line))
                    
# parse the data
grid = Grid()
z = 0
w = 0
for y, line in enumerate(open(fn)):
    for x, c in enumerate(line):
        grid.set(x+1000, y+1000, z+1000, w+1000, c)

for i in range(6):
    newgrid = deepcopy(grid)
    for (x, y, z, w) in grid.iter():
        c = grid.get(x, y, z, w)
        n = grid.neighbors(x, y, z, w)
        if c=='#':
            if 2 <= n.count('#') <= 3:
                newcell = '#'
            else:
                newcell = '.'
        else:
            if n.count('#') == 3:
                newcell = '#'
            else:
                newcell = '.'
        newgrid.set(x, y, z, w, newcell)

    grid = newgrid
    # print('-----------------')
    # grid.print()

count = 0
for x, y, z, w in grid.iter():
    count += grid.get(x, y, z, w) == '#'
print(count)
