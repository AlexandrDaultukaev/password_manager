from tkinter import *

FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


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
email_input.insert(0, "shyra31102000@mail.ru")
email_input.grid(row=2, column=1, columnspan=2)

pass_input = Entry(font=(FONT_NAME, 14, "bold"), bg="white", width=21)
pass_input.grid(row=3, column=1)

add_button = Button(text="Add", bg="lavender", bd=0, width=36, font=(FONT_NAME, 14, "bold"))
add_button.grid(row=4, column=1, columnspan=2)

gen_button = Button(text="Generate Password", bg="lavender", bd=0, width=15, font=(FONT_NAME, 12, "normal"))
gen_button.grid(row=3, column=2)


window.mainloop()