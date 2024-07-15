import random

def get_answer():
    answer = ''

    while len(answer) < 4:
        s = str(random.randrange(9))
        if s in answer:
           ## print(f'duplicated number: {s}')
            continue
        answer += s

    return answer

answer = get_answer()
##print(f'answer is {answer}')

while True :
    str = input("please input : ")
    m = str.isdigit()
    if str == 'quit' :
        print('answer is '+ answer)
        break
    if m == False :
        print('only number')
        continue
    if len(str) != 4 :
        print("four Numbers")
        continue

    for i in range(4):
        if str[i] in str[i+1:4] :
            print(f'duplicated number {str[i]}')
            continue

    count_A = 0
    for i in range(4) :
        if str[i] == answer[i] :
            count_A += 1

    if count_A == 4:
        print('victory')
        break

    count_B = 0
    for i in range(4) :
        for j in range(4) :
            if answer[i] == str[j] and i != j:
                count_B += 1
    print(f'hint {count_A}A,{count_B}B')

