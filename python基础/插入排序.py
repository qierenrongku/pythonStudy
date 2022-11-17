# _*_ coding:utf-8 _*_
'''
@File       :插入排序.py
@Time       :2022/8/2 22:38
@Author     :且任荣枯
@Version    :1.0

'''
#插入排序
def insert_sort(list):
    for j in range(len(list)):
        for i in range(0,j):
            if list[j]<list[i]:
                list[j], list[i] =list[i],list[j]
    return  list





blist=[7,3,9,6,44,33,92,11,23,44,53,54,64,234,562,22,62]
# print(select_sort(blist))
print(insert_sort(blist))