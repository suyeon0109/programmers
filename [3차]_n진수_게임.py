from collections import deque

def solution(n, t, m, p):
    answer = ''

    num = 0
    num2 = 0
    index = 1

    while len(answer) <= t:

        lst = deque()
        num2 = num
        while num2 >= n: # num을 n진수로 바꾸는 과정. -> num < n일 경우 실행 x
            remainder = num2%n
            if remainder >= 10:
                remainder = chr(remainder + 55)

            lst.appendleft(str(remainder))
            num2 //= n
        
        if num2 >= 10:
            lst.appendleft(chr(num2+55))
        else:
            lst.appendleft(str(num2))
        
        # s = n 진수 변환
        s = ''.join(lst)

        # s의 한 글자씩 검사 -> 튜브의 순서에 맞는 글자를 answer에 더함
        for i in range(len(s)):
            if index % m == p % m:
                answer += s[i]
                if len(answer) == t:
                    return answer
            index += 1 # 다음 글자의 인덱스
        
        num += 1