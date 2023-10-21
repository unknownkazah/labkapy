def calculate(operation, a, b):
  """Calculates the result of the given operation on the given two numbers.

  Args:
    operation: The arithmetic operation to perform.
    a: The first number.
    b: The second number.

  Returns:
    The result of the operation.
  """

  if operation == 1:
    return a + b
  elif operation == 2:
    return a * b
  elif operation == 3:
    return a / b
  elif operation == 4:
    return a ** b
  else:
    raise ValueError("Invalid operation.")


def main():
  print("Please chose the task you want to perform:")
  print("1. Addition")
  print("2. Multiplication")
  print("3. Division")
  print("4. Exponentiation")

  operation = int(input("User Input: "))

  print("Please enter two numbers for addition, comma separated")

  a, b = input("User Input: ").split(",")

  a = float(a)
  b = float(b)

  result = calculate(operation, a, b)

  print(f"The result is: {result}")


if __name__ == "__main__":
  main()
