# 1.1 Запрос строки у пользователя и создание кортежа
user_input = input("Введите строку без пробелов: ")  # Запрос строки без пробелов
tuple_1 = tuple(user_input)  # Создание кортежа из введенной строки
print("Созданный кортеж:", tuple_1)  # Вывод созданного кортежа

# Sample Input 1:
# ‘TheBigBen’
# Sample Output 1:
# Created tuple is:
# (‘T’, ‘h’, ‘e’, ‘B’, ‘i’, ‘g’, ‘B’, ‘e’, ‘n’)



# 1.2 Преобразование кортежа в строку
tuple_1 = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')  # Заданный кортеж
string_1 = ''.join(tuple_1)  # Преобразование кортежа в строку
print("Полученная строка:", string_1)  # Вывод полученной строки

# Sample Input 1:
# (‘T’, ‘h’, ‘e’, ‘B’, ‘i’, ‘g’, ‘B’, ‘e’, ‘n’)’
# Sample Output 1:
# The string is: ‘TheBigBen

# 1.3 Конкатенация двух кортежей
tuple_A = (1, 2, 3, 4, 5, 6, 7)  # Первый кортеж
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)  # Второй кортеж

mid_point = len(tuple_A) // 2  # Вычисление средней точки кортежа
tuple_C = tuple_A[:mid_point] + tuple_B[mid_point:]  # Конкатенация первой половины tuple_A с второй половиной tuple_B
print("Результат конкатенации:", tuple_C)  # Вывод результирующего кортежа

# Sample Input 1:
#   tuple_A: (1,2,3,4,5,6,7)
#   tuple_B: (5,6,7,9,7,1,10,10)
# Sample Output 1:
#  (1,2,3,4,7,1,10,10)
# here (1,2,3,4)- the first half of the tuple_A
# (7,1,10,10) - the second half of the tuple_B

# 1.4 Подсчет количества вхождений элементов в кортеж и создание нового кортежа
def count_occurrences(input_tuple):
    occurrences = {}  # Инициализация словаря для подсчета вхождений
    for item in input_tuple:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1

    occurrences_list = [(key, value) for key, value in occurrences.items()]  # Создание списка кортежей (элемент, количество)
    return tuple(occurrences_list)  # Преобразование списка в кортеж

# Примеры входных данных
input_tuple_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
input_tuple_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
input_tuple_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

# Подсчет вхождений и создание кортежей
output_tuple_1 = count_occurrences(input_tuple_1)
output_tuple_2 = count_occurrences(input_tuple_2)
output_tuple_3 = count_occurrences(input_tuple_3)

# Вывод результирующих кортежей
print("Элементы и их количество:")
print(output_tuple_1)
print(output_tuple_2)
print(output_tuple_3)

# Sample Input 1:
#   (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
# Sample Input 2:
#  (‘55’, ‘6’, ‘777’, 54, 6, 7777, 9, 777, 6)
# Sample input 3:
# ((1,2,3), ([‘A’, ‘B’]), (1,2,3), ([‘A’]))
# Sample Output 1:
# Elements and their occurrences:
# ((55,1), (6,3), (777,2), (54,1), (76,1), (7777,1), (1,1))
# Sample Output 2:
# Elements and their occurrences:
# ((‘55’,1), (‘6’,1), (‘777’,1), (54,1), (6,2), (7777,1), (9,1), (777,1))
# Sample Output 3:
# Elements and their occurrences: (((1,2,3),2), (([‘A’, ‘B’]),1), (([‘A’]),1))

# 1.5 Создание кортежей для хранения конкретных типов данных
data_objects = (55, 6, 777, 70.0, '7', 'A')  # Заданные объекты

# Создание кортежей для хранения определенных типов данных
tuple_integers = tuple(item for item in data_objects if isinstance(item, int))
tuple_floats = tuple(item for item in data_objects if isinstance(item, float))
tuple_strings = tuple(item for item in data_objects if isinstance(item, str))

# Вывод результирующих кортежей
print(tuple_integers)
print(tuple_floats)
print(tuple_strings)

# Sample
# Input
# 1:
#
# (55, 6, 777, 70.0, ‘7’, ‘A’)
# Sample
# Output
# 1:
# (55, 6, 777)
# (70.0)
# (‘7’, ‘A’)

# 2.1 Запрос строки у пользователя и создание множества с использованием генератора множеств
user_input = input("Введите строку без пробелов: ")  # Запрос строки без пробелов
created_set = {char for char in user_input}  # Создание множества с уникальными символами из введенной строки
print("Созданное множество:", created_set)  # Вывод созданного множества


# Sample Input 1:
# ‘TheBigBen’
# Sample Output 1:
# Created set is:
# {‘n’, ‘T’, ‘e’, ‘B’, ‘h’, ‘i’, ‘g’}

# 2.2 Создание множества, которое является разностью двух множеств
set_A = {1, 2, 3, 4, 5}  # Первое множество
set_B = {5, 7, 8, 9, 2, 10}  # Второе множество
result_set = set_A.difference(set_B)  # Создание множества, которое является разностью set_A и set_B
print("Результат разности множеств:", result_set)  # Вывод результирующего множества

# Sample Input 1:
#        set_A = {1,2,3,4,5}
#        set_B  = {5,7,8,9,2,10}
# Sample Output 1:
#        {1,3,4,7,8,9,10}
# elements 1,3,4 are not in set B and 7,8,9,10 are not in set A

# 2.3 Удаление элементов из множества, если они также есть в другом множестве
set_A = {1, 2, 3, 4, 5}  # Первое множество
set_B = {5, 7, 8, 9, 2, 10}  # Второе множество
set_A.difference_update(set_B)  # Удаление элементов из set_A, если они также есть в set_B
print("Измененное множество set_A:", set_A)  # Вывод измененного множества set_A

# SSample Input 1:
#        set_A = {1,2,3,4,5}
#        set_B = {5,7,8,9,2,10}
# Sample Output 1:
#        {7,8,9,2,10}

# 2.4 Перемещение элементов из одного множества в другое, если они также есть в третьем множестве
set_A = {1, 2, 3, 4, 7}  # Первое множество
set_B = {8, 7, 9, 4, 2, 0, 10}  # Второе множество
set_C = {4, 0, 1}  # Третье множество

# Проверяем каждый элемент в set_A
for element in set_A.copy():
    if element in set_C:
        set_A.remove(element)  # Удаляем элемент из set_A
        set_B.add(element)  # Добавляем элемент в set_B

# Вывод измененных множеств
print("Измененное множество set_A:", set_A)
print("Измененное множество set_B:", set_B)

# Sample Input 1:
#        set_A = {1, 2, 3, 4, 7}
#        set_B = {8, 7, 9, 4, 2, 0, 10}
#        set_C = {4, 0, 1}
# Sample Output 1:
#        Updated set_C = {4, 1, 0, 2, 7}

# 2.5 Создание списка множеств определенного размера
import random

A = {1, 2, 3, 4, 5, 6}  # Надмножество A
n = 3  # Размер множества
m = 5  # Количество множеств

combinations_list = []  # Список для хранения множеств

for _ in range(m):
    combination = set(random.sample(A, n))  # Создание множества случайных элементов из A
    combinations_list.append(combination)  # Добавление множества в список

# Вывод списка множеств
print(combinations_list)

# Sample Input 1:
#        A = {1,2,3,4,5,6}
#        n = 3, m = 5
# Sample Output 1:
# [{1,2,3}, {1,2,4}, {1,5,6}, {3,4,5}, {5,6,2}]

# Task 3
# 3.1
from itertools import groupby

# Sample data as a list of tuples (manufacturer, model)
data = [
    ("Toyota", "Camry"),
    ("Toyota", "Corolla"),
    ("Honda", "Civic"),
    ("Honda", "Accord"),
    ("Ford", "Fusion"),
    ("Ford", "Mustang"),
]

# Sort the data by manufacturer (required for groupby to work)
sorted_data = sorted(data, key=lambda x: x[0])

# Group the data by manufacturer
grouped_data = groupby(sorted_data, key=lambda x: x[0])

# Print the table output
for manufacturer, models in grouped_data:
    model_count = len(list(models))
    model_list = [model for _, model in models]

    print(f"MANUFACTURER: {manufacturer}")
    print(f"Count of Models: {model_count}")
    print("Car Models:")

    for model in model_list:
        print(f" - {model}")

    print()


