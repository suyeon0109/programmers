from collections import deque

def solution(s):
    s = deque(list(s))
    cnt = 0

    for _ in range(len(s) - 1):

        stk = []

        for i in range(len(s)):
            if stk:
                if stk[-1] == '[' and s[i] == ']':
                    stk.pop()
                elif stk[-1] == '{' and s[i] == '}':
                    stk.pop()
                elif stk[-1] == '(' and s[i] == ')':
                    stk.pop()
                else:
                    stk.append(s[i])
            else:
                stk.append(s[i])
        
        if not stk:
            cnt += 1
        
        s.rotate(-1)
    
    return cnt