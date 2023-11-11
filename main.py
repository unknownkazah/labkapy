from lab6 import *

# Пример данных
example_dict = {'a': True, 'b': False, 'c': True}
example_list = [1, 2, 2, 3, 4, 4, 5]
example_date = "2023.11.11"
example_string = "This is an example string with some words."
example_shopping_list = [
    {"item": "apple", "price": 1.5},
    {"item": "banana", "price": 0.75},
    {"item": "chocolate", "price": 2.0},
]

# Использование функций
keys_with_true_value = get_keys_with_value_true(example_dict)
unique_elements_list = get_unique_elements(example_list)
date_in_format = get_date_in_format(example_date)
elements_with_two_occurrences = get_elements_with_no_more_than_two_occurrences(example_list)
words_from_string = get_words_from_string(example_string)
unique_elements_with_count = get_unique_elements_with_count(example_list)
prime_numbers_up_to_10 = get_prime_numbers(10)
prime_numbers_in_list = get_prime_numbers_in_list(example_list)
difference_between_dates = get_difference_between_dates("2023.11.10", "2023.11.11")
perfect_numbers_in_list = get_perfect_numbers_from_list([6, 28, 12, 15])
perfect_squares_in_list = get_perfect_squares_from_list([4, 9, 16, 25])
sorted_shopping_list = sort_shopping_list_by_price(example_shopping_list)
words_starting_with_vowel = get_words_starting_with_vowel(words_from_string)

# Вывод результатов
print("Ключи с значением True:", keys_with_true_value)
print("Уникальные элементы:", unique_elements_list)
print("Дата в формате:", date_in_format)
print("Элементы с не более чем двумя появлениями:", elements_with_two_occurrences)
print("Слова из строки:", words_from_string)
print("Уникальные элементы с количеством:", unique_elements_with_count)
print("Простые числа до 10:", prime_numbers_up_to_10)
print("Простые числа в списке:", prime_numbers_in_list)
print("Разница между датами:", difference_between_dates)
print("Совершенные числа в списке:", perfect_numbers_in_list)
print("Квадраты чисел в списке:", perfect_squares_in_list)
print("Отсортированный список покупок:", sorted_shopping_list)
print("Слова, начинающиеся с гласной:", words_starting_with_vowel)