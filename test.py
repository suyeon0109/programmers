def solution(n, works):

    s = sum(works)

    if s <= n:
        return 0
    s -= n
    length = len(works)
    quotient = s//length
    remainder = s%length
    works2 = [quotient] * length

    if remainder:
        for i in range(len(works2)-1, -1, -1):
            works2[i] += 1
            remainder -= 1
            if remainder == 0:
                break

    ssum = 0
    for i in works2:
        ssum += i ** 2

    return ssum

print(solution(1, [2, 1, 2]))
