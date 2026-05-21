#!/usr/bin/env python3
import subprocess

def clear_all_tasks():
    result = subprocess.run(
        ["todo", "list"],
        capture_output=True,
        text=True
    )

    lines = result.stdout.strip().split("\n")

    indices = []
    for line in lines:
        if line.strip():
            idx = line.split()[0]
            indices.append(int(idx))

    for i in sorted(indices, reverse=True):
        subprocess.run(["todo", "rm", str(i)])

def todo():
    while True:
        act = int(input("Enter the process to be executed :\n 1. Add task\n " \
        "2. Task Completed\n 3. Clear List\n " \
        "4. Display list\n 5. Sort List\n 6. Exit\n   >>> "))
        list = []

        if act == 101:
            subprocess.run(["todo","--help"])
            break

        elif act == 6:
            print("You are Done for now")
            break

        elif act == 3:
            confirm = input("Clear all tasks? (y/n): ")

            if confirm.lower() == 'y':
                clear_all_tasks()
                print("All tasks cleared.")
            else:
                print("Cancelled.")
            break
            
        elif act == 5:
            subprocess.run(["todo","sort"])
            print("\n##############\n##############")
            subprocess.run(["todo","list"])
            print("\n##############\n##############")


        elif act == 4:
            print("\n##############\n##############")
            subprocess.run(["todo","list"])
            print("\n##############\n##############")

        elif act == 1:
            num = int(input('how many tasks : '))
            for i in range(num):
                task = input(f"Enter task number {i+1} here >> ")
                list.append(task)
            subprocess.run(["todo","add",*list])

        elif act == 2:
            n = str(int(input("Enter task index here >> ")))
            subprocess.run(["todo","done",n])

        else:
            print("\n##Invalid Option##\n")
            break
todo()
