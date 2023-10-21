def fibonacci(n):
  """Generates a Fibonacci sequence of the given length.

  Args:
    n: The length of the Fibonacci sequence.

  Returns:
    A list of the Fibonacci numbers.
  """

  fibonacci_sequence = []

  for i in range(n):
    if i < 2:
      fibonacci_sequence.append(1)
    else:
      fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

  return fibonacci_sequence


def main():
  n = int(input("Please enter the length of Fibonacci sequence\n"))

  fibonacci_sequence = fibonacci(n)

  print(f"The Fibonacci sequence for {n} is")
  print(", ".join(map(str, fibonacci_sequence)))


if __name__ == "__main__":
  main()
