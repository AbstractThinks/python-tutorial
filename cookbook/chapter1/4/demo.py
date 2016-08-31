# -*- coding:utf-8 -*-

# 找到最大或是最小元素
# heapq 模块
# nlargest()和 nsmallest()


import heapq

nums = [1, 8, 33, 99, 88, 0, 77]

print(heapq.nlargest(3, nums))
print(heapq.nsmallest(2, nums))

portfolio = [{
        'name':'jesse', 'share':70, 'price': 100
    },{
        'name':'alvin', 'share':80, 'price':90
    },{
        'name':'leslie', 'share':90, 'price':80
    },{
        'name':'fen', 'share':100, 'price':70
        }]

cheap = heapq.nsmallest(2, portfolio, key=lambda s:s['price'])
print(cheap)
expensive = heapq.nlargest(2, portfolio, key=lambda s:s['share'])
print(expensive)
