#=====importing libraries===========
import datetime

#====Login Section====
# define functions
def reg_user():
    """
    add a new user to 'user.txt
    if the user is already registered, request to change the username
    '"""
    # request username and password from the user. Password confirmation is also requested
    username_new = input("Register as a new user. Please enter the username:")
    # check if the user is already registered
    # create existing user list
    user_list = []
    with open('user.txt', 'r') as f:
        user_data = f.readlines()
        for line in user_data:
            user, pw = line.split(', ')
            user_list.append(user)

    if username_new in user_list:
        print("The user name has already existed")
        username_new = input("Please add the user with a different username.\nusername:")

    password_new = input("Please enter the password:")
    pw_conf = input("Password confirmation. Please enter the password again:")
    # check if password and confirmation password are the same
    if password_new == pw_conf:
        with open('user.txt', 'a') as f:
            f.write(f"\n{username_new}, {password_new}")
        print("Successfully registered\n")
    else:
        print("You entered different passwords.\n")

def add_task():
    """ ask user to enter the information to add to 'tasks.txt'"""
    username_task = input("Add a task. Please enter the username:")
    task = input("Please enter a title of a task:")
    task_descript = input("Please enter a description of the task:")
    due_date_str = input("Please enter the due date in DD/MM/YYYY")
    due_date = datetime.datetime.strptime(due_date_str, "%d/%m/%Y").date()
    due_date_formatted = due_date.strftime("%d %b %Y")
    today = datetime.date.today().strftime("%d %b %Y")
    with open('tasks.txt', 'a') as f:
        f.write(f"\n{username_task}, {task}, {task_descript}, {today}, {due_date_formatted}, No")
    print("Successfully registered\n")

def view_all():
    """print out all the tasks"""
    with open('tasks.txt', 'r') as f:
        tasks_lines = f.readlines()
        for num, line in enumerate(tasks_lines):
            split_tasks_lines = line.split(", ")
            split_tasks_lines[-1] = split_tasks_lines[-1].strip("\n")
            output = f"[{num + 1}]---------------------------\n"
            output += f"Assigned to:\t\t{split_tasks_lines[0]}\n"
            output += f"Task:\t\t\t{split_tasks_lines[1]}\n"
            output += f"Description:\t\t{split_tasks_lines[2]}\n"
            output += f"Assigned Date:\t\t{split_tasks_lines[3]}\n"
            output += f"Due Date:\t\t\t{split_tasks_lines[4]}\n"
            output += f"Is completed:\t\t{split_tasks_lines[5]}\n"
            output += "-------------------------------\n"
            print(output)

def view_mine():
    """
    print out the tasks of the user logged in
    the user can select the task and mark it as completed or edit the username or the due date
    """
    with open('tasks.txt', 'r') as f:
        tasks_lines = f.readlines()
        task_count = 1
        print("\nYour Tasks:")
        for line in tasks_lines:
            split_tasks_lines = line.split(", ")
            split_tasks_lines[-1] = split_tasks_lines[-1].strip("\n")
            if split_tasks_lines[0] == username:
                output = f"Task{task_count}:\n------------------------------\n"
                output += f"Assigned to:\t\t{split_tasks_lines[0]}\n"
                output += f"Task:\t\t\t\t{split_tasks_lines[1]}\n"
                output += f"Description:\t\t{split_tasks_lines[2]}\n"
                output += f"Assigned Date:\t\t{split_tasks_lines[3]}\n"
                output += f"Due Date:\t\t\t{split_tasks_lines[4]}\n"
                output += f"Is completed:\t\t{split_tasks_lines[5]}\n"
                output += "-------------------------------\n"
                print(output)
                task_count += 1

    # a user select the task or return to the main menu
    task_num = int(input("\nPlease enter the task number you want to select (please enter whole number)\n"
                         "If you want to return to the main menu, please enter -1\n"
                         "number:"))
    if task_num == -1:
        pass

    # a user select an action to take
    elif task_num <= task_count:
        action = input("\nPlease select action that you want to take.\n"
                       "a) mark the task as complete\n"
                       "b) edit the task\n"
                       "a or b :")

        # mark the selected task as completed
        if action == "a":
            edited_lines = ""
            with open('tasks.txt', 'w+') as f:
                counter = 1
                for line in tasks_lines:
                    split_tasks_lines = line.split(", ")
                    # mark the selected task as complete
                    if split_tasks_lines[0] == username:
                        if counter == task_num:
                            change = line.replace("No", "Yes")
                            edited_lines += change
                        else:
                            edited_lines += line
                        counter += 1
                    else:
                        edited_lines += line
                # overwrite the file
                f.write(edited_lines)
                print("\nSuccessfully edited\n")

        # a user can edit the username and the due date if the task has not been completed
        elif action == "b":
            edited_lines = ""
            with open('tasks.txt', 'w+') as f:
                counter = 1
                for line in tasks_lines:
                    split_tasks_lines = line.split(", ")

                    if split_tasks_lines[0] == username:
                        if counter == task_num:
                            if split_tasks_lines[-1] == "No\n":
                                username_ed = input("\nYou can edit the username to whom the task is assigned and the due date\n"
                                                    "If you don't want to edit, please do not enter anything\n"
                                                    "username:")
                                date_ed_str = input("due date (DD/MM/YYYY):")
                                date_ed = datetime.datetime.strptime(date_ed_str, "%d/%m/%Y").date()
                                date_ed_formatted = date_ed.strftime("%d %b %Y")
                                if username_ed != "":
                                    split_tasks_lines[0] = username_ed
                                if date_ed_str != "":
                                    split_tasks_lines[4] = date_ed_formatted
                                line_ed = ", ".join(split_tasks_lines)
                                edited_lines += line_ed

                            else:
                                print("\nThe task has already been completed.\n")
                                edited_lines += line
                        else:
                            edited_lines += line
                        counter += 1
                    else:
                        edited_lines += line

                # overwrite the file
                f.write(edited_lines)
                print("\nSuccessfully edited\n")

def gen_report():
    """
    generate the two report files: task_overview.txt, user_overview.txt
    """
    with open("task_overview.txt", 'w') as f1, open("user_overview.txt", 'w') as f2, open("tasks.txt", 'r') as f3:
        tasks_lines = f3.readlines()
        num_comp_task = 0
        num_uncomp_task = 0
        num_overdue = 0
        task_list =[]
        users = []
        today = datetime.date.today().strftime("%d %b %Y")
        for line in tasks_lines:
            split_tasks_lines = line.split(", ")
            split_tasks_lines[-1] = split_tasks_lines[-1].strip("\n")
            task_list.append(split_tasks_lines)
            users.append(split_tasks_lines[0])

            # check if the task is completed
            if split_tasks_lines[-1] == "Yes":
                num_uncomp_task +=1
            else:
                num_uncomp_task += 1
                # check if the task is overdue
                if split_tasks_lines[4] < today:
                    num_overdue += 1

        num_tasks = len(task_list)
        p_uncomp = num_uncomp_task / num_tasks * 100
        p_overdue = num_overdue / num_tasks * 100

        # create output for task_overview.txt
        output = "\n============Task Overview============\n"
        output += f"Number of tasks: {num_tasks}\n"
        output += f"Number of completed tasks: {num_comp_task}\n"
        output += f"Number of uncompleted tasks: {num_uncomp_task}\n"
        output += f"Number of uncompleted and overdue tasks: {num_overdue}\n"
        output += f"The percentage of uncompleted tasks: {round(p_uncomp, 2)}\n"
        output += f"The percentage of overdue tasks: {round(p_overdue, 2)}\n"

        f1.write(output)

        # create output for user_overview.txt

        output2 = "\n============User Overview===========\n"
        output2 += f"Total number of users: {len(set(users))}\n"
        output2 += f"Total number of tasks: {num_tasks}\n"

        # get each user's tasks information and create output
        for user in set(users):
            num_comp = 0
            num_uncomp = 0
            num_overdue = 0
            # percentage of the number of tasks assigned to the user
            p_user_task = users.count(user) / num_tasks * 100
            for task in task_list:
                if task[0] == user:
                    if task[-1] == "Yes":
                        num_comp += 1
                    else:
                        num_uncomp += 1
                        if task[4] < today:
                            num_overdue += 1

            p_user_comp_task = num_comp / num_tasks * 100
            p_user_uncomp_task = num_uncomp / num_tasks * 100
            p_user_overdue = num_overdue / num_tasks * 100
            output2 += f"\n-------------The information of the tasks assigned to {user}-------------\n"
            output2 += f"The total number of tasks: {users.count(user)}\n"
            output2 += f"The percentage of the total tasks assigned: {round(p_user_task, 2)}\n"
            output2 += f"The percentage of completed tasks: {round(p_user_comp_task, 2)}\n"
            output2 += f"The percentage of uncompleted tasks: {round(p_user_uncomp_task, 2)}\n"
            output2 += f"The percentage of uncompleted and overdue tasks: {round(p_user_overdue, 2)}\n"

        f2.write(output2)

        print("Reports has been created")

def display_stats():
    with open("task_overview.txt") as f1, open("user_overview.txt") as f2:
        task_overview = f1.read()
        user_overview = f2.read()
        print(task_overview)
        print(user_overview)

# read usernames and password from 'user.txt'
password_dict = {}
with open('user.txt', 'r') as f:
    user_data = f.readlines()
    for line in user_data:
        k, v = line.split(', ')
        password_dict[k] = v.strip("\n")

# validate the username and password for login
username = ""
while True:
    username = input("Please enter your username:")
    if username not in password_dict.keys():
        print("Username is not valid. Please enter the correct username.")
    else:
        password = input("Please enter your password:")
        if password == password_dict[username]:
            print(f"\nWelcome, {username}! You are successfully logged in.")
            break
        else:
            print("\nPlease enter the correct password.")

while True:
    #presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = ""
    # only the user 'admin' is allowed to register new users and view statistics
    if username == "admin":
        menu = input("\nSelect one of the following Options below:\n"  
                    "r - Registering a user\n"
                    "a - Adding a task\n"
                    "va - View all tasks\n"
                    "vm - view my task\n"
                    "gr - generate reports\n"
                    "ds - display statistics\n"
                    "e - Exit\n"
                    ": ").lower()
    else:
        menu = input("\nSelect one of the following Options below:\n"  
                    "a - Adding a task\n"
                    "va - View all tasks\n"
                    "vm - view my task\n"
                    "e - Exit\n"
                    ": ").lower()

    if (menu == 'r') and (username == "admin"):
        # add a new user to 'user.txt'
        reg_user()

    elif menu == 'a':
        # ask user to enter the information to add to 'tasks.txt'
        add_task()

    elif menu == 'va':
        # print out all the tasks
        view_all()

    elif menu == 'vm':
        # print out the tasks of the user logged in
        view_mine()

    elif (menu == "gr") and (username == 'admin'):
        # generate the report
        gen_report()

    elif (menu == 'ds') and (username == 'admin'):
        # print out the reports
        try:
            with open("task_overview.txt") as f1, open("user_overview.txt") as f2:
                task_overview = f1.read()
                user_overview = f2.read()
                print(task_overview)
                print(user_overview)

        except IOError as e:
            gen_report()
            display_stats()

    elif menu == 'e':
        # exit from the for loop
        print('Goodbye!!!')
        break

    else:
        print("You have made a wrong choice, Please Try again\n")