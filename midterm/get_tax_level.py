def get_tax_level(name, salary):
  """Calculates and outputs the tax level for a given user name and salary.

  Args:
    name: The user name.
    salary: The desired salary level.

  Returns:
    None.
  """

  try:
    salary = float(salary)
  except ValueError:
    print(f"{name}, please enter your desired salary as a digit.")
    return

  tax_level = salary * 0.2
  print(f"{name}, the tax level you will pay with the salary {salary} is {tax_level}")


def main():
  name = input("Enter your name please: ")
  salary = input("Enter your desired salary level: ")

  get_tax_level(name, salary)


if __name__ == "__main__":
  main()


