import math
def solution(progresses, speeds):
    answer = []
    times = []

    for i in range(len(progresses)):
        time = math.ceil((100 - progresses[i]) / speeds[i])
        times.append(time)
    
    deploy = 1
    
    start = times[0]
    for j in range(1, len(times)):
        if times[j] <= start:
            deploy += 1
        else:
            start = times[j]
            answer.append(deploy)
            deploy = 1
    
    answer.append(deploy)

    return answer