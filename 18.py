#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

程序分析：关键是计算出每一项的值。
'''
Tn = 0
Sn = []
n = int(raw_input('n = :\n'))       #控制相加的个数
a = int(raw_input('a = :\n'))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x,y : x + y,Sn)
print Sn

'''
python中的reduce
   python中的reduce内建函数是一个二元操作函数，他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
如：
    def myadd(x,y):
        return x+y
    sum=reduce(myadd,(1,2,3,4,5,6,7))
    print sum

#结果就是输出1+2+3+4+5+6+7的结果即28
当然，也可以用lambda的方法，更为简单：
    sum=reduce(lambda x,y:x+y,(1,2,3,4,5,6,7))
    print sum

在python 3.0.0.0以后, reduce已经不在built-in function里了, 要用它就得from functools import reduce.
'''