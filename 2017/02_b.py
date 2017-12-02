#!/usr/bin/env python3

import itertools,sys

chksum = 0
for line in sys.stdin:
    numbers = [int(n) for n in line.strip().split()]
    combinations = itertools.combinations(numbers, 2)
    for a, b in combinations:
        if a > b:
            if a % b == 0:
                chksum += a // b
                break
        else:
            if b % a == 0:
                chksum += b // a
                break
print(chksum)
