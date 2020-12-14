from cellular_automaton import CellularAutomaton, MooreNeighborhood, EdgeRule

fn = 'input.txt'
# fn = 'test.txt'

class AoC11(CellularAutomaton):
    def __init__(self, data):
        rows = len(data)
        cols = len(data[0])
        self.data = data
        super().__init__(dimension=[rows, cols],
                         neighborhood=MooreNeighborhood(EdgeRule.IGNORE_MISSING_NEIGHBORS_OF_EDGE_CELLS))

    def init_cell_state(self, coordinate):
        row, col = coordinate
        return self.data[row][col]

    def evolve_rule(self, seat, neighbors):
        new_seat = seat
        if seat == 'L' and '#' not in neighbors:
            new_seat = '#'
        if seat == '#' and neighbors.count('#') >= 4:
            new_seat = 'L'
        return new_seat

    def get_state(self):
        return [cell.state for (_, cell) in self.cells.items()]

if __name__ == "__main__":
    grid =  [list(line.strip())  for line in  open(fn)]

    ca = AoC11(grid)
    last_state = ca.get_state()
    while True:
        ca.evolve(1)
        state = ca.get_state()
        if state == last_state:
            break
        last_state = state
    print(state.count('#'))

