# importing libraries
import datetime
from datetime import *


# define function to register user
def reg_user(my_menu):
    # creating if statement for the menu
    if my_menu == "r":

        new_user = input("Please enter a new username: ")

        # checking if the username already exists in the usernames_list
        # if listed, an error message is displayed and the user is asked to enter a new username
        while new_user in usernames_list:
            print("The username you entered is already listed.")
            new_user = input("Please enter a new username: ")

        # if the new username is not listed, it is added to usernames_list
        if new_user not in usernames_list:
            usernames_list.append(new_user)

        # the list is then updated in the dictionary user_details
        user_details_dict["Usernames"] = usernames_list

        # the user is prompted to enter a password
        new_password = input("Please enter a new password: ")

        # the user is asked to confirm the new password
        pass_confirm = input("Please confirm your new password: ")

        # if the new and confirmed password values do not match, an error message is displayed
        # the user is prompted to enter the new password and confirm it until they match
        while new_password != pass_confirm:
            print("Your confirmed password does not match the original password.")
            new_password = input("Please enter your new password: ")
            pass_confirm = input("Please confirm your new password: ")

        # if the new and confirmed password values match, a successful message is displayed
        # the new password is added to the passwords_list and dictionary updated
        if new_password == pass_confirm:
            print("Your password is valid.")
            passwords_list.append(new_password)
            user_details_dict["Passwords"] = passwords_list

            # user.txt file opened to write to
            with open('user.txt', 'r+') as f:

                # print username and passwords on separate lines
                for i in range(len(usernames_list)):
                    f.write(user_details_dict["Usernames"][i] + ", " + user_details_dict["Passwords"][i] + '\n')

            # message returned at the end of function
            return "Your new username and password have been successfully added."


# define function to add task
def add_task(my_menu):
    if my_menu == "a":
        import datetime
        from datetime import date
        # getting user input on the username of the person the task is assigned to
        # getting user input on the title of the task being added
        # getting user input on the description of the added task
        name = input("Please enter the username of the person you wish to assign the task to: ")
        title = input("Please enter the title of the task: ")
        descrip = input("Please enter a description of the task: ")

        # using the imported datetime module "today()" function to calculate the current date
        # changing the date object to a string in the correct date format
        current_date = datetime.date.today()
        assigned_date = current_date.strftime("%d %b %Y")

        # getting input on the due date of the task being added
        date_format = input("Please enter the due date of the task (e.g. dd-mm-yyyy): ")
        date_list = date_format.split("-")
        numbers_date = [int(x) for x in date_list]
        due_date = date(numbers_date[2], numbers_date[1], numbers_date[0]).strftime("%d %b %Y")

        # task_completed is automatically set to "No" when adding a new task.
        task_completed = "No"

        # casting all the user input info into a list, to add to the tasks_dict
        task_list = [name, title, descrip, assigned_date, due_date, task_completed]
        tasks_dict[f"Task {count} details:"] = task_list

        # opening the tasks.txt file to enter the new task information
        with open("tasks.txt", "r+") as f2:

            # printing the list values for each key in tasks_dict to a new line
            for key in tasks_dict:
                line_string = str(tasks_dict[key])
                bad_chars = ["[", "]", "\'", ]

                # taking out characters pertaining to previous list/dictionary format
                for i in bad_chars:
                    line_string = line_string.replace(i, "")

                # writing the correct format of each string line to the file
                f2.write(line_string + "\n")

        # message returned at the end of the function
        return "Your new task has been added successfully."


# define function to view all tasks
def view_all(my_menu):
    # user to view all tasks listed in tasks.txt
    # these tasks are already stored in the dictionary 'tasks_dict', the dictionary will be used to view all the tasks
    if my_menu == "va":
        task_count = 0

        for key in tasks_dict:
            task_count += 1
            print(f"""____________________________________________
    Task {str(task_count)}:     {str(tasks_dict[key][1])}
    Assigned to:            {str(tasks_dict[key][0])}
    Date assigned:          {str(tasks_dict[key][3])}
    Due Date:               {str(tasks_dict[key][4])}
    Task Complete?          {str(tasks_dict[key][5])}
    Task Description:
    {str(tasks_dict[key][2])}
    ________________________________________________""")
        return "End of Tasks."


# define function to view my tasks
def view_mine(my_menu, username):
    # user to view only tasks assigned to him in tasks.txt
    if my_menu == "vm":
        task_count = 0

        for key in tasks_dict:
            task_count += 1
            if username == (tasks_dict[key][0]):
                print(f"""____________________________________________
    Task {str(task_count)}:      \t{str(tasks_dict[key][1])}
    Assigned to:        {str(tasks_dict[key][0])}
    Date assigned:      {str(tasks_dict[key][3])}
    Due Date:           {str(tasks_dict[key][4])}
    Task Complete?      {str(tasks_dict[key][5])}
    Task Description:
     {str(tasks_dict[key][2])}
    ________________________________________________""")

    # the user can choose to either edit a task by number or return to the main menu
    task_selection = input(
        "Please select a a task by number to edit (e.g. 1, 2,3) or type -1 to return to the main menu. ")

    # if they select '-1', they return to the outer while loop main menu
    if task_selection == "-1":
        return menu

    # if they enter a task number, they can choose to mark as complete or edit
    else:
        option = input("Would you like to mark the task as complete or edit the task? (e.g. mark OR edit) ")
        if option == "mark":

            # if they choose to mark, the item linked to that task for completion is changed to 'Yes' in tasks_dict
            tasks_dict[f"Task {task_selection} details:"][5] = "Yes"
            return "Your task has been successfully marked as complete."

        # if they choose to edit, the task must be incomplete, i.e. appropriate item in dictionary list equal to 'No'
        elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "No"):

            # they are given the option to edit username or due date
            edit_choice = input("Would you like to edit the task username or due date? (Type 'U' or 'D') ").lower()

            # if they choose to edit the username, they are prompted to enter a new username for the task
            if edit_choice == "u":
                name_edit = input("Please enter a new username for the task: ")
                # the new name is assigned in the dictionary
                tasks_dict[f"Task {task_selection} details:"][0] = name_edit
                return "The task username has been updated successfully."

            # if they choose to edit the due date, they are prompted to enter a new date
            elif edit_choice == "d":

                due_date_change = input("Please enter a new due date (e.g. 12 May 2020) ")

                # new date is updated in the tasks_dict
                tasks_dict[f"Task {task_selection} details:"][4] = due_date_change
                return "The due date has been updated successfully."

            elif option == "edit" and (tasks_dict[f"Task {task_selection} details:"][5] == "Yes"):
                return "You can only edit tasks that are not already complete."
                return "Choose 'vm' from menu below to select another task to edit."


# define function to generate reports
def generate_reports():
    # setting blank strings to store info in to be written to the generated text files
    task_overview = ""
    user_overview = ""

    # total number of tasks is equal to the key count of tasks_dict
    tasks_total = len(tasks_dict)

    # adding a string with the total tasks number to the tas_overview string
    task_overview = task_overview + f"The total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."

    # setting variables for integers concerning complete tasks and incomplete tasks respectively
    x = 0
    y = 0

    for key in tasks_dict:
        # checking for which tasks are complete by finding the 'Yes' string in each key of tasks_dict
        if tasks_dict[key][5] == "Yes":

            # if the task is complete, i.e. 'Yes' string item is present, variable x is increased by 1
            x += 1
        # checking for which tasks are complete by finding the 'No' string in each key of tasks_dict
        elif tasks_dict[key][5] == "No":
            # if the task is complete, i.e. 'No' string item is present, variable y is increased by 1
            y += 1

    # all numbers calculated above are now built into sentences in the task_overview string
    task_overview = task_overview + f"\nThe total number of completed tasks is {str(x)}."
    task_overview = task_overview + f"\nThe total number of incomplete tasks is {str(y)}."

    # generating a 'task_overview' file
    # task_overview string is then written to the file in an easy-to-read format
    with open("task_overview.txt", "w") as f3:

        f3.write(task_overview)

    # setting variables to store information regarding total users, complete and incomplete tasks for the user
    a = 0
    b = 0
    c = 0

    for key in tasks_dict:
        # counting the number of tasks assigned to the user by identifying the first list item
        if tasks_dict[key][0] == username:
            # integer 'a' is increased by 1 if the task is for the user
            a += 1

        # checking if the task for the user is complete
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "Yes":
            # integer 'b' is increased by 1 if the task is complete
            b += 1

        # checking if the task for the user is incomplete
        elif tasks_dict[key][0] == username and tasks_dict[key][5] == "No":
            # integer 'c' is increased by 1 if the task is incomplete
            c += 1

    # writing all the info calculated above into sentence strings which are built into the user_overview string variable
    user_overview = user_overview + f"The total number of users registered with task_manager.py is {str(len(user_details_dict))}."
    user_overview = user_overview + f"\nThe total number of tasks generated and tracked by task_manager.py is {str(len(tasks_dict))}."
    user_overview = user_overview + f"\nThe total number of tasks assigned to {username} is {str(a)}."
    user_overview = user_overview + f"\nThe total number completed tasks assigned to {username} is {str(b)}."
    user_overview = user_overview + f"\nThe total number of incomplete tasks assigned to {username} is {str(c)}."

    # generating a 'user_overview' file
    # user_overview string is then written to the file in an easy-to-read format
    with open("user_overview.txt", "w") as f4:

        f4.write(user_overview)

    # the user then views a message stating that their reports have been successfully generated
    # they do not have the option to view the reports
    # the admin user can select to display statistics from their main menu
    return "Your reports have been generated successfully."


# ====Login Section====
# create a user details dictionary
user_details_dict = {}

# the user details dictionary will consist of 2 lists: "usernames_list" and "passwords_list"
usernames_list = []
passwords_list = []

# create a tasks details dictionary
tasks_dict = {}

# open the tasks.txt file to read and write information from it
# add the info in the user.txt file into the list
with open("user.txt", "r+") as f:
    for line in f:
        newline = line.rstrip("\n")
        split_line = newline.split(", ")
        usernames_list.append(split_line[0])
        passwords_list.append(split_line[1])
        user_details_dict["Usernames"] = usernames_list
        user_details_dict["Passwords"] = passwords_list

# keep track of the number of lines in the tasks.txt file
count = 1

# open the tasks.txt file to read and write information to it
with open("tasks.txt", "r+") as f2:
    for line in f2:
        newline = line.rstrip("\n")
        split_line = newline.split(", ")
        tasks_dict[f"Task {count} details:"] = split_line
        count += 1

# prompt the user to login
username = input("Please enter your username: ")
password = input("Please enter your password: ")

# use a while loop which will stop when login details are correct
# if login details are incorrect the error message will appear
while (username not in usernames_list) or (password not in passwords_list):
    if (username not in usernames_list) and (password in passwords_list):
        print("Your username is not listed.")

        username = input("Please re-enter your username: ")
        password = input("Please re-enter your password: ")

    # if password is incorrect and username is correct, this message will appear
    elif (password not in passwords_list) and (username in usernames_list):
        print("Your password is incorrect.")
        username = input("Please re-enter your username: ")
        password = input("Please re-enter your password: ")

    # if both the username and password are incorrect, this message will appear
    elif (username not in usernames_list) and (password not in passwords_list):
        print("Your username and password are incorrect.")
        username = input("Please re-enter your username: ")
        password = input("Please re-enter your password: ")

# If both username and password are correct, this message will appear
if (username in usernames_list) and (password in passwords_list):
    print("You are now logged in.")

while 1:
    # the admin user views a specific menu with extra options
    if username == "admin":

        menu = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics
e - exit
""").lower()

    # all other users can only view the basic menu
    else:
        menu = input("""\nPlease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit
""").lower()

    if menu == "r":
        print(reg_user(menu))

    elif menu == "a":
        print(add_task(menu))

    elif menu == "va":
        print(view_all(menu))

    elif menu == "vm":
        print(view_mine(menu, username))

    elif menu == "gr":
        print(generate_reports())

    elif menu == "ds":
        print(generate_reports())
        print("""\n____________________________________________________
The task overview report is as follows:
____________________________________________________\n""")

        # opening the task_overview file to get info from it
        with open("task_overview.txt", "r+") as f3:
            for line in f3:
                print(line)

        print("""\n_____________________________________________________
The user overview report is as follows:
_____________________________________________________\n""")

        with open("user_overview.txt", "r+") as f4:
            for line in f4:
                print(line)

        print("""\n______________________________________________________
End of Statistics Reports
______________________________________________________\n""")

    # if the user selects 'e' they can log out of the programme
    elif menu == "e":
        print("Goodbye!!!")

    else:
        print("The option you chose is not recognised. Please try again.")

        break
