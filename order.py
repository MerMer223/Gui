from tkinter import *
from tkinter.ttk import *
import tkinter.messagebox
top = Tk()

top.title("Pizza App")

top.geometry("450x450")

top.config(background="black")

welcome = Label(top,text="Welcome to Pizza Hut")
welcome.grid(row=1,column=2)

selection = Label(top,text="Select your pizza:")
selection.grid(row=2,column=1)

select = StringVar()
selection1 = Combobox(top,textvariable=select,width=5)
selection1["values"] = ("Cheese","Peperonni","Veggie")
selection1.grid(row=2,column=2)

quantity = Label(top,text="Enter Quantity")
quantity.grid(row=3,column=1)

quantity2 = IntVar()
quantity1 = Combobox(top,textvariable=quantity2,width=5)
quantity1["values"] = tuple(range(11))
quantity1.grid(row=3,column=2)

value1 = StringVar()
s = Radiobutton(top,text="S",variable=value1,value="S")
s.grid(row=2,column=3)
m = Radiobutton(top,text="M",variable=value1,value="M")
m.grid(row=3,column=3)
l = Radiobutton(top,text="L",variable=value1,value="L")
l.grid(row=4,column=3)


def Order():
    pizzas = select.get()
    quantities = quantity2.get()
    size = value1.get()
    if not size:
        tkinter.messagebox.showerror("Error","Please selecct a size")
        return
    size_text = {"S": "Small","M": "Medium", "L": "Large"}
    result.config(text=f"You ordered {quantities} {size_text[size]} {pizzas} pizzas")


order = Button(top,text="Order",command=Order)
order.grid(row=5,column=3)

result = Label(top,text="")
result.grid(row=6,column=2)


top.mainloop()