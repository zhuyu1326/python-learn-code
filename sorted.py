# -*- coding: utf-8 -*-
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L1 = sorted(L, key = lambda x: x[0])
L2 = sorted(L, key = lambda x: x[1])

print(L1)
print(L2)