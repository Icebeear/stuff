from tkinter import messagebox
import tkinter 
import random
import json

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, cursor="trek")

canvas = tkinter.Canvas(width=200, height=200)
image = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)
    
entry_website = tkinter.Entry(width=33)
entry_website.grid(column=1, row=1, pady=5, columnspan=2, sticky="w")
entry_website.focus()

site_label = tkinter.Label(text="Website:", font=("Arial", 10, "bold"))
site_label.grid(column=0, row=1)

entry_email = tkinter.Entry(width=50)
entry_email.grid(column=1, row=2, pady=5, columnspan=2)

mail_label = tkinter.Label(text="Email/Username:", font=("Arial", 10, "bold"))
mail_label.grid(column=0, row=2)

entry_password = tkinter.Entry(width=33)
entry_password.grid(column=1, row=3, pady=5)

pass_label = tkinter.Label(text="Password:", font=("Arial", 10, "bold"))
pass_label.grid(column=0, row=3)


def password():
    symbols = "1234567890qwertyuiopasdfghjklzxcvbnm,./;'[]_+-=)(*&^%$#@!QWERTYUIOPLKJHGFDSAMNBVCXZ"
    password = ""
    for x in range(15):
        password += random.choice(symbols)
    entry_password.delete(first=0, last="end")
    entry_password.insert(0, password)


def save_data():
    email = entry_email.get().lower()
    site = entry_website.get().lower()
    password = entry_password.get()

    dict = {
        site: {
            "email": email, 
            "password": password
        }   
    }

    if (site == "" or email == "" or password == ""):
        messagebox.showinfo(title="Error", message="Fill all the lines")

    elif messagebox.askyesno(title=site, message=f"Email: {email}\nPassword: {password}\nIs this ok?"):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(dict)
        except:
            with open("data.json", "w") as file:
                json.dump(dict, file, indent=4)
        else:
            with open("data.json", "w") as file:
                data.update(dict)
                json.dump(data, file, indent=4)
        finally:
                entry_website.delete(first=0, last="end")
                entry_password.delete(first=0, last="end")
                entry_email.delete(first=0, last="end")
                messagebox.showinfo(title="Completed", message="Password saved")


def search():
    site = entry_website.get().lower()
    try:
        with open("data.json", "r") as file:
            new_data = json.load(file)
    except:
        messagebox.showinfo(title="Error", message=f"No file found")
    else:
        try:
            messagebox.showinfo(title=site, message=f"Email: {new_data[site]['email']}\nPassword: {new_data[site]['password']}")
        except:
            messagebox.showinfo(title="Error", message=f"No details for {site}")



pass_btn = tkinter.Button(text="Generate Password", command=password, width=13)
pass_btn.grid(column=2, row=3, sticky="w")


add_btn = tkinter.Button(text="Add", command=save_data, width=42,)
add_btn.grid(column=1, row=4, columnspan=2)


search_btn = tkinter.Button(text="Search", command=search, width=13)
search_btn.grid(column=2, row=1)

window.mainloop()