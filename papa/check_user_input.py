def check_user_input(value):
    if not value.isdigit():
        print('Number (0 ~ 9) only!')
        return False

    if len(value) != 4:
        print(f'Please input 4 numbers!')
        return False

    for index, data in enumerate(value):
        for x in range(index+1, len(value)):
            if value[index] == value[x]:
                print(f'Do not input the duplicated number: {value[index]}')
                return False

    return True

