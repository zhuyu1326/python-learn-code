# -*- coding: utf-8 -*-
'''
利用闭包返回一个计数器函数，每次调用的时候返回递增整数
'''
def createCounter():
    L = [0]
    def counter():
        L[0] += 1
        return L[0]

    return counter 

a = createCounter()
print(a(), a(), a(), a(), a())