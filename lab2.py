# Problem 1: Check if the sum of two numbers equals the absolute difference of two other numbers

def is_sum_equal_to_difference():
    try:
        number = int(input("Enter a four-digit number: "))
        if 1000 <= number <= 9999:
            thousands, hundreds, tens, ones = number // 1000, (number % 1000) // 100, (number % 100) // 10, number % 10
            if thousands + ones == abs(tens - hundreds):
                print("YES")
            else:
                print("NO")
        else:
            print("Invalid input. Enter a four-digit number.")
    except ValueError:
        print("Invalid input.")

# Problem 2: Check age for access to something

def check_age_access():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            age = int(input("Enter your age: "))
            if age >= 18:
                print("Access granted")
            else:
                print("Access denied")
    except ValueError:
        print("Invalid input.")

# Problem 3: Check if three numbers are consecutive

def are_three_numbers_consecutive():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            n1, n2, n3 = map(int, input("Enter three numbers separated by spaces: ").split())
            if n2 - n1 == 1 and n3 - n2 == 1:
                print("Yes")
            else:
                print("No")
    except ValueError:
        print("Invalid input.")

# Problem 4: Check if two positions are in the same line (horizontal or vertical)

def are_positions_on_one_line():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            col1, row1, col2, row2 = map(int, input("Enter coordinates of two positions separated by spaces: ").split())
            if col1 == col2 or row1 == row2:
                print("Yes")
            else:
                print("No")
    except ValueError:
        print("Invalid input.")

# Problem 5: Check if two positions are adjacent (king's move)

def are_king_positions_adjacent():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            king_col1, king_row1, king_col2, king_row2 = map(int, input("Enter coordinates of two king positions separated by spaces: ").split())
            if abs(king_col1 - king_col2) <= 1 and abs(king_row1 - king_row2) <= 1:
                print("Yes")
            else:
                print("No")
    except ValueError:
        print("Invalid input.")

# Problem 6: Calculate the average of three numbers

def calculate_average():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            num_a, num_b, num_c = map(int, input("Enter three numbers separated by spaces: ").split())
            average = (num_a + num_b + num_c) / 3
            print("Average:", average)
    except ValueError:
        print("Invalid input.")

# Problem 7: Get the number of days in a given month

def get_days_in_month():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            month = int(input("Enter a month (1-12): "))
            if 1 <= month <= 12:
                days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                num_days = days_in_month[month - 1]
                print("Number of days:", num_days)
            else:
                print("Invalid month")
    except ValueError:
        print("Invalid input.")

# Problem 8: Determine weight category

def determine_weight_category():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            weight = int(input("Enter weight: "))
            if weight <= 60:
                print("Lightweight")
            elif 60 < weight <= 64:
                print("Featherweight")
            elif 64 < weight <= 69:
                print("Light Middleweight")
            else:
                print("Invalid weight category")
    except ValueError:
        print("Invalid input.")

# Problem 9: Check if two passwords match

def check_passwords_match():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            password = input("Enter a password: ")
            password_check = input("Repeat the password: ")
            if password_check == password:
                print("Password accepted")
            else:
                print("Passwords do not match")
    except ValueError:
        print("Invalid input.")

# Problem 10: Check if a number is even or odd

def check_even_or_odd():
    try:
        num_tests = int(input("Enter the number of tests: "))
        for _ in range(num_tests):
            num = int(input("Enter a number: "))
            if num % 2 == 0:
                print("Even number")
            else:
                print("Odd number")
    except ValueError:
        print("Invalid input.")
