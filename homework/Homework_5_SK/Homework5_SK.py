# ЗАДАНИЕ 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

print(name, last_name, city, phone, country)

# ЗАДАНИЕ 2

result_operation = 'результат операции: 42'
result_operation2 = 'результат операции: 514'
result_program = 'результат работы программы: 9'

#n1 = int(result_operation[result_operation.index(':') + 2:]) + 10
n1 = int(result_operation[result_operation.index('4'):]) + 10
n2 = int(result_operation2[result_operation2.index('5'):]) + 10
n3 = int(result_program[result_program.index('9'):]) + 10

print(n1, n2, n3)



# ЗАДАНИЕ 3

students = ['Ivanov', 'Petrov', 'Sidorov']

subjects = ['math', 'biology', 'geography']

print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))
