from collections import deque

def solution(want, number, discount):
    dic = {}
    dic2 = {}
    q = deque()
    cnt = 0

    for i in range(len(want)):
        dic[want[i]] = number[i]
        dic2[want[i]] = 0

    for j in range(len(discount)):
        q.append(discount[j])
        if len(q) > 10:
            menu = q.popleft()
            if dic2.get(menu):
                dic2[menu] -= 1
        
        if dic2.get(discount[j]) or dic2.get(discount[j]) == 0:
            dic2[discount[j]] += 1
        
        if dic2 == dic:
            cnt += 1

    return cnt