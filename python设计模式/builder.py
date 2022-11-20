# _*_ coding:utf-8 _*_
'''
@File       :builder.py
@Time       :2022/11/20 23:53
@Author     :且任荣枯
@Version    :1.0

'''
from abc import ABCMeta, abstractmethod

class Computer:
    def __init__(self):
        self.monitor = None
        self.cpu = None
        self.keyboard = None
        self.chassis = None
    def __str__(self):
        return f"{self.cpu},{self.monitor},{self.chassis},{self.keyboard}"

class ComputerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_monitor(self):
        pass

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_keyboard(self):
        pass

    @abstractmethod
    def build_chassis(self):
        pass

class HuaWeiComputer(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.cpu = "I9"

    def build_monitor(self):
        self.computer.monitor = "京东方"

    def build_chassis(self):
        self.computer.chassis = "华硕"

    def build_keyboard(self):
        self.computer.keyboard = "联想"

class AppleComputer(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.cpu = "M1"

    def build_monitor(self):
        self.computer.monitor = "三星"

    def build_chassis(self):
        self.computer.chassis = "自产"

    def build_keyboard(self):
        self.computer.keyboard = "双飞燕"

class ComputerDirector:
    def build_computer(self, builder):
        builder.build_cpu()
        builder.build_chassis()
        builder.build_monitor()
        builder.build_keyboard()
        return builder.computer

if __name__ == "__main__":
    builder = AppleComputer()
    computer_director = ComputerDirector()
    print(computer_director.build_computer(builder))
    print(computer_director.build_computer(HuaWeiComputer()))
