def create_list(user_input):
  """
  Создает список из введенной пользователем строки с пробелами. Все символы в списке будут в нижнем регистре.

  Args:
    user_input: Введенная пользователем строка с пробелами.

  Returns:
    A list containing all symbols from the user input string in lower case.
  """

  # Преобразуем строку в нижний регистр

  user_input = user_input.lower()

  # Создаем пустой список

  list_of_symbols = []

  # Проходим по строке, добавляя каждый символ в список

  for symbol in user_input:
    list_of_symbols.append(symbol)

  # Возвращаем список

  return list_of_symbols


def count_symbol_frequency(list_of_symbols):
  """
  Подсчитывает частоту встречаемости каждого символа в списке и возвращает результаты в виде списка кортежей. Каждый кортеж содержит символ и его частоту встречаемости.

  Args:
    list_of_symbols: Список символов.

  Returns:
    A list of tuples containing symbols and their frequency of occurrence.
  """

  # Создаем словарь для хранения частоты встречаемости символов

  symbol_frequency_map = {}

  # Проходим по списку символов, добавляя каждый символ в словарь

  for symbol in list_of_symbols:
    if symbol in symbol_frequency_map:
      symbol_frequency_map[symbol] += 1
    else:
      symbol_frequency_map[symbol] = 1

  # Создаем список кортежей, содержащих символы и их частоту встречаемости

  symbol_frequency_list = []
  for symbol, frequency in symbol_frequency_map.items():
    symbol_frequency_list.append((symbol, frequency))

  # Возвращаем список

  return symbol_frequency_list


def classify_symbols(symbol_frequency_list):
  """
  Классифицирует символы в списке на гласные, согласные и символы.

  Args:
    symbol_frequency_list: Список кортежей, содержащих символы и их частоту встречаемости.

  Returns:
    A tuple of three lists: list_vow, list_cons, list_symb.
  """

  # Создаем множества гласных, согласных и символов

  vowels = set('aeiouy')
  consonants = set('bcdfghjklmnpqrstvwxz')
  symbols = set('!@#$%^&*()-_+={}[]|\\:;"\'<>,./?')

  # Создаем пустые списки для хранения гласных, согласных и символов

  list_vow = []
  list_cons = []
  list_symb = []

  # Проходим по списку кортежей, добавляя каждый символ в соответствующий список

  for symbol, frequency in symbol_frequency_list:
    if symbol in vowels:
      list_vow.append((symbol, frequency))
    elif symbol in consonants:
      list_cons.append((symbol, frequency))
    else:
      list_symb.append((symbol, frequency))

  # Возвращаем кортеж из трех списков

  return (list_v


def create_student_dictionary(student_name, assignment_scores, lab_scores, test_scores):
  """
  Creates a dictionary to store student information, including their name, assignment scores, lab scores, and test scores.

  Args:
    student_name: The name of the student.
    assignment_scores: A list of the student's assignment scores.
    lab_scores: A list of the student's lab scores.
    test_scores: A list of the student's test scores.

  Returns:
    A dictionary containing the student's information.
  """

  student_dictionary = {}
  student_dictionary['name'] = student_name
  student_dictionary['assignment'] = assignment_scores
  student_dictionary['lab'] = lab_scores
  student_dictionary['test'] = test_scores

  return student_dictionary


def check_submission_rate(student_dictionary):
  """
  Checks if the student submitted all 6 activities (4 assignments, 2 labs, and 2 tests).

  Args:
    student_dictionary: A dictionary containing the student's information.

  Returns:
    A dictionary containing the student's name and their submission rate.
  """

  submission_rate_dictionary = {}
  submission_rate = 0

  # Check the number of assignments submitted.
  if len(student_dictionary['assignment']) == 4:
    submission_rate += 1

  # Check the number of labs submitted.
  if len(student_dictionary['lab']) == 2:
    submission_rate += 1

  # Check the number of tests submitted.
  if len(student_dictionary['test']) == 2:
    submission_rate += 1

  submission_rate_dictionary[student_dictionary['name']] = submission_rate

  return submission_rate_dictionary


def calculate_final_grade(student_dictionary, submission_rate_dictionary):
  """
  Calculates the final grade for a student based on their assignment scores, lab scores, test scores, and submission rate.

  Args:
    student_dictionary: A dictionary containing the student's information.
    submission_rate_dictionary: A dictionary containing the student's name and their submission rate.

  Returns:
    A dictionary containing the student's information, including their final grade.
  """

  final_grade = 0

  # Check if the student submitted at least 4 activities.
  if submission_rate_dictionary[student_dictionary['name']] >= 4:
    # Calculate the average assignment score.
    average_assignment_score = sum(student_dictionary['assignment']) / len(student_dictionary['assignment'])

    # Calculate the average lab score.
    average_lab_score = sum(student_dictionary['lab']) / len(student_dictionary['lab'])

    # Calculate the average test score.
    average_test_score = sum(student_dictionary['test'])


def register_transactions(transactions):
  """Registers transactions made by users and stores the statistics in a dictionary.

  Args:
    transactions: A list of tuples, where each tuple contains a user ID and a transaction type.

  Returns:
    A dictionary, where the keys are user IDs and the values are dictionaries containing the statistics for that user.
  """

  stats = {}

  for user_id, transaction_type in transactions:
    if user_id not in stats:
      stats[user_id] = {}
      stats[user_id]['mft'] = transaction_type
      stats[user_id]['lft'] = transaction_type

    stats[user_id][transaction_type] += 1

    if stats[user_id][transaction_type] > stats[user_id]['mft']:
      stats[user_id]['mft'] = transaction_type

    if stats[user_id][transaction_type] < stats[user_id]['lft']:
      stats[user_id]['lft'] = transaction_type

  return stats
