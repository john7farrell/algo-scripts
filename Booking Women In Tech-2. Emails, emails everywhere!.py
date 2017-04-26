# -*- coding: utf-8 -*-
#     Key point
# 1. use minus value to build a max_heap
# 2. add a changing constant to pre-sort the equalities

from heapq import *

def get_next_email(memory):
    if memory == []:
        print('-1')
    else:
        print(heappop(memory)[-1])
def store_email(memory, email, urgency, cnt):
    const = 1e-6
    heappush(memory, (-(urgency - cnt * const), cnt, email))
    return memory 
n = int(input())
memory = []
cnt = 0
for a0 in range(n):
    request0 = input().split(' ')
    #print(request0)
    if len(request0) == 1 and request0 == ['get_next_email']:
        get_next_email(memory)
    elif len(request0) == 3:
        query, email, urgency = request0[0], request0[1], request0[2]
        urgency = int(urgency)
        cnt += 1
        memory = store_email(memory, email, urgency, cnt)
    else:
        print('Unknown query!')
