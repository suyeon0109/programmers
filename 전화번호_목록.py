def solution(phone_book):
    phone_book.sort()
    answer = True
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) <= len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
                answer = False
    return answer