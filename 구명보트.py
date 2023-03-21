from collections import deque

def solution(people, limit):
    people.sort()
    people = deque(people)
    start, end = 0, 0

    cnt = 0

    while people:
        start = people.popleft()
        if people:
            end = people.pop()
        else:
            end = 0

        if start + end <= limit :
            cnt += 1
        else :
            people.appendleft(start)
            cnt += 1

    return cnt