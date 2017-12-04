#!/usr/bin/env python3

import re, sys
from itertools import permutations

node_regex = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T.*$')
matrix = {}
viable_nodes = 0

for line in sys.stdin:
    m = node_regex.match(line)
    if m:
      pos = tuple([int(n) for n in m.group(1, 2)])
      # (total, used, avail)
      val = tuple([int(n) for n in m.group(3, 4, 5)])
      matrix[pos] = val
for a, b in permutations(matrix, 2):
    if matrix[a][3] == 0:
        continue
    if matrix[a][1] <= matrix[b][2]:
        print(matrix[a], matrix[b])
        viable_nodes += 1
print(viable_nodes)
