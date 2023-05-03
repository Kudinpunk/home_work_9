# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# Пример:  2 2   4 

first_number = int(input('Ввведите первое число:'))
second_number = int(input('Ввведите второе число:'))

def sum_numbers(number_1, number_2):
    if number_1 == 0:
        return number_2
    return sum_numbers(number_1 - 1, number_2 + 1)

print(f'{first_number} + {second_number} = {sum_numbers(first_number, second_number)}')