def solution(A,B):
    A.sort()
    B.sort()
    B.reverse()

    ssum = 0

    for i in range(len(A)):
        ssum += A[i] * B[i]

    return ssum