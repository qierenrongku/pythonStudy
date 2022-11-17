# _*_ coding:utf-8 _*_
'''
@File       :sample.py
@Time       :2022/8/17 22:06
@Author     :且任荣枯
@Version    :1.0

'''
from faker import Faker
fakeob = Faker('zh-CN')
# print(fakeob.user_agent())
# print(fakeob.paragraphs())
# print(fakeob.profile())
students = []
for i in range(30):
    student = fakeob.name()+"  "+fakeob.address()+"  "+fakeob.ssn()
    students.append(student)
print(students)
# https://www.bilibili.com/video/BV1RK4y1t71w?spm_id_from=333.337.search-card.all.click&vd_source=2f93a9fe36f6fcd519542fb82331d531