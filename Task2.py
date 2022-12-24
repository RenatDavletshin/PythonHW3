# Напишите программу, которая найдет произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и последний и т.д. 

import random
import math

def create_list():
    numbers = list()
    for i in range(0, 7):
        numbers.append(random.randint(1, 10))
    return numbers

def sked(numbers):
    roster = list()
    j = -1
    for i in range(math.ceil(len(numbers) / 2)):
        roster.append(numbers[i] * numbers[j])
        j += -1
    return roster

nums = create_list()
print(nums)
print(sked(nums))