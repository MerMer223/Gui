from tkinter import *
from time import strftime
top = Tk()

top.title("Clock")

top.geometry("450x450")

top.config(background="Black")

def function():
    integers = strftime("%H:%M:%S %p")
    label.config(text=integers)
    label.after(1000,function)
label = Label(top,font=("TimesNewRoman",10,),background="White",foreground="Black")
label.pack()
function()















top.mainloop()