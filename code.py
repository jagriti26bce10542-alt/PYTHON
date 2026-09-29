print("===================================")
print("     SMART STUDENT LIFE MANAGER")
print("===================================")

# Data storage
expenses = []
attendance = {}
tasks = []


while True:

    print("\n1. Expense Manager")
    print("2. Attendance Manager")
    print("3. Task Manager")
    print("4. Analytics")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    # ================= EXPENSE MANAGER =================

    if choice == "1":

        while True:

            print("\n----- EXPENSE MANAGER -----")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Total Expenses")
            print("4. Back to Main Menu")

            expense_choice = input("\nEnter your choice: ")

            if expense_choice == "1":

                name = input("Enter expense name: ")
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")

                expense = {
                    "name": name,
                    "amount": amount,
                    "category": category
                }

                expenses.append(expense)

                print("\nExpense added successfully!")

            elif expense_choice == "2":

                if len(expenses) == 0:
                    print("\nNo expenses recorded.")

                else:
                    print("\n----- YOUR EXPENSES -----")

                    for i in range(len(expenses)):
                        print(
                            i + 1,
                            ".",
                            expenses[i]["name"],
                            "- Rs.",
                            expenses[i]["amount"],
                            "-",
                            expenses[i]["category"]
                        )

            elif expense_choice == "3":

                total = 0

                for expense in expenses:
                    total = total + expense["amount"]

                print("\nTotal Expenses = Rs.", total)

            elif expense_choice == "4":
                break

            else:
                print("\nInvalid choice. Please try again.")


    # ================= ATTENDANCE MANAGER =================

    elif choice == "2":

        while True:

            print("\n----- ATTENDANCE MANAGER -----")
            print("1. Add Subject")
            print("2. View Attendance")
            print("3. Back to Main Menu")

            attendance_choice = input("\nEnter your choice: ")

            if attendance_choice == "1":

                subject = input("Enter subject name: ")
                attended = int(input("Enter classes attended: "))
                total = int(input("Enter total classes: "))

                percentage = (attended / total) * 100

                attendance[subject] = {
                    "attended": attended,
                    "total": total,
                    "percentage": percentage
                }

                print("\nAttendance added successfully!")

            elif attendance_choice == "2":

                if len(attendance) == 0:
                    print("\nNo attendance records found.")

                else:

                    print("\n----- ATTENDANCE -----")

                    for subject in attendance:

                        attended = attendance[subject]["attended"]
                        total = attendance[subject]["total"]
                        percentage = attendance[subject]["percentage"]

                        print(
                            subject,
                            ":",
                            attended,
                            "/",
                            total,
                            "=>",
                            round(percentage, 2),
                            "%"
                        )

            elif attendance_choice == "3":
                break

            else:
                print("\nInvalid choice. Please try again.")


    # ================= TASK MANAGER =================

    elif choice == "3":

        while True:

            print("\n----- TASK MANAGER -----")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Back to Main Menu")

            task_choice = input("\nEnter your choice: ")

            if task_choice == "1":

                task_name = input("Enter task: ")

                task = {
                    "name": task_name,
                    "completed": False
                }

                tasks.append(task)

                print("\nTask added successfully!")

            elif task_choice == "2":

                if len(tasks) == 0:
                    print("\nNo tasks available.")

                else:

                    print("\n----- YOUR TASKS -----")

                    for i in range(len(tasks)):

                        if tasks[i]["completed"]:
                            status = "Completed"
                        else:
                            status = "Pending"

                        print(
                            i + 1,
                            ".",
                            tasks[i]["name"],
                            "-",
                            status
                        )

            elif task_choice == "3":

                if len(tasks) == 0:
                    print("\nNo tasks available.")

                else:

                    for i in range(len(tasks)):
                        print(i + 1, ".", tasks[i]["name"])

                    task_number = int(
                        input("\nEnter task number to mark as completed: ")
                    )

                    if task_number >= 1 and task_number <= len(tasks):

                        tasks[task_number - 1]["completed"] = True

                        print("\nTask marked as completed!")

                    else:
                        print("\nInvalid task number.")

            elif task_choice == "4":
                break

            else:
                print("\nInvalid choice. Please try again.")


    # ================= ANALYTICS =================

    elif choice == "4":

        print("\n========== ANALYTICS ==========")

        # Expense Analytics

        total_expense = 0

        for expense in expenses:
            total_expense = total_expense + expense["amount"]

        print("\nTotal Expenses: Rs.", total_expense)

        # Attendance Analytics

        if len(attendance) > 0:

            total_percentage = 0

            for subject in attendance:
                total_percentage = (
                    total_percentage
                    + attendance[subject]["percentage"]
                )

            average_attendance = (
                total_percentage / len(attendance)
            )

            print(
                "Average Attendance:",
                round(average_attendance, 2),
                "%"
            )

        else:
            print("Average Attendance: No data")

        # Task Analytics

        total_tasks = len(tasks)
        completed_tasks = 0

        for task in tasks:

            if task["completed"]:
                completed_tasks = completed_tasks + 1

        pending_tasks = total_tasks - completed_tasks

        print("Total Tasks:", total_tasks)
        print("Completed Tasks:", completed_tasks)
        print("Pending Tasks:", pending_tasks)

        print("\n===============================")


    # ================= EXIT =================

    elif choice == "5":

        print("\nThank you for using the program!")
        break


    else:

        print("\nInvalid choice. Please try again.")