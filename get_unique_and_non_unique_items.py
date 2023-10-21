def get_unique_and_non_unique_items(items):
  """Stores unique items in a set and non-unique items in a nested tuple.

  Args:
    items: A list of items.

  Returns:
    A tuple of the set of unique items and the nested tuple of non-unique items.
  """

  unique_items = set()
  non_unique_items = {}

  for item in items:
    if item in non_unique_items:
      non_unique_items[item] += 1
    else:
      non_unique_items[item] = 1
      unique_items.add(item)

  non_unique_items = tuple((item, count) for item, count in non_unique_items.items() if count > 1)
  return unique_items, non_unique_items


def main():
  print("Please chose the task you want to perform:")
  print("1. Enter items")
  print("2. Exit")

  user_input = input("User Input: ")

  if user_input == "1":
    items = input("Please enter items separated by comma\n").split(",")

    unique_items, non_unique_items = get_unique_and_non_unique_items(items)

    print("Items are saved")
    print(f"Unique items: {unique_items}")
    print(f"Not unique items: {non_unique_items}")
  elif user_input == "2":
    exit()
  else:
    print("Invalid input.")
    main()


if __name__ == "__main__":
  main()
