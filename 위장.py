def solution(clothes):
    dic = {}

    for i in clothes:
        try:
            dic[i[1]].append(i[0])
        except:
            dic[i[1]] = [i[0]]
    
    mul = 1
    for key, item in dic.items():
        mul *= (len(item)+1)
    
    answer = mul - 1
    return answer