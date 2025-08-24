from tkinter import *
from tkinter.ttk import *

top = Tk()

top.title("Weight Converter")

top.geometry("450x450")

top.config(background="Black")

Math = Label(top,text="Mathamateical Table")
Math.grid(row=2,column=2)

number_range = Label(top,text="Number and Range")
number_range.grid(row=3,column=1)





value1 = IntVar()
ten = Radiobutton(top,text="10",variable=value1,value=10)
ten.grid(row=2,column=3)
twenty = Radiobutton(top,text="20",variable=value1,value=20)
twenty.grid(row=3,column=3)
thirty = Radiobutton(top,text="30",variable=value1,value=30)
thirty.grid(row=4,column=3)

select = IntVar()
numbers = Combobox(top,textvariable=select,width=5)
numbers["values"]=tuple(range(101))
numbers.grid(row=3,column=2)

def multiplication():
    tables = ""
    for i in range(value1.get()+1):
        tables += str(select.get())+" x "+str(i)+" = "+str(select.get()*i)+"\n"
    table.configure(text=tables)

generate = Button(top,text="Generate",command=multiplication)
generate.grid(row=1,column=3)
table = Label(top,anchor="center")
table.grid(row=4,column=2)

top.mainloop()