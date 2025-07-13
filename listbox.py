from tkinter import *

top = Tk()

top.title("listbox homework")

top.geometry("450x450")

top.config(background="black")

scrollbar = Scrollbar(top)
scrollbar.pack(side=LEFT, fill=Y)

listbox = Listbox(top,width=30,height=40,yscrollcommand=scrollbar.set)
for i in range (1,300):
    listbox.insert(END,"NBA"+str(i))
listbox.pack(side=RIGHT,fill=BOTH)
scrollbar.config(command=listbox.yview)

top.mainloop()