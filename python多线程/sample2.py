# _*_ coding:utf-8 _*_
'''
@File       :sample2.py
@Time       :2022/8/7 18:32
@Author     :且任荣枯
@Version    :1.0

'''
#多进程支持的是multiprocessing 和 subprocess

from multiprocessing import Process
def run_proc():
    print("子进程-------------")

if __name__=='__main__':
    print("主进程")
    p=Process(target=run_proc)
    p.start()