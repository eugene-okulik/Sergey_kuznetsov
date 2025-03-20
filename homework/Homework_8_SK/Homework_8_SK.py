# Задание 1
import random

user_input1 = input('What you salary?')
salary = int(user_input1)
bonus = random.choice([True, False])

if bonus:
    bonus_num = random.randint(0, 1000)
    salary += bonus_num

print(f"{user_input1},{bonus}-'${salary}'")
