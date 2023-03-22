def solution(arr1, arr2):
    answer_row = len(arr1)
    answer_col = len(arr2[-1])
    answer = [[0]*answer_col for _ in range(answer_row)]


    for row in range(len(arr1)):
        for col2 in range(len(arr2[0])):
            for i in range(len(arr1[row])):

                answer[row][col2] += arr1[row][i] * arr2[i][col2]

    return answer