val1 = 'результат операции: 42'
val2 = 'результат операции: 54'
val3 = 'результат работы программы: 209'
val4 = 'результат: 2'


def number(var):
    return int(var[var.index(':') + 2:])


num1 = number(val1)
num2 = number(val2)
num3 = number(val3)
num4 = number(val4)
print(num1 + 10)
print(num2 + 10)
print(num3 + 10)
print(num4 + 10)
