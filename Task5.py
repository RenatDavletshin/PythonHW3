# Задайте число. Составьте список чисел Фибоначчи в том числе для отрицательных индексов.

n = int(input('Введите число: '))
if n < 0: n = n*-1
f1 = f2 = 1
list_of_numbers = [f1, f2]
for i in range(2, n):
    f1,f2 = f2, f1 + f2
    list_of_numbers.append(f2)
print(list_of_numbers)
f1=f2=1
for i in range(-n, 1):
    f1,f2 = f2, f1 - f2
    list_of_numbers.insert(0, f2)
print(list_of_numbers)