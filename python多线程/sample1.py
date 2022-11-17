# _*_ coding:utf-8 _*_
'''
@File       :sample1.py
@Time       :2022/8/7 18:27
@Author     :且任荣枯
@Version    :1.0

'''

from time import sleep

def sing():
    for i in range(3):
        print(f"正在唱歌{i}")
        sleep(1)
def dance():
    for i in range(3):
        print(f"正在跳舞{i}")
        sleep(1)

if __name__ =='__main__':
    sing()
    dance()
