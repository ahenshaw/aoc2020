from math import radians, sin, cos, degrees, atan2, sqrt
fn = 'input.txt'

def part1():
    facing = 0
    x, y = (0, 0)
    for line in open(fn):
        cmd = line[0]
        num = int(line[1:])
        if cmd == 'N': y += num
        if cmd == 'S': y -= num
        if cmd == 'E': x += num
        if cmd == 'W': x -= num
        if cmd == 'L': facing += num
        if cmd == 'R': facing -= num
        if cmd == 'F':
            x += cos(radians(facing)) * num
            y += sin(radians(facing)) * num
    print('Part 1:', abs(x) + abs(y))

def part2():
    wx, wy = (10, 1)
    x, y   = (0, 0)
    for line in open(fn):
        cmd = line[0]
        num = int(line[1:])
        if cmd == 'N': wy += num
        if cmd == 'S': wy -= num
        if cmd == 'E': wx += num
        if cmd == 'W': wx -= num
        if cmd == 'L': 
            theta = degrees(atan2(wy, wx)) + num
            magnitude = sqrt(wx*wx + wy*wy)
            wx = magnitude * cos(radians(theta))
            wy = magnitude * sin(radians(theta))
        if cmd == 'R': 
            theta = degrees(atan2(wy, wx)) - num
            magnitude = sqrt(wx*wx + wy*wy)
            wx = magnitude * cos(radians(theta))
            wy = magnitude * sin(radians(theta))
        if cmd == 'F':
            x += wx * num
            y += wy * num
    print('Part 2:', abs(x)+abs(y))

part1()
part2()


