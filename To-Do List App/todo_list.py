todos = []

def add_task(task):
        todos.append({"task": task, "done": False})
        print("Task added!")

def show_tasks():
    print()
    if todos:
        for index, task in enumerate(todos):
            status = "Done" if todos[index]["done"] else "Not done"
            print(f"{index + 1}. {task['task']} - {status}")
    
    else:
         print("Tasks not found.")

def mark_task(index):
    if 0 <= index < len(todos):
         todos[index]['done'] = True
         print(f"Task ({todos[index]['task']}) is marked as Done!")
    
    else:
         print("Invalid index.")


def main():
    while True:
        print("==== To-Do List (CLI Version) ====")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Mark the task as done")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
             n_tasks = int(input("How many tasks do you want to add: "))

             for i in range(n_tasks):
                task = input("\nEnter your task: ")
                add_task(task)

        elif choice == 2:
             show_tasks()

        elif choice == 3:
             show_tasks()
             index = int(input("\nEnter the task number to mark as done: ")) -1
             mark_task(index)

        elif choice == 4:
             print("Exiting the To-Do List.")
             break
        
        else:
             print("Invalid choice.")


if __name__ == '__main__':
    main()