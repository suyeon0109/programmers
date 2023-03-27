from collections import deque

def solution(priorities, location):
    maxx = max(priorities)
    priorWithLoc = deque()
    order = 0

    for i in range(len(priorities)):
        priorWithLoc.append((priorities[i],i))
    
    while priorWithLoc:
        maxx = max(priorWithLoc)[0]
        a,b = priorWithLoc.popleft()

        if a == maxx:
            order += 1
            if b == location:
                answer = order
                return answer
        else:
            priorWithLoc.append((a,b))