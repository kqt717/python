#!/usr/bin/python
#coding:utf-8

def test():
    print "we are in %s" % __name__

if __name__ == '__main__':  #仅供自己文件执行时，才执行if下面的代码
    test()