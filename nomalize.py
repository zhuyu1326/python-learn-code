# -*- coding: utf-8 -*-
def normalize(c):
        return c.title()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)