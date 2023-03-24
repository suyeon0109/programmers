from collections import deque
from itertools import combinations

def solution(elements):

    lst = deque()

    len_el = len(elements)
    length = 1

    for i in combinations(elements,length):
        print(i)
        print(sum(i))
        lst.append(sum(i))
    print(lst)
    length += 1


    # while length <= len_el:

    #     for k in range(len_el): 
    #         ssum = 0
    #         for i in range(k, k + length):
    #             ssum += elements[i%len_el]
    #         lst.append(ssum)

    #     length += 1

    lst = list(set(lst))
    return len(lst)

print(solution([7,9,1,1,4]))