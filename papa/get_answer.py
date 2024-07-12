import random

def get_answer():
    answer = ''

    while len(answer) < 4:
        s = str(random.randrange(9))
        if s in answer:
            print(f'duplicated number: {s}')
            continue
        answer += s

    return answer

answer = get_answer()
print(f'answer is {answer}')

while True :
    str = input("please input")
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
   



