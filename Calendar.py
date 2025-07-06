from tkinter import *
import calendar

top = Tk()

top.title("Calendar")

Enter = Label(top,text="Enter Year")

Enter_entry = Entry(top,width=20)

Exit = Button(top,width=20,text="EXIT",command=top.destroy)

Enter.grid(row=2,column=1)
Enter_entry.grid(row=3,column=1)
Exit.grid(row=6,column=1)

def calendar1():
    top1 = Tk()
    top1.title("Calendar2")
    Year = int(Enter_entry.get())
    Cal = calendar.calendar(Year)
    label = Label(top1,text=Cal)
    label.grid(row = 5, column = 1)
    top1.mainloop()

show = Button(top,width=20,text="Show Calendar", command= calendar1)
show.grid(row=4,column=1)
top.mainloop()