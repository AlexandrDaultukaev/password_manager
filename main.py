from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint


FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]


    shuffle(password_list)

    password = ""
    for char in password_list:
      password += str(char)
    pass_input.delete(0, END)
    pass_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    web = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.askokcancel(title="Error", message="Some fields empty")
        return 0
    if web == " " or email == " " or password == " ":
        messagebox.askokcancel(title="Error", message="Incorrect input")
        return 0

    is_ok = messagebox.askokcancel(title=web, message=f"Website: {web}\nEmail: {email}\nPassword: {password}\n\nIs everything "
                                                   f"right?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{web} | {email} | {password}\n")
    web_input.delete(0, END)
    email_input.delete(0, END)
    pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.maxsize(670, 500)
window.minsize(670, 500)
window.config(padx=20, pady=20, bg="white")

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=230, bg="white", highlightthickness=0)
canvas.create_image(100, 120, image=img)
canvas.grid(row=0, column=1)

web_text = Label(text="Website:", font=(FONT_NAME, 14, "bold"), bg="white", padx=5, pady=10)
web_text.grid(row=1, column=0)

email_text = Label(text="Email/Username:", font=(FONT_NAME, 14, "bold"), bg="white", padx=5, pady=10)
email_text.grid(row=2, column=0)

pass_text = Label(text="Password:", font=(FONT_NAME, 14, "bold"), bg="white", padx=5, pady=10)
pass_text.grid(row=3, column=0)

web_input = Entry(font=(FONT_NAME, 14, "bold"), bg="white", width=35)
web_input.focus()
web_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(font=(FONT_NAME, 14, "bold"), bg="white", width=35)
email_input.grid(row=2, column=1, columnspan=2)

pass_input = Entry(font=(FONT_NAME, 14, "bold"), bg="white", width=21)
pass_input.grid(row=3, column=1)

add_button = Button(text="Add", bg="lavender", bd=0, width=36, font=(FONT_NAME, 14, "bold"), command=add_pass)
add_button.grid(row=4, column=1, columnspan=2)

gen_button = Button(text="Generate Password", bg="lavender", bd=0, width=15, font=(FONT_NAME, 12, "normal"), command=generate_pass)
gen_button.grid(row=3, column=2)

window.mainloop()
