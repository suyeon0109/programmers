def solution(s):
    lst = s.split(' ')

    for k in range(len(lst)):
        lst[k] = int(lst[k])
    a,b = min(lst), max(lst)
    answer = str(a) + ' ' + str(b)
    return answer