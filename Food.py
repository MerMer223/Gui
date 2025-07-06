from tkinter import *
from tkinter.ttk import *

top = Tk()

top.title("Food Portions")

top.geometry("500x500")

top.config(background="black")

Email = Label(top,text="Email").place(x=20,y=50)
Email_entry = Entry(top,width=20).place(x=100,y=50)

Password = Label(top,text="Password").place(x=20,y=90)
Password_entry = Entry(top,width=25).place(x=100,y=90)

Food_choice = Label(top,text="What food would yo like: Chicken, Pizza, Pasta or None?").place(x=60,y=150)
Food_entry = Entry(top,width=20).place(x=20,y=190)
Food_amount = Spinbox(top, from_= 0, to = 3).place(x=250,y=190)

Drink_choice = Label(top,text="What would you like to drink: Coke, Pepsi, Sprite, Water or None?").place(x=60,y=250)
Drink_entry = Entry(top,width=20).place(x=20,y=290)
Drink_amount = Spinbox(top, from_= 0, to = 3).place(x=250,y=290)

Dessert_choice = Label(top,text="What dessert would you like to eat: Ice cream, A popsicle, Cake or None?").place(x=60,y=350)
Dessert_entry = Entry(top,width=20).place(x=20,y=390)
Dessert_amount = Spinbox(top, from_= 0, to = 3).place(x=250,y=390)

Submit = Button(top,text="Submit").place(x=100,y=450)


top.mainloop()