# Задайте список из вещественных чисел. Напишите программу, 
# которая найдет разницу между максимальным и минимальным значением дробной части элементов.

my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_first_list = []

for i in range(len(my_list)):
    if my_list[i]:
        my_first_list.append(my_list[i])
new_list = [round(my_first_list[i] % 1, 2) for i in range(len(my_first_list))]
print(f'{new_list} => {max(new_list) - min(new_list)}')