def solution(prices):
    answer = [0] * len(prices)
    stk = []
    for i in range(len(prices)):
        if not stk:
            stk.append((prices[i], i))
        else:
            while stk:
                price, idx = stk.pop()
                if prices[i] < price:
                    answer[idx] = i - idx
                else:
                    stk.append((price, idx))
                    break
            stk.append((prices[i], i))
    if stk:
        length = len(prices) - 1
        while stk:
            price, idx = stk.pop()
            answer[idx] = length - idx
            
    return answer