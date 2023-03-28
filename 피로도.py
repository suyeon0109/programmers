def solution(k, dungeons):
    dungeons.sort(reverse=True)
    global maxx
    maxx = 0
    visited = [0]*len(dungeons)

    def dfs(k, dungeons, cnt):
        global maxx
        if cnt > maxx:
            maxx = cnt
        
        for i in range(len(dungeons)):
            if dungeons[i][0] <= k and visited[i] == 0:
                visited[i] = 1
                dfs(k - dungeons[i][1], dungeons, cnt + 1)
                visited[i] = 0
    
    dfs(k, dungeons, 0)
        
    return maxx