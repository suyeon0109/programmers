def solution(arr):
    arr.sort()

    maxx = arr[-1]
    multi = 1

    while 1:
        multiple = maxx * multi
        for i in range(len(arr)-1):
            if multiple % arr[i] != 0:
                multi += 1
                break
        else:
            return multiple