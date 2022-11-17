# _*_ coding:utf-8 _*_
'''
@File       :二分查找.py
@Time       :2022/8/4 22:13
@Author     :且任荣枯
@Version    :1.0

'''

def tf_search(list,item):
    n = len(list)
    left = 0
    right = n-1

    while left<= right:
        mid = (left + right) // 2
        if list[mid] == item:
            return True
        elif list[mid]>item:
            right =mid-1
        else:
            left =mid+1
    return False


list = [x for x in range(1,10)]
print(tf_search(list, 4))
print(tf_search(list, 14))