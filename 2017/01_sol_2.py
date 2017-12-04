#! /bin/env python3

import sys

for number in sys.stdin:
    number = number.strip() + number[0] 
    total_sum = 0
    last_digit = None
    for digit in (int(d) for d in number):
        if digit == last_digit:
            total_sum += digit
        last_digit = digit
    print(total_sum)
