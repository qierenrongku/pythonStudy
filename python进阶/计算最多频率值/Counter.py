# _*_ coding:utf-8 _*_
'''
@File       :Counter.py
@Time       :2022/9/22 22:33
@Author     :且任荣枯
@Version    :1.0

'''
from collections import Counter
words =[
    'look','out','me','my','you','look','out','me','look','out','me','look','out',
    'me','my','you','look','my','you','look','my','you','look','how'
]
words_counts = Counter(words)
top_three = words_counts.most_common(3)
print(top_three)
# [('look', 7), ('out', 4), ('me', 4)]