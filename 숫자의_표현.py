def solution(n):

    ssum = 0
    cnt = 0
    minus = 1

    for i in range(1,n+1):
        ssum += i

        if ssum > n:
            while ssum > n:
                ssum -= minus
                minus += 1

        if ssum == n:
            cnt += 1
            
    return cnt