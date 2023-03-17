def solution(n):
    n_bin = bin(n)[2:]
    cnt_n = n_bin.count('1')
    while 1:
        n += 1
        n2_bin = bin(n)[2:]
        if cnt_n == n2_bin.count('1'):
            answer = n
            return answer