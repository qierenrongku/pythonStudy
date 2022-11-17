# _*_ coding:utf-8 _*_
'''
@File       :priorityQueue.py
@Time       :2022/9/22 22:04
@Author     :且任荣枯
@Version    :1.0

'''
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
