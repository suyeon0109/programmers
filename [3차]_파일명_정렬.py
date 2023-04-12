def solution(files):
    answer = []
    lst = []
    for word in files:
        head = ''
        number = ''
        tail = ''
        head_chk = 0
        for i in range(len(word)):

            if word[i].isdigit():
                number += word[i]
                for j in range(i+1, len(word)):
                    if word[j].isdigit():
                        number += word[j]
                    else:
                        tail = word[j:]
                        break
            else:
                head += word[i]
            
            if number:
                break

        lst.append([head,number,tail])
    
    lst = sorted(lst, key=lambda x:(x[0].lower(), int(x[1])))
    answer = [''.join(i) for i in lst]

    return answer