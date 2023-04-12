def solution(m, n, puddles):
    answer = 0
    road = [[0]*n for _ in range(m)]
    visited = [[0]*n for _ in range(m)]

    for puddle in puddles:
        road[puddle[0]-1][puddle[1]-1] = -1
    
    for i in range(m):
        for j in range(n):
            if road[i][j] != -1:

                if i == 0 and j == 0:
                    visited[i][j] = 1
                    continue

                left, up = 0,0
                if 0 <= j-1:
                    left = visited[i][j-1]
                if 0 <= i-1:
                    up = visited[i-1][j]

                visited[i][j] = (left + up)%1000000007

    answer = visited[m-1][n-1]

    return answer