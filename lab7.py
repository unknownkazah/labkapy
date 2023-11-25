import random

file_path = '/Users/rakhmet_zhanserik/Desktop/labkapy/text.txt'
def read_and_display(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found.")

# Usage
read_and_display('text.txt')

def read_random_line(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
            print(random_line.strip())
    except FileNotFoundError:
        print("File not found.")

# Usage
read_random_line('text.txt')

def count_uppercase_chars(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            print("Uppercase characters count:", uppercase_count)
    except FileNotFoundError:
        print("File not found.")

# Usage
count_uppercase_chars('text.txt')

def count_lines_not_starting_with_D(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            count = sum(1 for line in lines if not line.startswith('D'))
            print("Number of lines not starting with 'D':", count)
    except FileNotFoundError:
        print("File not found.")

# Usage
count_lines_not_starting_with_D('text.txt')


def count_words_ending_with_F(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            count = sum(1 for word in words if word.lower().endswith('f'))
            print("Number of words ending with 'F' or 'f':", count)
    except FileNotFoundError:
        print("File not found.")

# Usage
count_words_ending_with_F('text.txt')

def count_all_and_none_words(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            all_count = words.count("all")
            none_count = words.count("none")
            print("'all' count:", all_count)
            print("'none' count:", none_count)
    except FileNotFoundError:
        print("File not found.")

# Usage
count_all_and_none_words('text.txt')

def count_word_frequency(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            word_freq = {}
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1
            print("Word frequency:", word_freq)
    except FileNotFoundError:
        print("File not found.")

# Usage
count_word_frequency('text.txt')


def find_longest_word(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            longest_word = max(words, key=len)
            print("Longest word:", longest_word)
    except FileNotFoundError:
        print("File not found.")

# Usage
find_longest_word('text.txt')

def replace_B_with_J(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            corrected_content = content.replace('B', 'J')
            print("Corrected content:")
            print(corrected_content)
    except FileNotFoundError:
        print("File not found.")

# Usage
replace_B_with_J('text.txt')

def count_A_and_B_characters(file_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            count_a = content.lower().count('a')
            count_b = content.lower().count('b')
            print(f"a={count_a}, b={count_b}")
    except FileNotFoundError:
        print("File not found.")

# Usage
count_A_and_B_characters('text.txt')



