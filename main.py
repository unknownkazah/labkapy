print("Task 1.1")

print(f"{4} {8} {15} {16} {23} {42}")

print("Task 1.2")
print(f"{4}\n{8}\n{15}\n{16}\n{23}\n{42}")


print("Task 1.3")
try:
    num1 = int(input("Insert a num 1\n"))
    print(num1)
    print(num1+1)
    print(num1+2)
except:
    print("insert a number please")

print("Task 1.4")

try:
    num2 = int(input("Insert a number 1\n"))
    num3 = int(input("Insert a number 2\n"))
    num4 = int(input("Insert a number 4\n"))
    print(num2 + num3 + num4)
except:
    print("Insert a integer type valie please")

print("Task 1.5")

edge_length = float(input("Enter the edge length of the cube: "))


volume = edge_length ** 3


surface_area = 6 * (edge_length ** 2)


print(f"volume {volume}")
print(f"surface area {surface_area}")

print("Task 2. Arithmetic, logic and bitwise ops.")


print("Task 2.1")

# Вводим количество школьников (N) и количество мандаринов (K)
N = int(input("Введите количество школьников: "))
K = int(input("Введите количество мандаринов: "))

# Вычисляем, сколько мандаринов получит каждый ученик
mandarins_per_student = K // N  # Используем оператор "//" для целочисленного деления

# Вычисляем, сколько мандаринов останется в корзинке
remaining_mandarins = K % N  # Используем оператор "%" для получения остатка от деления

# Выводим результаты
print(f"Каждый ученик получит {mandarins_per_student} целых мандаринов.")
print(f"В корзинке останется {remaining_mandarins} целых мандаринов.")

# 2.2 Write a program to find the digits of a four-digit number. [ 10 point ]

print("Task 2.2")

# Input a four-digit number from the user
number = int(input("Enter a four-digit number: "))

# Check if the input number is indeed four digits
if 1000 <= number <= 9999:
    # Extract each digit using integer division and modulo
    thousands_digit = number // 1000
    hundreds_digit = (number // 100) % 10
    tens_digit = (number // 10) % 10
    ones_digit = number % 10

    # Print the digits
    print(f"Thousands Digit: {thousands_digit}")
    print(f"Hundreds Digit: {hundreds_digit}")
    print(f"Tens Digit: {tens_digit}")
    print(f"Ones Digit: {ones_digit}")
else:
    print("Please enter a valid four-digit number.")

print("Task 2.3")
# Вводим начальное количество жителей вселенной
population = int(input("Введите начальное количество жителей вселенной: "))

# Проверяем, является ли количество жителей нечетным
if population % 2 == 1:
    # Если количество жителей нечетное, то округляем вверх до ближайшего четного числа
    survivors = (population + 1) // 2
else:
    # Если количество жителей четное, то просто делим пополам
    survivors = population // 2

# Выводим количество выживших
print(f"Количество выживших: {survivors}")

print("Task 2.4")
# 2.4 Write a code that accepts a number as input from the user, and performs “<<” and outputs the result.
# If the result is zero the code should output the warning message.  [ 10 point ]

try:
    # Get a number from the user
    number = int(input("Enter a number: "))

    # Perform the left shift operation "<<"
    result = number << 1

    if result == 0:
        print("Warning: The result is zero.")
    else:
        print(f"The result of << is {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
except Exception as e:
    print(f"An error occurred: {e}")

    print("Task 2.5")

    try:
        # Запросите два числа у пользователя
        first_number = float(input("Пожалуйста, введите первое число: "))
        second_number = float(input("Пожалуйста, введите второе число: "))

        # Запросите выбор операции у пользователя
        operation = input("Пожалуйста, выберите операцию (+, -, *, /): ")

        # Выполните выбранную операцию и отобразите результат
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            if second_number == 0:
                print("Ошибка: Деление на ноль.")
            else:
                result = first_number / second_number
                print(f"{first_number} {operation} {second_number} = {result:.3f}")
        else:
            print("Недопустимая операция. Пожалуйста, выберите +, -, *, или /.")
    except ValueError:
        print("Недопустимый ввод. Пожалуйста, введите действительные числа.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
