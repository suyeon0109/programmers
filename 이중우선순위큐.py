import heapq

def solution(operations):
    heap = []

    for i in range(len(operations)):
        lst = operations[i].split(' ')
        oper = lst[0]
        num = int(lst[1])

        if oper == 'I':
            heapq.heappush(heap, num)
        else:
            if num == 1:
                if heap:
                    for i in range(len(heap)):
                        heap[i] = -heap[i]
                    heapq.heapify(heap)
                    heapq.heappop(heap)

                    for i in range(len(heap)):
                        heap[i] = -heap[i]
                    heapq.heapify(heap)
            else:
                if heap:
                    heapq.heappop(heap)
    
    heapq.heapify(heap)

    if heap:
        answer = [max(heap), heapq.heappop(heap)]
    else:
        answer = [0,0]

    return answer