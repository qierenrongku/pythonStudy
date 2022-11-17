# _*_ coding:utf-8 _*_
'''
@File       :快速排序.py
@Time       :2022/8/2 22:57
@Author     :且任荣枯
@Version    :1.0

'''

#快速排序
def quick_sort(list,i,j):
    if i >= j:
        return list
    pivot = list[i]
    low = i
    high = j
    while i < j:
        while i < j and list[j] >= pivot:
            j -= 1
        list[i]=list[j]
        while i < j and list[i] <=pivot:
            i += 1
        list[j]=list[i]
    list[j] = pivot
    quick_sort(list,low,i-1)
    quick_sort(list,i+1,high)
    return list


blist=[7,3,9,6,44,33,92,11,23,44,53,54,64,234,562,22,62]
print(quick_sort(blist,0,len(blist)-1))

