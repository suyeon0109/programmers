def solution(n, left, right):

    quotient = left//n
    remainder = left%n

    quotient2 = right//n

    lst = [quotient + 1] * (quotient + 1)
    lst.extend([i for i in range(quotient+2,n+1)])

    answer = []

    answer.extend(lst)

    for j in range(quotient+2, quotient2+2):
        for k in range(j-1):
            lst[k] = j
        answer.extend(lst)

    answer = answer[remainder:remainder + (right - left) + 1]

    return answer