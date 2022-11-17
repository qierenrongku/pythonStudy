# _*_ coding:utf-8 _*_
'''
@File       :simple_factory.py
@Time       :2022/11/18 0:23
@Author     :且任荣枯
@Version    :1.0

'''

class Fruit():
    def buy(self,money):
        print(f"买了{money}的水果")

class Drink():
    def buy(self,money):
        print(f"买了{money}的饮料")

class Snake():
    def buy(self,money):
        print(f"买了{money}的零食")

class Shop:
    def support_commodity(self,need):
        if need == "fruit":
            return Fruit()
        elif need == "drink":
            return Drink()
        elif need == "Snake":
            return Snake()
        else:
            raise TypeError(f"没有{need}这类商品")


if __name__ == "__main__":
    fruit = Fruit().buy(100)
    drink = Drink().buy(100)
    snake = Snake().buy(100)

    shop = Shop()
    need = shop.support_commodity("fruit")
    need.buy(100)