fn = "input.txt"
# fn = "test.txt"
import numpy as np
from collections import Counter

def match(ref, ident):
    matches = []
    for i in range(16):
        other = ident[i]
        n = ref[0] == other[1]
        s = ref[1] == other[0]
        e = ref[2] == other[3]
        w = ref[3] == other[2]
        results = (n, s, e, w)
        if any(results):
            matches.append((i, results))
    return matches

def xform(tile, n):
    ud = n & 1
    lr = (n >> 1) & 1
    rot = (n >> 2) 
    tile = np.rot90(tile, rot)
    if lr:
        tile = np.fliplr(tile)
    if ud:
        tile = np.flipud(tile)
    return tile

def fingerprint(tile):
    m = np.array([512, 256, 128, 64, 32, 16, 8, 4, 2, 1], dtype=int)
    n = np.sum(m * tile[0])
    s = np.sum(m * tile[-1])
    e = np.sum(m * tile[:,-1])
    w = np.sum(m * tile[:,0])
    return n, s, e, w

# parse the data
data = open(fn).read().split('\n\n')
tiles = {}
identities = {}
for image in data:
    image = image.replace('.', '0').replace('#', '1')
    lines = image.split('\n')
    tile_id = int(lines[0][5:-1])
    tile = []
    for line in lines[1:]:
        tile.append([int(x) for x in line])
    tile = np.array(tile, dtype=int)
    tiles[tile_id] = tile
    ident = []
    for i in range(16):
        x = xform(tile, i)
        f = fingerprint(x)
        ident.append(f)
    identities[tile_id] = ident

keys = list(tiles)
prod = 1
for i in keys:
    matchers = []
    ref = identities[i][0]
    # print(i)
    for j in keys:
        if i != j:
            other = identities[j]
            m = match(ref, other)
            if m:
                # print('    ', j, m)
                matchers.append(m)
    if len(matchers) == 2:
        print(i)
        prod *= i
print('Answer:', prod)

    



    



