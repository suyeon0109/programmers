import math

def solution(fees, records):

    dic = {}
    answer_dic = {}
    answer = []

    for i in range(len(records)):
        lst = records[i].split(' ')
        if lst[-1] == 'IN':
            dic[lst[1]] = lst
            if not answer_dic.get(lst[1]):
                answer_dic[lst[1]] = 0
        else:
            in_info = dic.pop(lst[1])[0]
            in_info = in_info.split(':')
            in_hour, in_minute = int(in_info[0]), int(in_info[1])

            out_info = lst[0].split(':')
            out_hour, out_minute = int(out_info[0]), int(out_info[1])

            ssum_time = (60 * out_hour + out_minute) - (60 * in_hour + in_minute)
            answer_dic[lst[1]] += ssum_time
    
    if dic:
        for key, item in dic.items():
            in_info = item[0]
            in_info = in_info.split(':')
            in_hour, in_minute = int(in_info[0]), int(in_info[1])

            out_hour, out_minute = 23, 59

            ssum_time = (60 * out_hour + out_minute) - (60 * in_hour + in_minute)

            answer_dic[key] += ssum_time
    
    for key, item in sorted(answer_dic.items()):
        if item > fees[0]:
            answer.append(fees[1] + math.ceil((item - fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])

    return answer