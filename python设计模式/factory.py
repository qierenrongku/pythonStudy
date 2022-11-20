# _*_ coding:utf-8 _*_
'''
@File       :factory.py
@Time       :2022/11/20 20:29
@Author     :且任荣枯
@Version    :1.0

'''
from abc import ABCMeta,abstractmethod

class Fruit():
    def buy(self):
        print("买水果")

class Drink():
    def buy(self):
        print("买饮料")

# 抽象工厂
class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def support_commodity(self):
        pass

# Fruity 工厂
class FruitFactory(AbstractFactory):
    def support_commodity(self):
        return Fruit()

# Drink 工厂
class DrinkFactory(AbstractFactory):
    def support_commodity(self):
        return Drink()


if __name__ == "__main__":
    FruitFactory().support_commodity().buy()
    DrinkFactory().support_commodity().buy()
