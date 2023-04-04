import datetime

def solution(fees, records):

    dic = {}
    stk = []
    answer = []

    for i in range(len(records)):
        lst = records[i].split(' ')
        if lst[-1] == 'IN':
            stk.append(lst[1])
        else:
            in_info = dic.get(lst[1])[0]
            in_info = in_info.split(':')
            in_hour, in_minute = int(in_info[0]), int(in_info[1])

            out_info = lst[0].split(':')
            out_hour, out_minute = int(out_info[0]), int(out_info[1])

            ssum_time = (60 * out_hour + out_minute) - (60 * in_hour + in_minute)

            if ssum_time > fees[0]:
                answer.append(fees[1] + int((ssum_time - fees[0])/fees[2])*fees[3])
            else:
                answer.append(fees[0])
        

    return answer

# print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
dic1 = {'a':1}
t = dic1.pop('a')
print(t)