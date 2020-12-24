from cellular_automaton import CellularAutomaton, MooreNeighborhood, EdgeRule

fn = 'input.txt'
# fn = 'test.txt'

class AoC17(CellularAutomaton):
    def __init__(self, data, cols, rows, depth, padding):
        self.data = data
        self.padding =  padding
        super().__init__(dimension=[cols, rows, depth],
                         neighborhood=MooreNeighborhood(EdgeRule.IGNORE_MISSING_NEIGHBORS_OF_EDGE_CELLS))

    def init_cell_state(self, coordinate):
        x, y, z = coordinate
        xx = x - self.padding
        yy = y - self.padding
        if z == self.padding:
            if xx < 0 or yy < 0:
                c = '.'
            else:
                try:
                    c = self.data[xx][yy]
                except IndexError:
                    c = '.'
        else:
            c = '.'
        return c

    def evolve_rule(self, cube, neighbors):
        new_cube = cube
        if cube == '#':
            if 2 <= neighbors.count('#') <= 3:
                new_cube = '#'
            else:
                new_cube = '.'
        elif neighbors.count('#') == 3:
            new_cube = '#'
        return new_cube

    def get_state(self):
        return [cell.state for (_, cell) in self.cells.items()]

    def pp(self):
        state = self.get_state()
        cols, rows, _ = self.dimension
        span = cols * rows
        for i in range(0, len(state), span):
            print(i//span)
            block = state[i:i+span]
            for j in range(0, len(block), cols):
                print(''.join(block[j:j+cols]))


if __name__ == "__main__":
    ''' The grid starts with depth=1 and rows, cols based on input size. 
        In each cycle, the grid could grow by 2 in each dimension.'''

    CYCLES = 6
    grid =  [list(line.strip())  for line in  open(fn)]
    rows = len(grid) + 2 * CYCLES
    cols = len(grid[0]) + 2 * CYCLES
    depth = 1 + 2 * CYCLES

    ca = AoC17(grid, cols, rows, depth, CYCLES)
    # ca.pp()
    # print('______')
    for i in range(CYCLES):
        ca.evolve(1)
        # ca.pp()
    print(ca.get_state().count('#'))

