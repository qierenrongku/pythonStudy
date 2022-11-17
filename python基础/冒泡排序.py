# _*_ coding:utf-8 _*_
'''
@File       :冒泡排序.py
@Time       :2022/8/2 21:13
@Author     :且任荣枯
@Version    :1.0

'''
#冒泡排序
def bubble_sort(list:[])->[]:
    n = len(list)
    for j in range(n-1):
        for i in range(n-1-j):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
    return list
#递归实现
def dg_bubble_sort(list):
    if len(list) == 1:
        return list
    else:
        t =max(list)
        list.remove(t)
        t_list=dg_bubble_sort(list)
        t_list.append(t)
        return t_list


def dg2_bubble_sort(list,n):
    if n == 1:
        return list
    else:
        for i in range(n-1):
            if list[i]>list[i+1]:
                list[i],list[i+1]=list[i+1],list[i]
        return dg2_bubble_sort(list,n-1)





# alist=[7,3,9,6,44,33,92,11]
# print(bubble_sort(alist))
blist=[7,3,9,6,44,33,92,11,23,44,53,54,64,234,562,22,62]
print(dg2_bubble_sort(blist,len(blist)))
