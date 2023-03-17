from collections import deque

def solution(s):

    q = deque()
    
    # q.append(s[0])
    num = 0

    while num <= len(s) - 1:
        print(q)
        if not q:
            q.append(s[num])
            num += 1
        else:
            first = q.pop()
            if first != s[num]:
                q.append(first)
                q.append(s[num])
            num += 1
    
    if q:
        return 0
    else:
        return 1