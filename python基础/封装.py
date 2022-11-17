# _*_ coding:utf-8 _*_
'''
@File       :封装.py
@Time       :2022/7/31 21:34
@Author     :且任荣枯
@Version    :1.0

'''

class Rectangle:

    def __init__(self,width,height):
        self.__width = width  #__width--->_Rectangle__width
        self._height= height
    def get_width(self):
        return self.__width
    def get_height(self):
        return self._height
    def set_width(self,width):
        self.__width=width
    def set_height(self,height):
        self._height=height

    def get_area(self):
        return self.width*self.height

# r= Rectangle(2,5)
# print(r.get_area())
# r.set_width(3)
# r.set_height(4)
# print(r.get_area())

class Person:

    def __init__(self,name):
        self._name=name

    @property  #装饰器 将get方法转化为对象属性
    def name(self):
        return self._name


    @name.setter
    def name(self,name):
        self._name=name


p=Person("张三")
print(p.name)
p.name="李四"
print(p.name)
