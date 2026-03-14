from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import tkinter.font as tkFont

root = Tk()
root.title("Marvel Login")
root.iconbitmap("my-icon.ico")

# -------- FULL SCREEN --------
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
root.geometry(f"{screen_w}x{screen_h}")

# -------- BACKGROUND IMAGE --------
bg_img = Image.open("marvel-back.jpg")
bg_img = bg_img.resize((screen_w, screen_h))
bg_img = ImageTk.PhotoImage(bg_img)

bg_label = Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# -------- CUSTOM FONTS --------
title_font = tkFont.Font(family="Bebas Neue", size=40, weight="bold")
label_font = tkFont.Font(family="Arial", size=14)
button_font = tkFont.Font(family="Bebas Neue", size=16)

# -------- LOGIN FUNCTION --------
def login():
    email = email_entry.get()
    password = password_entry.get()

    if email == "admin@gmail.com" and password == "1234":
        messagebox.showinfo("Success", "Login Successful")
        open_student_form()
    else:
        messagebox.showerror("Error", "Invalid Email or Password")

# -------- STUDENT FORM --------
def open_student_form():

    student = Toplevel(root)
    student.title("Student Registration")
    student.geometry("900x600")

    name_var = StringVar()
    roll_var = StringVar()
    email_var = StringVar()
    dept_var = StringVar()
    gender_var = StringVar()

    Label(student,
          text="Student Registration",
          font=("Bebas Neue",30,"bold"),
          fg="red").pack(pady=20)

    form = Frame(student)
    form.pack()

    Label(form, text="Name", font=label_font).grid(row=0,column=0,padx=10,pady=5)
    Entry(form, textvariable=name_var).grid(row=0,column=1)

    Label(form, text="Roll", font=label_font).grid(row=1,column=0,padx=10,pady=5)
    Entry(form, textvariable=roll_var).grid(row=1,column=1)

    Label(form, text="Email", font=label_font).grid(row=2,column=0,padx=10,pady=5)
    Entry(form, textvariable=email_var).grid(row=2,column=1)

    Label(form, text="Department", font=label_font).grid(row=3,column=0,padx=10,pady=5)

    dept = ttk.Combobox(form,
                        textvariable=dept_var,
                        values=["CSE","IT","ECE","MECH","CIVIL"])
    dept.grid(row=3,column=1)

    Label(form, text="Gender", font=label_font).grid(row=4,column=0)

    Radiobutton(form, text="Male",
                variable=gender_var,
                value="Male").grid(row=4,column=1,sticky="w")

    Radiobutton(form, text="Female",
                variable=gender_var,
                value="Female").grid(row=4,column=1,sticky="e")

    table = ttk.Treeview(student,
                         columns=("Name","Roll","Email","Dept","Gender"),
                         show="headings")

    table.heading("Name", text="Name")
    table.heading("Roll", text="Roll")
    table.heading("Email", text="Email")
    table.heading("Dept", text="Department")
    table.heading("Gender", text="Gender")

    table.pack(pady=30)

    def submit():

        table.insert("", END, values=(
            name_var.get(),
            roll_var.get(),
            email_var.get(),
            dept_var.get(),
            gender_var.get()
        ))

        name_var.set("")
        roll_var.set("")
        email_var.set("")
        dept_var.set("")
        gender_var.set("")

    Button(student,
           text="SUBMIT",
           font=button_font,
           bg="red",
           fg="white",
           command=submit).pack()

# -------- LOGIN CARD --------
login_frame = Frame(root, bg="black", bd=5)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

Label(login_frame,
      text="MARVEL PORTAL",
      font=title_font,
      bg="black",
      fg="red").pack(pady=20)

Label(login_frame,
      text="Email",
      font=label_font,
      bg="black",
      fg="white").pack()

email_entry = Entry(login_frame, width=30, font=("Arial",12))
email_entry.pack(pady=5)

Label(login_frame,
      text="Password",
      font=label_font,
      bg="black",
      fg="white").pack()

password_entry = Entry(login_frame, show="*", width=30, font=("Arial",12))
password_entry.pack(pady=5)

Button(login_frame,
       text="LOGIN",
       font=button_font,
       bg="red",
       fg="white",
       width=20,
       command=login).pack(pady=20)

root.mainloop()