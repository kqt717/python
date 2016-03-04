#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。

程序源代码：
'''

from sys import stdout
for i in range(4):
    for j in range(2 - i + 1):
        stdout.write('+')
    for k in range(2 * i + 1):
        stdout.write('*')           #输出*号， for 只是控制输出几个*号而已
    print

'''
for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print
'''