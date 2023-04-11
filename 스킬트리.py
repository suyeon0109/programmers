from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for k in range(len(skill_trees)):
        stk = deque(list(skill))
        for i in range(len(skill_trees[k])):
            if skill_trees[k][i] in skill:
                char = stk.popleft()
                if char != skill_trees[k][i]:
                    break
        else:
            answer += 1

    return answer