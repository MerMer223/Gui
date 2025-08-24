from tkinter import *
import tkinter.messagebox
import time

top = Tk()

top.title("Time countdown")

top.geometry("450x450")

top.config(background="black")

hour_set = StringVar()
minute_set = StringVar()
second_set = StringVar()

hour_set.set("00")
minute_set.set("00")
second_set.set("00")

hour = Entry(top,width=50,textvariable=hour_set)
hour.grid(row=0,column=1)
minute = Entry(top,width=50,textvariable=minute_set)
minute.grid(row=0,column=2)
second = Entry(top,width=50,textvariable=second_set)
second.grid(row=0,column=3)

def converter():
    entry=int(hour_set.get())*3600+int(minute_set.get())*60+int(second_set.get())
    hour.config(state='disabled')
    minute.config(state='disabled')
    second.config(state='disabled')
    while entry > -1:
        min,scd=divmod(entry,60,)
        hours=00
        if min>60:
            hours,min=divmod(min,60)
        hour_set.set("{00:2d}".format(hours))
        minute_set.set("{00:2d}".format(min))
        second_set.set("{00:2d}".format(scd))
        top.update()
        time.sleep(1)
        if entry == 0:
            tkinter.messagebox.showinfo("Alert","The time is up")
        entry -= 1



Start = Button(top,text="Start",command=converter)
Start.grid(row=1,column=2)


top.mainloop()