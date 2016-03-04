#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：统计 1 到 100 之和。

程序分析：无
'''
tmp = 0
for i in range(1,101):  #range()第一个下标默认是从0开始的，而且不包括最后一位，所以这里指定了从1开始，并且末位是101
    tmp += i
print 'The sum is %d' % tmp