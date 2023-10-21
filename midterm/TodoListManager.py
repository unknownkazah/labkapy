class TodoListManager:
  def __init__(self):
    self.to_do_list = []
    self.completed_tasks = []

  def add_task(self, task):
    self.to_do_list.append(task)

  def view_all_tasks(self):
    print("To-do list:")
    for task in self.to_do_list:
      print(task)

  def mark_task_as_completed(self, task):
    self.to_do_list.remove(task)
    self.completed_tasks.append(task)

  def view_all_completed_tasks(self):
    print("Completed tasks:")
    for task in self.completed_tasks:
      print(task)

  def run(self):
    while True:
      print("Please chose the task you want to perform:")
      print("1. Add Task")
      print("2. View All Tasks")
      print("3. Mark Task as Completed")
      print("4. View All Completed Tasks")
      print("5. Exit")

      user_input = input("User Input: ")

      if user_input == "1":
        task = input("Enter the task: ")
        self.add_task(task)
      elif user_input == "2":
        self.view_all_tasks()
      elif user_input == "3":
        task = input("Enter the name of the task: ")
        self.mark_task_as_completed(task)
      elif user_input == "4":
        self.view_all_completed_tasks()
      elif user_input == "5":
        break
      else:
        print("Invalid input.")


if __name__ == "__main__":
  to_do_list_manager = TodoListManager()
  to_do_list_manager.run()
