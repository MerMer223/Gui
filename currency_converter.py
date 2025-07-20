from tkinter import *

top = Tk()

top.title("Currency Converter")

top.geometry("450x450")

top.config(background="Black")

Currency_converter = Label(top, text= "Currency Converter")
Currency_converter.grid(row = 0, column= 0)

conversion = Label(top, text="Rs -> $ Converter")
conversion.grid(row=0,column=1)

source = Label(top,text="Source Currency amount (Rs)")
source.grid(row=1,column=0)

Entryboxvalue = StringVar()
source_entry = Entry(top,textvariable=Entryboxvalue)
source_entry.grid(row=1,column=2)

target = Label(top,text="Target Currency amount ($)")
target.grid(row=2,column=0)

def conversion():
    source_amount = float(Entryboxvalue.get())*0.014

    T1.delete("1.0",END)
    T1.insert(END,source_amount)

Convert = Button(top,text="Convert",command=conversion)
Convert.grid(row=2,column=1)



T1 = Text(top,height=1,width=30)
T1.grid(row=2,column = 2)









top.mainloop()