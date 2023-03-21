fibo = [0,1,1]

def solution(n):

    def fibonacci(n):
        if len(fibo) >= n + 1 :
            return fibo[n]
        else:
            for i in range(len(fibo),n+1):
                fibo.append(fibo[i-2] + fibo[i-1])
            return fibo[n]
    
    answer = fibonacci(n+1) % 1234567

    return answer