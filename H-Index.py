def solution(citations):
    citations.sort()

    maxx = 0

    citation = 0

    for i in range(len(citations)-1, -1, -1):
        citation += 1
        if citations[i] <= len(citations) - i:
            start = citations[i]

            while 1:
                if len(citations) - i - 1 > start:
                    start += 1
                else:
                    maxx = start
                    return maxx
    else:
        maxx = citation


    return maxx