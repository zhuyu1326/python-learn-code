#!/usr/bin/python3
# -*- coding: utf-8 -*-

'  a test module  '

__author__ = 'Leon Zhu'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello World !')
    elif len(args) == 2:
        print('hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
