from tkinter import *

top = Tk()

top.title("Frame")

frame = Frame(top)
frame.pack()

frame2 = Frame(top)
frame2.pack(side=BOTTOM)

button = Button(frame,width=20,text="Green")
button.pack(side=LEFT)

button2 = Button(frame,width=20,text="Basketball")
button2.pack(side=RIGHT)

button3= Button(frame,width=20,text="Videogames")
button3.pack(side=LEFT)

button4 = Button(frame2,width=30,text="Sprite")
button4.pack(side=LEFT)

button5 = Button(frame2,width=30,text="MountainDew")
button5.pack(side=RIGHT)

scrollbar = Scrollbar(top)
scrollbar.pack(side=LEFT, fill=Y)

listbox = Listbox(top,width=30,height=40,yscrollcommand=scrollbar.set)
#listbox.insert(1,"Giannis")
#listbox.insert(2,"Jordan")
#listbox.insert(3,"Curry")
for i in range (1,200):
    listbox.insert(END,"Hi"+str(i))
listbox.pack(side=RIGHT,fill=BOTH)
scrollbar.config(command=listbox.yview)



















top.mainloop()