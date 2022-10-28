from Cipher import Encryptor
from password_generator import PassGen
from timer import DateAndTime
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile
from PIL import Image,ImageTk
from tkinter import messagebox
import os

encryptor = Encryptor()

my_key = encryptor.create_key()
encryptor.write_key(my_key, 'MyKey.key')
loaded_key = encryptor.load_key('MyKey.key')

day = DateAndTime.extract_day()
hour = DateAndTime.extract_hour()
minute = DateAndTime.extract_minute()

if hour == 0:
    hour = day
elif minute == 0:
    minute = day

with open('password_file.txt','w') as pass_file:
    pass_file.write(PassGen.create_password(nr_letters=minute,nr_digits=day,nr_symbols=hour))

with open('password_file.txt','r') as pass_file:
    password_generated = pass_file.read()
    pass_file.close()

def validate_acces():
    username = user.get()
    password = acces_password.get()

    if username == "admin" and password == password_generated:

        messagebox.showinfo("","Access allowed!")

        browse_text = StringVar()
        browse_button = Button(main_window, textvariable=browse_text, command=lambda: open_file(),font="Raleway 12 bold"
                               , bg="#20bebe", fg="black")
        browse_text.set("Browse")
        browse_button.grid(column=1, row=7)
    else:
        messagebox.showinfo("","Access denied!")

main_window = Tk()
main_window.title("FileEncryption")
main_canvas = Canvas(main_window, width=600, height=300)
main_canvas.grid(columnspan=3, rowspan=20)
title = Label(main_window, text="Welcome to FileEncryption", font="Raleway 22 bold").grid(columnspan=3, column=0, row=0)


logo = Image.open('Logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tkinter.Label(image=logo)
logo_label.grid(column=1,row=1)

user_label = Label(main_window, text="User",font="Raleway 12 bold", fg="black").grid(column=1, row=2)
user = StringVar()
user_entry = Entry(main_window, textvariable=user,font="Raleway 12 bold", bg="#20bebe").grid(column=1, row=3)

password_label = Label(main_window, text="Password", font="Raleway 12 bold", fg="black").grid(column=1, row=4)
acces_password = StringVar()
password_entry = Entry(main_window, textvariable=acces_password, show='*',font="Raleway 12 bold", bg="#20bebe").grid(column=1,row=5,)

validate_button = Button(main_window, text="Validate", command=validate_acces,font="Raleway 12 bold", bg="#20bebe", fg="black")
validate_button.grid(column=1,row=6)

browse_text = StringVar()
browse_button = Button(main_window, textvariable=browse_text, font="Raleway 12 bold"
                       , bg="grey", fg="black")
browse_text.set("Browse")
browse_button.grid(column=1, row=7)


def open_file():

    browse_text.set("loading")
    file = askopenfile(parent=main_window, mode='rb', title="Choose a file")
    first_index = str(file).index('=')
    last_index = str(file).index('>')
    file_path = str(file)[first_index+1:last_index-1]
    file_name = os.path.basename(file_path)
    dot_index = file_name.index('.')
    file_extention = file_name[dot_index:]
    encr_file_name = "encrypted_file"+file_extention
    decr_file_name = "decrypted_file"+file_extention

    if file:
        def encr():
            encryptor.file_encryption(loaded_key, file_name, encr_file_name)
            messagebox.showinfo("", "The file was successfully encrypted!")

        def decr():
            encryptor.file_decryption(loaded_key, encr_file_name, decr_file_name)
            messagebox.showinfo("", "The file was successfully decrypted!")

        decision_window = Tk()
        decision_window.title("Choosing an operation")
        decision_canvas = Canvas(decision_window, width=400, height=250)
        decision_canvas.grid(columnspan=3, rowspan=3)

        decision_title = Label(decision_window, text="Choose an option",font="Raleway 22 bold",fg="red").grid(columnspan=3, column=0, row=0)

        encr_button = Button(decision_window,command= encr, text="Encryption", font="Raleway 12 bold", bg="#20bebe", height=2, width=15)
        encr_button.grid(column=0,row=1)

        decr_button = Button(decision_window,command=decr, text="Decryption", font="Raleway 12 bold", bg="#20bebe", fg="black",
                             height=2, width=15)
        decr_button.grid(column=2,row=1)

        decision_window.mainloop()

main_window.mainloop()