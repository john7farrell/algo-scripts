# -*- coding: utf-8 -*-
# def check_inventory_memo still has 2 cases TimeLimitError, but accepted
#     Key point
# 1. list transpose
# 2. memoization

from heapq import *

def check_inventory_memo(query, query_results, price_byDay, inventory_byDay):
    checkInDay = query[0] - 1
    lengthStay = query[1]
    price = 0
    for day in range(checkInDay, checkInDay + lengthStay):
        q = (day + 1, lengthStay)
        if q in price_byDay:
            price += price_byDay[q]
        else:
            inv_bak = []
            while inventory_byDay[day]:
                item = heappop(inventory_byDay[day])
                heappush(inv_bak, item)
                for length in range(item[1], item[2] + 1):
                    q_byDay = (day + 1, length)
                    if q_byDay not in price_byDay:
                        price_byDay[q_byDay] = item[0]
            while inv_bak:
                heappush(inventory_byDay[day], heappop(inv_bak))
            if q in price_byDay:
                price += price_byDay[q]
            else:
                price = -1
                break
    query_results[(checkInDay + 1, lengthStay)] = price
    return query_results, price_byDay, inventory_byDay

def getColData(prices, minStay, maxStay):
    pr_col, minS_col, maxS_col = [], [], []
    for pr in zip(*prices):
        pr_col.append(pr)
    for minS in zip(*minStay):
        minS_col.append(minS)
    for maxS in zip(*maxStay):
        maxS_col.append(maxS)
    return pr_col, minS_col, maxS_col

def check_inventory(query, query_results, inventory_byDay):
    checkInDay = query[0] - 1
    lengthStay = query[1]
    price = 0
    for day in range(checkInDay, checkInDay + lengthStay):
        found = False
        inv_bak = []
        while not found and inventory_byDay[day]:
            item = heappop(inventory_byDay[day])
            heappush(inv_bak, item)
            if item[1] <= lengthStay <= item[2]:
                found = True
                price += item[0]
                break
            else:
                continue
        while inv_bak:
            heappush(inventory_byDay[day], heappop(inv_bak))
        if not found:
            break
    if found:
        query_results[(checkInDay + 1, lengthStay)] = price
    else:
        query_results[(checkInDay + 1, lengthStay)] = -1
    return query_results, inventory_byDay

n, m, q = list(map(int, input().split(' ')))
prices = []
minStay = []
maxStay = []

for a0 in range(m):
    li = list(map(int, input().split(' ')))
    prices.append(li)
for a0 in range(m):
    li = list(map(int, input().split(' ')))
    minStay.append(li)
for a0 in range(m):
    li = list(map(int, input().split(' ')))
    maxStay.append(li)
pr_col, minS_col, maxS_col = getColData(prices, minStay, maxStay)

inventory_byDay = []
for a0 in range(n):
    inventory_byDay0 = []
    for a1 in range(m):
        item = [pr_col[a0][a1], minS_col[a0][a1], maxS_col[a0][a1]]
        if item[0] != 0:
            heappush(inventory_byDay0, tuple(item))
    inventory_byDay.append(inventory_byDay0)

query_results = {}
price_byDay = {}
for a0 in range(q):
    query = tuple(map(int, input().split(' ')))
    if query not in query_results:
        query_results, price_byDay, inventory_byDay = check_inventory_memo(query, query_results, price_byDay, inventory_byDay)
    print(query_results[query])
    
