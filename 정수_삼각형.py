def solution(triangle):
    lst = [ [0]*i for i in range(1,len(triangle)+1)]

    lst[0][0] = triangle[0][0]
    for j in range(len(triangle)-1): # j = 1
        for k in range(j+1): # k = 0 ~ 1, k = 1
            for i in range(k,k+2): # i = 1 ~ 2
                if lst[j][k] + triangle[j+1][i] > lst[j+1][i]:
                    lst[j+1][i] = lst[j][k] + triangle[j+1][i]

    answer = max(lst[-1])
    return answer

# def solution(triangle):
#     dp = [[0]*i for i in range(1,len(triangle)+1)]
#     dp[0][0] = triangle[0][0]
#     for i in range(len(triangle)):
#         for j in range(i):
#             dp[i][j] = max(dp[i][j],dp[i-1][j] + triangle[i][j])
#             dp[i][j+1] = dp[i-1][j] + triangle[i][j+1]
#     return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))