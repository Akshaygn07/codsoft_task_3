from tkinter import *
from tkinter import messagebox
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(2, 4)
nr_symbols = random.randint(0, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))



for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)



password = ""
for char in password_list:
  password += char



def get_info():
    f = open("info.txt", "a")
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website)==0 or len(username)==0 or len(password)==0:
        messagebox.showwarning(title="Warning!",message="Please dont leave any inputs empty!")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"the details you entered:\n Email:{username}\nPassword:{password}")

        if is_ok:
            f.write(f"{website}|{username}|{password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
def generate_pass_easy():
    password_entry.insert(0,str(password))

def generate_pass_hard():

    random.shuffle(password_list)


    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, str(password))

window = Tk()
window.title("Password Generator and Manager")
window.config(pady=50,padx=50)



website_label=Label(text="Website").grid(row=1,column=0)
website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)



username_label=Label(text="Username/Email").grid(row=2,column=0)
username_entry=Entry(width=35)
username_entry.grid(row=2,column=1,columnspan=2)

password_label=Label(text="Password").grid(row=3,column=0)
password_entry=Entry(width=25)
password_entry.grid(row=3,column=1)

generate_btn_easy=Button(text="Generate Easy Password",width=36,command=generate_pass_easy).grid(row=4,column=1,columnspan=2)
generate_btn_hard=Button(text="Generate Hard Password",width=36,command=generate_pass_hard).grid(row=5,column=1,columnspan=2)


add_btn=Button(text="Add",width=36,command=get_info).grid(row=6,column=1,columnspan=2)


window.mainloop()