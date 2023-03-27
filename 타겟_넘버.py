def solution(numbers, target):

    length = len(numbers)
    global cnt
    cnt = 0

    def dfs(a,b):
        global cnt
        if b == length :
            if a == target:
                cnt += 1
            return

        A = a + numbers[b]
        B = a - numbers[b]

        dfs(A, b+1)
        dfs(B, b+1)
    
    dfs(numbers[0],1)
    dfs(-numbers[0],1)

    return cnt