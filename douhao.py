#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
假定有下面这样的列表：
spam = ['apples', 'bananas', 'tofu', 'cats']
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所
有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入and。例如，将
前面的spam 列表传递给函数，将返回'apples, bananas, tofu, and cats'。但你的函数应
该能够处理传递给它的任何列表。
'''
def comma(someParameter):
    i = 0
    tempstr = someParameter[0]
    for i in range(len(someParameter)):
        if i == 0:
            tempstr = tempstr
        elif i == len(someParameter) - 1:
            tempstr = tempstr + ', and' + someParameter[i]
        else:
            tempstr = tempstr + ', ' + someParameter[i]

    print(tempstr)


a = ['apples', 'bananas', 'tofu', 'cats']

comma(a)
