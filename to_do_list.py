# Simple To-Do List Program

tasks = []  # to store all tasks

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added!")

    elif choice == "2":
        print("\nYour Tasks:")
        if not tasks:
            print("No tasks yet!")
        else:
            for i, t in enumerate(tasks):
                status = "✔️ Done" if t["done"] else "❌ Not done"
                print(f"{i+1}. {t['task']} - {status}")

    elif choice == "3":
        num_str = input("Enter task number to mark complete: ")
        if num_str.isdigit():  
            num = int(num_str)  
            if 0 < num <= len(tasks):
                tasks[num-1]["done"] = True
                print("✅ Task marked as complete!")
            else:
                print("Invalid task number.")
        else:
            print("Please enter a valid number.")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice, please try again.")
