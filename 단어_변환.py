def solution(begin, target, words):
    global cnt_min
    answer = 0
    cnt = 0
    cnt_min = 10e9
    visited = []
    if target not in words:
        return answer
    
    dfs(begin, target, words, cnt, visited)

    answer = cnt_min
    
    return answer

def dfs(begin, target, words, cnt, visited):
    global cnt_min

    if begin == target:
        if cnt <= cnt_min:
            cnt_min = cnt
            return
    
    if cnt > cnt_min:
        return

    for i in range(len(words)):
        word = words[i]
        if word == begin or word in visited:
            continue
        cnt_diff = 0
        for j in range(len(begin)):
            if begin[j] != word[j]:
                cnt_diff += 1
            
            if cnt_diff > 1:
                break
        else:
            cnt += 1
            visited.append(word)
            dfs(word, target, words, cnt, visited)
            visited.pop()
            cnt -= 1