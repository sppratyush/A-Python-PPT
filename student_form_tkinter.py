from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Marvel Form")

# icon
root.iconbitmap("my-icon.ico")

root.geometry('500x500+0+0')
root.configure(background='#8B0000')

# image
img = Image.open('marvel.jpg')
resize_img = img.resize((200,120))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img, bg='#8B0000')
img_label.pack(pady=10)

# text label
text_label = Label(root, text="Marvel Login", font=('Arial', 20, 'bold'), bg='#8B0000', fg='white')
text_label.pack(pady=10)

email_label = Label(root, text="Email", font=('Arial', 14, 'bold'), bg='#8B0000', fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root, font=('Arial', 14), fg='black', bg='white')
email_entry.pack(pady=(5,10))

password_label = Label(root, text="Password", font=('Arial', 14, 'bold'), bg='#8B0000', fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root, font=('Arial', 14), fg='black', bg='white', show="*")
password_entry.pack(pady=(5,10))

login_btn = Button(root, text="Login", font=('Arial', 14, 'bold'), bg='black', fg='white')
login_btn.pack(pady=15)

root.mainloop()