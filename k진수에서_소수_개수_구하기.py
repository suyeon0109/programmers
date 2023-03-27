from collections import deque
import math

def solution(n, k):
    answer = 0
    lst = deque()
    while n >= k:
        lst.appendleft(str(n%k))
        n //= k
    lst.appendleft(str(n))

    s = ''.join(lst)
    s = s.split('0')
    
    for i in range(len(s)):
        if not s[i]:
            continue

        num = int(s[i])

        if num == 1:
            continue
        elif num == 2:
            answer += 1
            continue
        else:
            for j in range(int(math.sqrt(num)),1,-1):
                if num%j == 0:
                    break
            else:
                answer += 1
    
    return answer