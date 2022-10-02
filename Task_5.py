# Реализуйте алгоритм перемешивания списка
# (метод random.shuffle использовать нельзя, но другие методы из библиотеки random - можно).


import random
list_first = [1, 2, 3, 4, 5, 6]
print(f'Исходный список: {list_first}')

list = list_first[:]
list_len = len(list)
for i in range(list_len):
  index = random.randint(0, list_len - 1)
  temp = list[i]
  list[i] = list[index]
  list[index] = temp
print(f'Сортированный список: {list}')
