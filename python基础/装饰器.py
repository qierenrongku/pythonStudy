# _*_ coding:utf-8 _*_
'''
@File       :装饰器.py
@Time       :2022/7/30 22:49
@Author     :且任荣枯
@Version    :1.0

'''

# def fun1():
#     print("I am a function1")
#     return "I am a return value1"
#
# # 我们想要在函数的前后进行修饰 所以用一个函数将fun包起来
# def out1(fun):
#     print("begin------------")
#     r=fun()
#     print("end--------------")
#     return r
#
#
# print(out1(fun))
'''
begin------------
I am a function
end--------------
I am a return value
'''

# 每有一个fun 需要定义一个out  so?

def begin_end(fun):
    def inner(*args,**kwargs):
        print("开始")
        r=fun(*args,**kwargs)
        print("结束")
        return r
    return inner


@begin_end
def add(*args):
    r =0
    print("计算中")
    for x in args:
        r+=x
    return x


print(add(3, 4, 5))
