from collections import Counter

def solution(k, tangerine):
    dic = Counter(tangerine)
    lst = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    orange = 0
    cnt = 0
    for i in range(len(lst)):
        if orange + lst[i][1] <= k:
            orange += lst[i][1]
            cnt += 1
        else:
            if orange == k:
                return cnt
            return cnt + 1
    return cnt