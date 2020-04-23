#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Student(object):
    count = 0 #count是类属性

    def __init__(self, name):
        self.name = name #添加name属性
        Student.count += 1 #def每执行一次，count加1
                            #即实现统计学生人数


if Student.count != 0:
    print('测试失败')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败')
    else:
        lisa = Student('Lisa')
        if Student.count != 2:
            print('测试失败！')
        else:
            print('Students:', Student.count)
            print('测试通过！')
