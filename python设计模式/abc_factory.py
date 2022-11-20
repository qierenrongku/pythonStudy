# _*_ coding:utf-8 _*_
'''
@File       :abc_factory.py
@Time       :2022/11/20 20:42
@Author     :且任荣枯
@Version    :1.0

'''
from abc import ABCMeta,abstractmethod

class Apple():
    def buy_fruit(self):
        print("买了苹果")

class Orange():
    def buy_fruit(self):
        print("买了橘子")

class Tea():
    def buy_drink(self):
        print("买了茶")

class NaiTea():
    def buy_drink(self):
        print("买了奶茶")

class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def support_fruit(self):
        pass

    @abstractmethod
    def support_drink(self):
        pass

# 奶茶店
class NaiTeaShop(AbstractFactory):
    def support_drink(self):
        return NaiTea()

    def support_fruit(self):
        return Apple()

# 茶馆
class TeaShop(AbstractFactory):
    def support_drink(self):
        return Tea()

    def support_fruit(self):
        return Apple()

if __name__=="__main__":
    NaiTeaShop().support_fruit().buy_fruit()
    NaiTeaShop().support_drink().buy_drink()

    TeaShop().support_fruit().buy_fruit()
    TeaShop().support_drink().buy_drink()



