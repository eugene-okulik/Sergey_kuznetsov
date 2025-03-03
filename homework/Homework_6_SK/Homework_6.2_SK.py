# Задание 2

numbers_list = list(range(1, 101))

res_list = []
for num in numbers_list:
    if num % 3 == 0 and num % 5 == 0:
        new_num = 'FuzzBuzz'
    elif num % 3 == 0:
        new_num = 'Fuzz'
    elif num % 5 == 0:
        new_num = 'Buzz'
    else:
        new_num = str(num)

    res_list.append(new_num)

new_list3 = ' '.join(res_list)

print(new_list3)
