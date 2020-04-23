# -*- coding: utf-8 -*-
from functools import reduce

def sum(L):
    sum = 0
    for i in L:
        sum = sum + i
    return sum

def f(x, y):
    return x * y

def prod(L):
    return reduce(f, L)

L1 = [3, 5, 7, 9]
print(prod(L1))
print(sum(L1))