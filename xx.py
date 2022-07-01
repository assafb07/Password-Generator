import tkinter as tk
from PIL import Image, ImageTk, ImageQt
import random
import pyperclip
from pic2str import logo
import base64
from io import BytesIO


def CopyToClipbaord(passwords):
	pyperclip.copy(passwords)
	spam = pyperclip.paste()
	textbox(passwords)

def generate(y):
	passwords = ''
	for c in range(y):
		passwords += random.choice(chars)
		CopyToClipbaord(passwords)

def textbox(passwords):
	text_box = tk.Text(root, height=6, width=30, padx=15, pady=15,bg = '#d8e6f2',font=("Raleway", 13))
	text_box.insert(1.0, passwords+ '\n\n\n\n'+'your new password is in\nthe clipboard :)')
	text_box.tag_configure("center", justify="center")
	text_box.tag_add("left", 1.0, "end")
	text_box.grid(column=1, row=5)

def tryit():
	x = howlong.get()
	if len(x) < 1: root.mainloop()
	try:
		y = int(x)
		generate(y)
	except:
		root.mainloop()


root = tk.Tk()
root.title('Password Generator')
chars = 'abcdeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^&*()_-+={[}]|\:;"<,>.?/'
passwords = ''

howlong=tk.StringVar()
canvas = tk.Canvas(root, width=400, height=200)
canvas.grid(columnspan=3, rowspan=5)

#logo = Image.open('logo01.png')
byte_data = base64.b64decode(logo)
image_data = BytesIO(byte_data)
logo = Image.open(image_data)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


#instructions
instructions = tk.Label(root, text='How long should your password be?', font=("Raleway", 15))
instructions.grid(columnspan=3, column=0, row=1)
#entry
space = tk.Entry(root,textvariable = howlong, bg = '#d8e6f2')
space.grid(columnspan=4, column=0, row=2, ipadx=5, pady=5)

#generate button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:tryit(), font="Raleway", bg="#587fa1", fg="white", height=1, width=15)
browse_text.set("Generate")
browse_btn.grid(column=1, row=4)


canvas = tk.Canvas(root, width=400, height=150)
canvas.grid(columnspan=5)


root.mainloop()
