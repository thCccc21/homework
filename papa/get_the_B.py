def get_the_B(answer, user_input):
    the_B = 0
    for index, data in enumerate(user_input):
        for x in range(len(answer)):
            if index != x and user_input[index] == answer[x]:
                the_B += 1

    return the_B

