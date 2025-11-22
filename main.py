from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    web=website_name.get()
    with open("data_file.json", mode="r") as file:
        data=json.load(file)
        if web in data:
            email=data[web]["Email"]
            password=data[web]["Password"]
            messagebox.showinfo(title="Website Credentials",message=f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showerror(message="This website details not found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)
    password_ = "".join(password_list)
    password_space.insert(0, password_)
    is__ok = messagebox.askokcancel(message=f"Is this password Ok {password_} ?")
    if not is__ok:
        password_space.delete(0, END)
        generate()


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entered = website_name.get()
    mail_entered = email_space.get()
    password_entered = password_space.get()
    new_data = {
        website_entered: {
            "Email": mail_entered,
            "Password": password_entered
        }
    }

    if website_entered == "":
        messagebox.showinfo(title="Error", message="please enter the website")
    elif password_entered == "":
        messagebox.showerror(title="error", message="Password can not be empty")

    else:
        is_ok = messagebox.askokcancel(title="Confirm Details",
                                       message=f"The details entered are\nWebsite  : {website_entered}\nEmail : {mail_entered}\nPassword : {password_entered}\nDo you want to save?")
        if is_ok:
            try:
                with open("data_file.json", mode='r') as data_file:
                    data=json.load(data_file)
            except FileNotFoundError:
                with open("data_file.json", mode='w') as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                data.update(new_data)
                with open("data_file.json", mode='w') as data_file:
                    json.dump(data,data_file,indent=4)
            finally:
                website_name.delete(0, END)
                password_space.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
back_image = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=back_image)
canvas.grid(row=0, column=1)

website = Label(text="Website : ", font=(24))
website.grid(row=1, column=0)

website_name = Entry(width=34)
website_name.focus()
website_name.grid(row=1, column=1)

search=Button(text="Search", width=14, command=search_password)
search.grid(row=1, column=2)

email = Label(text="Email : ", font=(24))
email.grid(row=2, column=0)

email_space = Entry(width=52)
email_space.insert(0, "subhash@gamil.com")
email_space.grid(row=2, column=1, columnspan=2)

password = Label(text="Password : ", font=(24))
password.grid(row=3, column=0)

password_space = Entry(width=34)
password_space.grid(row=3, column=1)

generate_password = Button(text="Generate Password", width=14, command=generate)
generate_password.grid(row=3, column=2)

add = Button(text="Add Password", width=44, command=save)
add.grid(row=4, column=1, columnspan=3)

window.mainloop()
