# Задайте список из n чисел последовательности(1+1/n) ^ n и выведите на экран их сумму.


a = int(input('Введите число: '))

list = [round((1+1/i)**i, 2) for i in range(1, a+1)]
print(f'{list}\n{round(sum(list), 2)}')


