from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
top = Tk()

top.title("Memorizer")

top.geometry("450x450")

top.config(background="black")

def open():
    file_open=askopenfile(title="Open File")
    if file_open is not None:
        list.delete(0,END)
        read = file_open.readlines()
        for i in read:
            list.insert(END,i.strip())

def save():
    file_save=asksaveasfile()
    if file_save is not None:
        for i in list.get(0,END):
            print(i.strip(),file= file_save)
        list.delete(0,END)

def add():
    list.insert(END,entry.get())
    entry.delete(0,END)

def delete():
    file_delete=list.curselection()
    if file_delete:
        list.delete(file_delete)

Open = Button(top,text="Open",command=open)
Open.pack(side=LEFT)

Delete = Button(top,text="Delete",command=delete)
Delete.pack(side=RIGHT)

Save = Button(top,text="Save",command=save)
Save.pack()

Add = Button(top,text="Add",command=add)
Add.pack()
entry = Entry(top,width=10)
entry.pack()

frame = Frame(top)


scroll = Scrollbar(frame,orient="vertical")
scroll.pack(side=RIGHT)

list = Listbox(frame,width=10,yscrollcommand=scroll.set)
for i in range(1,100):
    list.insert(END,str(i))
list.pack(side=LEFT)
scroll.config(command=list.yview)
frame.pack(side=RIGHT)





top.mainloop()