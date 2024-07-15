def get_the_A(answer, user_input):
    the_A = 0
    for i in range(len(user_input)):
        if answer[i] == user_input[i]:
            the_A += 1

    return the_A

