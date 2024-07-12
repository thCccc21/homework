import random

def get_answer():
    answer = ''

    while len(answer) < 4:
        s = str(random.randint(0, 9))
        if s in answer:
            print(f'duplicated number: {s}')
            continue
        answer += s

    return answer

answer = get_answer()
print(f'answer is {answer}')

