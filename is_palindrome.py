# -*- coding: utf-8 -*-
'''
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
请利用filter()筛选出回数：
'''
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return n

output = filter(is_palindrome, range(1, 200))
print(list(output))