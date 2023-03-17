def solution(n, words):
    answer = [0,0]
    cnt = 0
    lst = []

    for i in range(len(words)):
        cnt +=1

        if i >= 1:
            if words[i] in lst or words[i-1][-1] != words[i][0]:
                if cnt%n == 0:
                    answer[0], answer[1] = n, cnt//n
                else:
                    answer[0], answer[1] = cnt%n, cnt//n + 1
                return answer
        lst.append(words[i])

    return answer