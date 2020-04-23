#!usr/bin/python3
# -*- coding: utf-8 -*-
'''
请利用@property给一个Screen对象加上width和height属性，
以及一个只读属性resolution：
'''

class Screen(object):
    @property
    def width(self):    #定义一个getter方法
        return self._width
    @width.setter
    def width(self, width):     #定义一个getter方法
        if not isinstance(width, int):
            raise ValueError('请输入整数')
        else:
            self._width = width

    @property
    def height(self):   #定义一个getter方法
        return self._height
    @height.setter
    def height(self, height):   #定义一个setter方法
        if not isinstance(height, int):
            raise ValueError('请输入整数')
        else:
            self._height = height

    @property
    def resolution(self):   #定义一个getter方法，当只定义getter无定义
                            #setter，则为只读属性
        return self._width * self._height



s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过')
else:
    print('测试失败')
