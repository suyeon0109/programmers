from collections import deque

def solution(dirs):
    answer = 0

    dx = {'U':-1, 'D':1, 'R':0, 'L':0}
    dy = {'U':0, 'D':0, 'R':1, 'L':-1}

    moved = deque()

    now = [5,5]

    for i in range(len(dirs)):
        x = now[0]
        y = now[1]
        if 0 <= x + dx[dirs[i]] <= 10 and 0 <= y + dy[dirs[i]] <= 10:
            now[0] = x + dx[dirs[i]]
            now[1] = y + dy[dirs[i]]
            if ([x,y], [now[0],now[1]]) not in moved:
                moved.append(([x,y], [now[0],now[1]]))
                moved.append(([now[0],now[1]],[x,y]))
                answer += 1

    return answer