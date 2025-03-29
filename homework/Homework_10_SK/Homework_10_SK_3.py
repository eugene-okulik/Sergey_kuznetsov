def calc_dec(func):
    def wrapper(first, second, operation):
        if first == second:
            operation = '+'
        if first > second:
            operation = '-'
        elif first < second:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)

    return wrapper


@calc_dec
def calc(first, second, operation):
    first = float(first)
    second = float(second)
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


num1 = float(input('Введите число 1 - '))
num2 = float(input('Введите число 2 - '))
oper = input('Знак - ')

print(calc(num1, num2, oper))
