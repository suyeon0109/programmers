def solution(s):

    dic = {}

    s = s.rstrip('}}')
    s = s.lstrip('{{')

    s = s.split('},{')

    for i in s:
        lst = i.split(',')
        dic[len(lst)] = lst

    length = len(dic)
    answer = [0]*length

    for j in range(1,length+1):
        for k in dic[j]:
            if int(k) not in answer:
                answer[j-1] = int(k)
        
    return answer