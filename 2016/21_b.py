#!/usr/bin/env python3

import re, sys

def swap_position(password, match, reverse=False):
    x, y = [int(n) for n in match.group(1, 2)]
    password[x], password[y] = password[y], password[x]
    return password

def swap_letter(password, match, reverse=False):
    a, b = match.group(1, 2)
    x = password.index(a)
    y = password.index(b)
    password[x], password[y] = password[y], password[x]
    return password

def rotate(password, match, reverse=False):
    direction = match.group(1)
    steps = int(match.group(2)) % len(password)
    if direction == 'right':
        steps = (-1) * steps
    if reverse:
        steps *= -1
    password = password[steps:] + password [:steps]
    return password

def rotate_by_pos(password, match, reverse=False):
    letter = match.group(1)
    index = password.index(letter)
    if reverse:
        # Cheating? fuck math
        revtab = (7, 0, 4, 1, 5, 2, 6, 3)
        f_pos = revtab[index]
        steps = index - f_pos
    else:
        steps = index + 1
        if index >= 4:
            steps += 1
        steps = (-1) * (steps % len(password))
    password = password[steps:] + password [:steps]
    return password

def reverse(password, match, reverse=False):
    x, y = [int(n) for n in match.group(1, 2)]
    substring = password[x:y+1]
    password = password[:x] + substring[::-1] + password[y+1:]
    return password

def move(password, match, reverse=False):
    x, y = [int(n) for n in match.group(1, 2)]
    if reverse:
        x, y = y, x
    password.insert(y, password.pop(x))
    return password

regexes = [
        (re.compile(r'swap position (\d+) with position (\d+)'), swap_position),
        (re.compile(r'swap letter ([a-z]) with letter ([a-z])'), swap_letter),
        (re.compile(r'rotate (left|right) (\d+) steps?'), rotate),
        (re.compile(r'rotate based on position of letter ([a-z])'), rotate_by_pos),
        (re.compile(r'reverse positions (\d+) through (\d+)'), reverse),
        (re.compile(r'move position (\d+) to position (\d+)'), move)
        ]

if __name__ == '__main__':
    password = list('fbgdceah')
    instructions = sys.stdin.readlines()
    for pos, line in enumerate(instructions[::-1]):
        parsed = False
        for regex, action in regexes:
            m = regex.match(line.strip())
            if m:
                password = action(password, m, reverse=True)
                parsed = True
        if parsed == False:
            print('WARNING - No match for line: ', line)
        print(pos, password)
    print(''.join(password))
