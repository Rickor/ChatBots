tasks = []

def show_help():
    print("""
 Commands:
  - add <task>         : Add a new task
  - remove <task>      : Remove a task
  - show               : Show all tasks
  - clear              : Remove all tasks
  - help               : Show this help menu
  - exit               : Quit the bot
""")

def todo_bot():
    print(" Welcome to your To-Do Bot!")
    show_help()
    while True:
        command = input(" Enter command: ").strip().lower()
        if command.startswith("add "):
            task = command[4:]
            tasks.append(task)
            print(f" Added: '{task}'")
        elif command.startswith("remove "):
            task = command[7:]
            if task in tasks:
                tasks.remove(task)
                print(f" Removed: '{task}'")
            else:
                print(" Task not found.")
        elif command == "show":
            if not tasks:
                print(" No tasks yet.")
            else:
                print(" Your tasks:")
                for i, t in enumerate(tasks, start=1):
                    print(f"  {i}. {t}")
        elif command == "clear":
            tasks.clear()
            print(" All tasks cleared.")
        elif command == "help":
            show_help()
        elif command == "exit":
            print(" Goodbye!")
            break
        else:
            print(" Unknown command. Type 'help'.")

# Run code
todo_bot()
