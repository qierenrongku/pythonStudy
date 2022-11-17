# _*_ coding:utf-8 _*_
'''
@File       :orderDict.py
@Time       :2022/9/22 22:13
@Author     :且任荣枯
@Version    :1.0

'''
from collections import OrderedDict

d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key in d:
    print(key,d[key])
# a 1
# b 2
# c 3
# d 4

a ={
    'x':1,
    'y':2,
    'z':3
}
b = {
    'w':10,
    'x':11,
    'y':2
}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
# {'y', 'x'}
# {'z'}
# {('y', 2)}