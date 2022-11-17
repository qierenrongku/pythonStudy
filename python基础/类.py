# _*_ coding:utf-8 _*_
'''
@File       :类.py
@Time       :2022/7/30 23:09
@Author     :且任荣枯
@Version    :1.0

'''
class MyClass():
    pass


# print(MyClass)#<class '__main__.MyClass'>
# a=MyClass()
# print(isinstance(a, MyClass))
# a.name = "xxx"
# print(a.name)
#
# class Person :
#     name = "xxx" #实例变量
#     def sayHi(self):
#         print(locals())
#         print("hi")

p1=Person()
p2=Person()
p1.name="222"

# 一样
# print(p1)
# print(p1.sayHi())



# print(p1.name,p2.name)
# p1.sayHi()
# p2.sayHi()


class Person:
    name=""
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print(f"hello{1}",self.name)

class Dog:
    name="dog"
    age=0
    gender="公"
    height=0.6

    def __init__(self,name,age,gender,height) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.gender=gender

    def jiao(self):
        print(f"{self.name}在叫")
    def yao(self):
        print(f"{self.name}在咬")
    def run(self):
        print(f"{self.name}在跑")







