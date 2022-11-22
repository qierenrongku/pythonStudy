# _*_ coding:utf-8 _*_
'''
@File       :singleton.py
@Time       :2022/11/21 21:59
@Author     :且任荣枯
@Version    :1.0

'''
# class Singleton:
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance
#
# class Myclass(Singleton):
#     def __init__(self, a):
#         self.a = a
#
# a = Myclass(10)
# b = Myclass(20)
# print(a.a)
# print(b.a)
# print(id(a),id(b))


def singleton(cls, *args, **kw):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class Myclass:
    pass

a = Myclass()
b = Myclass()
print(a,b)
