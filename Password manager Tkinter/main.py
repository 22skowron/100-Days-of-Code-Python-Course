from tkinter import Tk, Label, END, Entry, Button, PhotoImage, Canvas, mainloop
from tkinter import messagebox
import random
import json

            ###################### CONSTANCE
ACCOUNTS = 0

    ########################################################################## # # #


    ########################################################################## # # #


            ############################################ EXTRACT CURRENT ACCOUNT NUMBER
            ############################################ or
            ############################################ CREATE FILE FOR ACCOUNT COUNT STORAGE
try:
    with open("accounts_count.txt", "r") as file:
        content = file.read()
        print("--> File read in try section.")
        print(f"--> Current accounts number: {content}")
        ACCOUNTS = int(content)
except:
    with open("accounts_count.txt", "w") as file:
        file.write("0")
    print("--> File created in except section.")
    print(f"--> Current accounts number: 0")

            ############################################ PASSWORD GENERATOR
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []

            # OPTION 1
    # for char in range(nr_letters):
    #     password_list += random.choice(letters)
            # OPTION 2
    password_list = [random.choice(letters) for x in range(nr_letters)]

            # OPTION 1
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
            # OPTION 2
    password_list += [random.choice(symbols) for x in range(nr_symbols)]

            # OPTION 1
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
            # OPTION 2
    password_list += [random.choice(numbers) for x in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    print("Password successfully generated.")

# INSERTING GENERATED PASSWORD
    current_password = insert_password.get()
    if current_password != "":
        wants_to_replace = messagebox.askyesno(title="Warning", message="The password which you entered will "
                                                                        "be replaced. Are you sure to continue?")
        if wants_to_replace:
            insert_password.delete(0, END)
            insert_password.insert(0, password)
            print("Old password deleted, new password inserted.")
        else:
            print("Cancelling, old password left intact.")
    else:
        insert_password.insert(0, password)
        print("New password inserted.")


            ############################################ FUNCTIONS
def get_details():
    website = insert_website.get()
    email = insert_email.get()
    password = insert_password.get()
    details_list = []
    details_list.append(website)
    details_list.append(email)
    details_list.append(password)
    print("")
    for x in details_list:
        if x == "":
            print(f"{details_list.index(x) + 1} field is empty.")
        elif x != "":
            print(f"Some details provided in {details_list.index(x) + 1} field.")
def add_account_details():
# GETTING INPUT
    website = insert_website.get()
    email = insert_email.get()
    password = insert_password.get()
    new_json_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showinfo(title="Error", message="Some elements are missing, please enter all required data.")

    else:
        user_is_sure = messagebox.askyesno(title="Confirmation", message="Are you sure u want to create "
                                                          "an account with provided details?")
        if user_is_sure:
            insert_website.delete(0, END)
            insert_email.delete(0, END)
            insert_password.delete(0, END)

            global ACCOUNTS
            ACCOUNTS += 1
            print("\nAccounts number increased.")

        # SAVING INTO A TEXT FILE
            with open("user_accounts_data.txt", "a") as file:
                file.write(f"{ACCOUNTS}. {website} | {email} | {password}\n")
            print("New user details saved into a file.")

            with open("accounts_count.txt", "w") as file:
                file.write(str(ACCOUNTS))
            print("New accounts' number saved into a file.")

        # SAVING INTO A JSON FILE
            try:
                with open("user_accounts_data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_json_data)

            except FileNotFoundError:
                with open("user_accounts_data.json", "w") as file:
                    json.dump(new_json_data, file, indent=4)

            else:
                with open("user_accounts_data.json", "w") as file:
                    json.dump(data, file, indent=4)


def change_password_display():
    global asterix
    if asterix:
        insert_password.config(show="")
        asterix = False
    else:
        insert_password.config(show="*")
        asterix = True
    print("Password display changed.")


def create_dummy_user():
    global ACCOUNTS
    insert_website.insert(0, f"Website{ACCOUNTS+1}")
    insert_email.insert(0, f"User{ACCOUNTS+1}")
    generate_password()
    add_account_details()


def search_details():
    website = insert_website.get()
    try:
        with open("user_accounts_data.json", "r") as file:
            data = json.load(file)
    # PRINTING DETAILS
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")

    except KeyError:
        messagebox.showinfo(title="Error", message="No account on this website yet.")

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file provided created yet. Add some accounts"
                                                   "before searching.")

            ############################################ OBJECTS

window = Tk()
window.config(pady=150, padx=200)
window.title("Password manager")
canvas = Canvas(width=240, height=240, bg=None, highlightthickness=0)
# canvas = Canvas(width=240, height=240, bg="red", highlightthickness=0)
canvas.grid(row=1, column=2, pady=3)

        ###################### # # # IMAGE # # #
padlock_image = PhotoImage(file="supreme_padlock_nobg2.png")
canvas.create_image(130, 110, image=padlock_image)

        ###################### # # # LABEL "WEBSITE" # # #
lbl_website = Label(text="Website:", font=("Arial", 12, "bold"))
lbl_website.grid(column=1, row=2)

        ###################### # # # LABEL "EMAIL/USERNAME" # # #
lbl_email = Label(text="Email/Username:", font=("Arial", 12, "bold"))
lbl_email.grid(column=1, row=3)

        ###################### # # # LABEL "PASSWORD" # # #
lbl_password = Label(text="Password:", font=("Arial", 12, "bold"))
lbl_password.grid(column=1, row=4)

        ###################### # # # ENTRY "WEBSITE" # # #
insert_website = Entry(width=40)

insert_website.grid(column=2, row=2, padx=00, pady=3)

        ###################### # # # ENTRY "EMAIL" # # #
insert_email = Entry(width=60)
insert_email.grid(row=3, column=2, columnspan=2, pady=3)

        ###################### # # # ENTRY "password" # # #
insert_password = Entry(width=40)
insert_password.grid(row=4, column=2, pady=3)
asterix = False

        ###################### # # # BUTTON "GENERATE" # # #
btn_generate = Button(text="Generate password", font=("Arial", 8, "normal"), bg="white", width=18,
                      command=generate_password)
btn_generate.grid(row=4, column=3)

        ###################### # # # BUTTON "SEARCH" # # #
btn_search = Button(text="Search", font=("Arial", 8, "normal"), bg="white", width=18,
                      command=search_details)
btn_search.grid(row=2, column=3)

        ###################### # # # BUTTON "ADD" # # #
btn_Add = Button(text="Add", font=("Arial", 8, "normal"), width=60, bg="white", command=add_account_details)
btn_Add.grid(row=5, column=2, columnspan=2, pady=3)

########################################################################## FOR LEARNING PURPOSE ONLY
btn_details = Button(text="Check details", font=("Arial", 8, "italic"), width=19, bg="white", command=get_details)
btn_details.grid(row=6, column=4, padx=30, pady=3)

########################################################################## PASSWORD DISPLAY SWITCH
btn_visibility = Button(text="Hide/show password", font=("Arial", 8, "italic"), width=19, bg="white",
                        command=change_password_display)
btn_visibility.grid(row=7, column=4, padx=30, pady=3)

########################################################################## FOR CREATING DUMMY ENTRY
btn_dummy_maker = Button(text="Create test account", font=("Arial", 8, "italic"), width=19, bg="white",
                        command=create_dummy_user)
btn_dummy_maker.grid(row=8, column=4, padx=30, pady=3)



mainloop()












