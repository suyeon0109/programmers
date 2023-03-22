def solution(s):
    s = s.lstrip('{{')
    s = s.rstrip('}}')
    lst = s.split('},{')
    for i in range(len(lst)):
        lst[i] = lst[i].split(',')
    print(lst)
    answer = []
    return answer

solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")