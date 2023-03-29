def solution(n, computers):
    visited = [0] * n
    cnt = 0

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i, computers, visited)
            cnt += 1

    return cnt

def dfs(i, computers, visited):
    for j in range(len(computers[i])):
        if j != i and visited[j] == 0 and computers[i][j] == 1:
            visited[j] = 1
            dfs(j, computers, visited)