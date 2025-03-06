number = 8

while True:
    user_input = input('Попробуй угадать цифру?: ')
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == number:
            print('Поздравляю! Вы угадали!')
            break
        elif user_input > 9:
            print('Это число, а не цифра :D')
            continue
        elif user_input != 8:
            print('Не та, попробуйте снова :(')
            continue
    else:
        if user_input == '':
            print("Поле пустое 0_о, введите цифру")
            continue
        elif user_input == ' ':
            print("Пробел это не цифра -_-, введите цифру")
            continue
        else:
            print('Введите цифру, а не букву 0_0')

print('Возвращайтесь снова!')
