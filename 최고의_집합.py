def solution(n,s):
    answer = []
    if n > s:
        answer = [-1]
        return answer
    
    quotient = s//n
    remainder = s%n
    answer = [quotient] * n
    if remainder:
        for i in range(len(answer)-1, -1, -1):
            answer[i] += 1
            remainder -= 1
            if remainder == 0:
                break

    return answer