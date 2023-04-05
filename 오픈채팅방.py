def solution(record):
    answer = []
    dic_name = {}
    for i in range(len(record)):
        lst = record[i].split(' ')
        if lst[0] == 'Enter' or lst[0] == 'Change':
            dic_name[lst[1]] = lst[2]
    
    for j in range(len(record)):
        lst = record[j].split(' ')
        if lst[0] == 'Enter':
            answer.append(f"{dic_name[lst[1]]}님이 들어왔습니다.")
        elif lst[0] == 'Leave':
            answer.append(f"{dic_name[lst[1]]}님이 나갔습니다.")
    
    return answer