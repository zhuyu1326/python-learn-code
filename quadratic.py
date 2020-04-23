# -*- coding: utf-8 -*-
'''
>>> 请定义一个函数 quadratic(a, b, c)，接收3个参数，
返回一元二次方程 ax^2+bx+c=0 的两个解

NOTE:
求解需要确定判别式 delta (b^2 - 4ac) 的大小:
    当 delta>0 时，方程有两个不相等的实数根；
    当 delta=0 时，方程有两个相等的实数根；
    当 delta<0 时，方程无实数根；
'''
import math
def quadratic(a, b, c):
    delte = b**2 - 4*a*c
    if delte < 0:
        print('此方程无解')
    elif delte == 0:
        #print("改方程有两个相等的解")
        x1 = x2 = (-b) / 2*a
        return x1,x2
    else:
        #print("该方程有两个不同的解")
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2*a
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2*a
        return x1, x2

a = int(input("请输入方程的系数a:"))
b = int(input("请输入方程的系数b:"))
c = int(input("请输入方程的系数c:"))

x = quadratic(a, b, c)
print("方程的解为：", x)