def solution(s):

    cnt = 0
    removed = 0
    
    def change(s):
        s = s.replace('0','')
        k = len(s)
        k = bin(k)[2:]

        return k
    
    while s != '1':
        cnt += 1
        removed += s.count('0')
        s = change(s)

    return [cnt, removed]