# _*_ coding:utf-8 _*_
'''
@File       :adapter.py
@Time       :2022/11/21 22:40
@Author     :且任荣枯
@Version    :1.0

'''
from abc import ABC,ABCMeta,abstractmethod
#
# class FlyAnimal(metaclass=ABCMeta):
#     @abstractmethod
#     def fly(self):
#         pass
#
#     def run(self):
#         pass
#
# class Bird(FlyAnimal):
#     def fly(self):
#         print("鸟在飞")
#     def run(self):
#         print("鸟在跑")
#
# class Dog:
#     def run(self):
#         print("狗在跑")
#
# class AnimalAdapter(Dog,FlyAnimal):
#     def __init__(self):
#         self.dog = Dog()
#     def fly(self):
#         print("我也能飞了")
#
#
# AnimalAdapter().fly()
# AnimalAdapter().run()
# AnimalAdapter().dog.run()

class FlyAnimal(ABC):
    @abstractmethod
    def fly(self):
        pass

    def run(self):
        pass

class Bird(FlyAnimal):
    def fly(self):
        print("鸟在飞")
    def run(self):
        print("鸟在跑")

class Dog:
    def run(self):
        print("狗在跑")

class AnimalAdapter(FlyAnimal):
    def __init__(self):
        self.dog = Dog()
    def fly(self):
        print("我也能飞了")
    def run(self):
        self.dog.run()

AnimalAdapter().fly()
AnimalAdapter().run()
AnimalAdapter().dog.run()