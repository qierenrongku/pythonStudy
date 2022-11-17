# _*_ coding:utf-8 _*_
'''
@File       :归并排序.py
@Time       :2022/8/3 21:20
@Author     :且任荣枯
@Version    :1.0

'''
def merg_sort(list,):
    n =len(list)
    if n ==1:
        return list
    else:
        mid = n//2
        left_li=merg_sort(list[0:mid])
        right_li=merg_sort(list[mid:])
        l_p = 0
        r_p = 0
        result =[]
        while l_p<len(left_li) and r_p<len(right_li):
            if left_li[l_p]<right_li[r_p]:
                result.append(left_li[l_p])
                l_p+=1
            else:
                result.append(right_li[r_p])
                r_p+=1

        result+=left_li[l_p:]
        result+=right_li[r_p:]
        return result

blist=[7,3,9,6,44,33,92,11,23,44,53,54,64,234,562,22,62]

print(merg_sort(blist))