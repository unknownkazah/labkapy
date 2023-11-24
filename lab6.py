from datetime import datetime
def get_keys_with_value_true(dictionary):
    result = []
    for key, value in dictionary.items():
        if value:
            result.append(key)
    return result


def get_unique_elements(input_list):
    return list(set(input_list))


def get_date_in_format(date):
        date_object = datetime.strptime(date, '%Y.%m.%d')

        formatted_date = date_object.strftime('%d.%m.%Y')
        return formatted_date

print(get_date_in_format('2023.10.23'))


def get_elements_with_no_more_than_two_occurrences(input_list):
    element_count = {}
    result = []
    for element in input_list:
        element_count[element] = element_count.get(element, 0) + 1
        if element_count[element] <= 2:
            result.append(element)
    return result


def get_words_from_string(input_string):
    return input_string.split()


def get_unique_elements_with_count(input_list):

    unique_elements_with_count = {}
    for element in input_list:
        unique_elements_with_count[element] = unique_elements_with_count.get(element, 0) + 1
    return unique_elements_with_count


def get_prime_numbers(n):
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


def get_prime_numbers_in_list(input_list):
    primes = get_prime_numbers(max(input_list, default=0))
    result = []
    for element in input_list:
        if element in primes:
            result.append(element)
    return result


def get_difference_between_dates(date1, date2):
    from datetime import datetime
    date1 = datetime.strptime(date1, "%Y.%m.%d")
    date2 = datetime.strptime(date2, "%Y.%m.%d")
    difference = date2 - date1
    return difference.days

def is_perfect_number(num):

    if num < 2:
        return False
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i
    return divisors_sum == num

def get_perfect_numbers_from_list(input_list):
    # Возвращает список элементов, являющихся числами-совершенными.
    result = []
    for element in input_list:
        if is_perfect_number(element):
            result.append(element)
    return result

def is_perfect_square(num):
    return num > 0 and (num**0.5).is_integer()

def get_perfect_squares_from_list(input_list):
    result = []
    for element in input_list:
        if is_perfect_square(element):
            result.append(element)
    return result


def sort_shopping_list_by_price(shopping_list):
    # Возвращает отсортированный по цене список покупок.
    return sorted(shopping_list, key=lambda item: item["price"])


def get_words_starting_with_vowel(words):
    # Возвращает список слов, начинающихся с гласной буквы.
    result = []
    for word in words:
        if word[0].lower() in "aeiou":
            result.append(word)
    return result

