# Задайте список из нескольких чисел. Напишите программу, которая найдет сумму элементов списка,
# стоящих на нечетной позиции.

import random
def create_list():
    numbers = list()
    for i in range(0, 5):
        numbers.append(random.randint(1, 10))
    return numbers

def summ_odd_pos(numbers):
    summ = 0
    for _, item in enumerate(numbers):
        if _ % 2:
            summ += item
    return summ

res = create_list()
print(res)
print(summ_odd_pos(res))