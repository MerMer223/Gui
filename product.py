from tkinter import *
import random
import tkinter.messagebox
top = Tk()

top.title("Guess The Number")

top.geometry("450x450")

top.config(background="Black")
    
numbers = random.randint(1,20)
numbers1 = random.randint(1,20)

welcome = Label(top,text="Welcome to our game")
welcome.grid(row=1,column=1)

name = Label(top,text="What is your name")
name.grid(row=2,column=0)

name_entry = Entry(top,width=5)
name_entry.grid(row=2,column=1)

guess = Label(top,text="Take a guess")
guess.grid(row=4,column=0)

number_guess = Entry(top,width=5)
number_guess.grid(row=4,column=1)

def check_num():
    Entryboxvalue = number_guess.get()
    Entryboxvalue = int(Entryboxvalue)
    if Entryboxvalue > numbers*numbers1:
        tkinter.messagebox.showinfo("High","Your guess is to high")
    if Entryboxvalue < numbers*numbers1:
        tkinter.messagebox.showinfo("Low","Your guess is to low")
    if Entryboxvalue == numbers*numbers1:
        tkinter.messagebox.showinfo("You did it","Good job")

def okay_button():
    entryboxvalue = name_entry.get()
    tkinter.messagebox.showinfo("Hello",entryboxvalue+" Im thinking of the product of two numbers between 1 and 20 one of the numbers are "+str(numbers)+" can you figure out the other one?")


okay = Button(top,text="Okay",command=okay_button)
okay.grid(row=5,column=1)

guess_button = Button(top,text="Guess",command=check_num)
guess_button.grid(row=5,column=2)

top.mainloop()