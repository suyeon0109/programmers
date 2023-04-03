import heapq

def solution(n, works):

    s = sum(works)

    if s <= n:
        return 0
    
    ssum = 0
    
    works2 = []

    for i in range(len(works)):
        heapq.heappush(works2, -works[i])
    
    for _ in range(n):
        a = heapq.heappop(works2)
        a += 1
        if a != 0:
            heapq.heappush(works2, a)
    
    for k in works2:
        ssum += k**2

    return ssum