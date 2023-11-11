# def create_list(user_input):
#     user_input = user_input.lower()
#
#     list_of_symbols = []
#
#     for symbol in user_input:
#         list_of_symbols.append(symbol)
#
#     return list_of_symbols
#
#
# def count_symbol_frequency(list_of_symbols):
#     symbol_frequency_map = {}
#
#     for symbol in list_of_symbols:
#         if symbol in symbol_frequency_map:
#             symbol_frequency_map[symbol] += 1
#         else:
#             symbol_frequency_map[symbol] = 1
#
#     symbol_frequency_list = []
#     for symbol, frequency in symbol_frequency_map.items():
#         symbol_frequency_list.append((symbol, frequency))
#
#     return symbol_frequency_list
#
#
# def classify_symbols(symbol_frequency_list):
#     vowels = set('aeiouy')
#     consonants = set('bcdfghjklmnpqrstvwxz')
#     symbols = set('!@#$%^&*()-_+={}[]|\\:;"\'<>,./?')
#
#     list_vow = []
#     list_cons = []
#     list_symb = []
#
#     for symbol, frequency in symbol_frequency_list:
#         if symbol in vowels:
#             list_vow.append((symbol, frequency))
#         elif symbol in consonants:
#             list_cons.append((symbol, frequency))
#         else:
#             list_symb.append((symbol, frequency))
#
#     return list_vow
#
#
# def create_student_dictionary(student_name, assignment_scores, lab_scores, test_scores):
#     student_dictionary = {}
#     student_dictionary['name'] = student_name
#     student_dictionary['assignment'] = assignment_scores
#     student_dictionary['lab'] = lab_scores
#     student_dictionary['test'] = test_scores
#
#     return student_dictionary
#
#
# def check_submission_rate(student_dictionary):
#     submission_rate_dictionary = {}
#     submission_rate = 0
#
#     # Check the number of assignments submitted.
#     if len(student_dictionary['assignment']) == 4:
#         submission_rate += 1
#
#     # Check the number of labs submitted.
#     if len(student_dictionary['lab']) == 2:
#         submission_rate += 1
#
#     # Check the number of tests submitted.
#     if len(student_dictionary['test']) == 2:
#         submission_rate += 1
#
#     submission_rate_dictionary[student_dictionary['name']] = submission_rate
#
#     return submission_rate_dictionary
#
#
# def calculate_final_grade(student_dictionary, submission_rate_dictionary):
#     final_grade = 0
#
#     # Check if the student submitted at least 4 activities.
#     student_name = student_dictionary['name']
#     if submission_rate_dictionary.get(student_name, 0) >= 4:
#         # Calculate the average assignment score.
#         average_assignment_score = sum(student_dictionary['assignment']) / len(student_dictionary['assignment'])
#
#         # Calculate the average lab score.
#         average_lab_score = sum(student_dictionary['lab']) / len(student_dictionary['lab'])
#
#         # Calculate the average test score.
#         average_test_score = sum(student_dictionary['test']) / len(student_dictionary['test'])
#
#         # Calculate the final grade as a weighted average.
#         final_grade = (average_assignment_score * 0.4 + average_lab_score * 0.3 + average_test_score * 0.3)
#
#     return final_grade
#
#
# def register_transactions(transactions):
#     stats = {}
#
#     for user_id, transaction_type in transactions:
#         if user_id not in stats:
#             stats[user_id] = {}
#             stats[user_id]['max_transaction_type'] = transaction_type
#             stats[user_id]['min_transaction_type'] = transaction_type
#             stats[user_id][transaction_type] = 1
#         else:
#             if transaction_type not in stats[user_id]:
#                 stats[user_id][transaction_type] = 1
#             else:
#                 stats[user_id][transaction_type] += 1
#
#             if transaction_type > stats[user_id]['max_transaction_type']:
#                 stats[user_id]['max_transaction_type'] = transaction_type
#
#             if transaction_type < stats[user_id]['min_transaction_type']:
#                 stats[user_id]['min_transaction_type'] = transaction_type
#
#     return stats
#
#
# user_input = "Hello, World!"
# symbol_list = create_list(user_input)
# print(symbol_list)  # Вывод: ['h', 'e', 'l', 'l', 'o', ',', ' ', 'w', 'o', 'r', 'l', 'd', '!']
#
# user_input = "Hello, World!"
# symbol_list = create_list(user_input)
# frequency_list = count_symbol_frequency(symbol_list)
# print(
#     frequency_list)  # Вывод: [('h', 1), ('e', 1), ('l', 3), ('o', 2), (',', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1), ('!', 1)]
#
# user_input = "Hello, World!"
# symbol_list = create_list(user_input)
# frequency_list = count_symbol_frequency(symbol_list)
# classified_symbols = classify_symbols(frequency_list)
# print(classified_symbols)  # Вывод: [('e', 1), ('o', 2), ('w', 1), ('r', 1), ('d', 1)]
#
# student_name = "John"
# assignment_scores = [90, 85, 92, 88]
# lab_scores = [95, 88]
# test_scores = [78, 85]
# student_dict = create_student_dictionary(student_name, assignment_scores, lab_scores, test_scores)
# print(student_dict)  # Вывод: {'name': 'John', 'assignment': [90, 85, 92, 88], 'lab': [95, 88], 'test': [78, 85]}
#
# student_dict = create_student_dictionary("John", [90, 85, 92, 88], [95, 88], [78, 85])
# submission_rate_dict = check_submission_rate(student_dict)
# print(submission_rate_dict)  # Вывод: {'John': 1}
#
# student_dict = create_student_dictionary("John", [90, 85, 92, 88], [95, 88], [78, 85])
# submission_rate_dict = check_submission_rate(student_dict)
# final_grade = calculate_final_grade(student_dict, submission_rate_dict)
# print(final_grade)  # Вывод: 88.1 (предполагая, что студент сдал хотя бы 4 элемента)
#
# transactions = [("user1", "purchase"), ("user2", "refund"), ("user1", "purchase"), ("user2", "purchase")]
# transaction_stats = register_transactions(transactions)
# print(transaction_stats)
# # Вывод: {'user1': {'max_transaction_type': 'purchase', 'min_transaction_type': 'purchase', 'purchase': 2},
# #         'user2': {'max_transaction_type': 'refund', 'min_transaction_type': 'refund', 'refund': 1, 'purchase': 1}}




def teacher(name,age,subject):

  teacher_dict = {}
  teacher_dict['name'] = name
  teacher_dict['age'] = age
  teacher_dict['subject'] = subject

  return teacher_dict


teacher_name = "Nazzere"
teacher_age = 20
teacher_dict ="Python Practice"
teacher_d = teacher(teacher_name, teacher_age, teacher_dict)
print(teacher_d.get("subject"))



