# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


a = input('Введите число: ')
result = 0

for i in a:
  if i.isdigit():
    result+= int(i)

print(result)
