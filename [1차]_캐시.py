from collections import deque

def solution(n, cities):
    cache = deque()
    time = 0

    for i in cities:
        i = i.lower()
        if i in cache:
            time += 1
            cache.remove(i)
            cache.append(i)
        else:
            cache.append(i)
            time += 5
            if len(cache) > n:
                cache.popleft()
    
    return time