#! /bin/env python3

import sys

for line in sys.stdin:
    numbers  = [int(d) for d in line.strip()]
    numbers_length = len(numbers)
    total_sum = 0
    for pos, number in enumerate(numbers):
        look_ahead_number = numbers[(pos + (numbers_length // 2)) % numbers_length]
        if number == look_ahead_number:
            total_sum += number
    print(total_sum)
