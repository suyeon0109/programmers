def solution(msg):
    dic = {}
    stk = []
    cnt = 27
    for i in range(1,27):
        dic[chr(i+64)] = i
    
    string = ''
    string += msg[0]
    for j in range(1, len(msg)):
        if dic.get(string + msg[j]):
            string += msg[j]
            continue
        else:
            stk.append(dic[string])
            dic[string + msg[j]] = cnt
            cnt += 1
            string = msg[j]
    
    if string:
        stk.append(dic[string])

    return stk