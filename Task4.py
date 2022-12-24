# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def bin(dec_number):
    bin_number = ''
    while dec_number > 0:
            bin_number = str(dec_number % 2) + bin_number
            dec_number = dec_number // 2
    return bin_number

number = int(input('Введите число: '))
print(f'{number} -> {bin(number)}')
