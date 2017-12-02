#!/usr/bin/env python3

import sys

chksum = 0
for line in sys.stdin:
    numbers = [int(n) for n in line.strip().split()]
    chksum += max(numbers) - min(numbers)
print(chksum)
