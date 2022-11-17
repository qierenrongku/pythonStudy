# _*_ coding:utf-8 _*_
'''
@File       :选则排序.py
@Time       :2022/8/2 22:14
@Author     :且任荣枯
@Version    :1.0

'''
#选择排序
def select_sort(list):
    for i in range(len(list)-1):
        min_index = i
        for j in range(i+1,len(list)):
            if list[min_index] >list[j]:
                min_index=j
        list[i] ,list[min_index] =list[min_index],list[i]
    return  list


def dg_select_sort(list,n):
    if n == 1:
        return list
    else:
        max_index = 0
        for i in range(n):
            if list[max_index]<list[i]:
                max_index = i
        list[n-1],list[max_index] = list[max_index],list[n-1]
        return dg_select_sort(list,n-1)






blist=[7,3,9,6,44,33,92,11,23,44,53,54,64,234,562,22,62]
# print(select_sort(blist))
print(dg_select_sort(blist,len(blist)))

