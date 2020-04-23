# -*- coding: utf-8 -*-
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5,
 '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2float(s):
    i = 0
    while s[i] != '.':
        i = i + 1
    p1 = reduce(lambda x, y: 10 * x + y, map(char2num, s[:i]))
    p2 = reduce(lambda x, y: 10 * x + y, map(char2num, s[i+1:])) / (10**(len(s[i:])-1))
    return p1 + p2
print(str2float('123.456'))