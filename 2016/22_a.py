#!/usr/bin/env python3

import re, sys
from itertools import combinations

node_regex = re.compile(r'/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T.*$')
matrix = {}
viable_nodes = 0

for line in sys.stdin:
    m = node_regex.match(line)
    if m:
      pos = m.group(1, 2)
      # (total, used, avail)
      val = m.group(3, 4, 5)
      matrix[pos] = val
for a, b in combinations(matrix, 2):
    viable_nodes += 1
    if viable_nodes > 10: break
