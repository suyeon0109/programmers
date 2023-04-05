import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    if K < scoville[0]:
        return -1
    
    while 1:
        
        minn = heapq.heappop(scoville)

        if minn >= K:
            return answer
        elif not scoville:
            return -1
        
        minn2 = heapq.heappop(scoville)

        mixed = minn + minn2*2
        heapq.heappush(scoville,mixed)
        answer += 1

    return answer