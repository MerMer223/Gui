from tkinter import *

top = Tk()

top.title("Weight Converter")

top.geometry("450x450")

top.config(background="Black")

Kg = Label(top,text="Enter kg amount here")
Kg.grid(row=0, column=1)
Entryboxvalue = StringVar()
Kg_entry = Entry(top,textvariable=Entryboxvalue)
Kg_entry.grid(row=0,column=2)

Pounds = Label(top,text="Pounds")
Pounds.grid(row=3,column=1)

Grams = Label(top,text="Grams")
Grams.grid(row=3,column=2)

Ounce = Label(top,text="Ounce")
Ounce.grid(row=3,column=3)

def conversion():
    grams = float(Entryboxvalue.get())*1000

    pounds = float(Entryboxvalue.get())*2.20462

    ounce = float(Entryboxvalue.get())*35.274
    T1.delete("1.0",END)
    T2.delete("1.0",END)
    T3.delete("1.0",END)
    T1.insert(END,pounds)
    T2.insert(END,grams)
    T3.insert(END,ounce)
Convert = Button(top,text="Convert",command=conversion)
Convert.grid(row=0,column=3)

T1 = Text(top,height=1,width=30)
T1.grid(row=4,column = 1)
T2 = Text(top,height=1,width=30)
T2.grid(row=4,column=2)
T3 = Text(top,height=1,width=30)
T3.grid(row=4,column=3)















top.mainloop()