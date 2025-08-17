from tkinter import *

top = Tk()

top.title("Distance Calculator")

top.geometry("450x450")

top.config(background="Black")

Distance_Calculator = Label(top, text= "Distance Calculator")
Distance_Calculator.grid(row = 0, column= 0)

calculation = Label(top, text="Distance In Hours")
calculation.grid(row=0,column=1)

Time = Label(top,text="Time In Hours")
Time.grid(row=1,column=0)

Entryboxvalue = StringVar()
time_entry = Entry(top,textvariable=Entryboxvalue)
time_entry.grid(row=1,column=2)

speed = Label(top,text="Speed In Hours")
speed.grid(row=2,column=0)

entryboxvalue = StringVar()
speed_entry = Entry(top,textvariable=entryboxvalue)
speed_entry.grid(row=2,column=2)

Distance_Travelled = Label(top,text="Distance Travelled")
Distance_Travelled.grid(row=3,column=0)
def conversion():
    time_amount = float(Entryboxvalue.get())
    speed_amount = float(entryboxvalue.get())*time_amount
    T1.delete("1.0",END)
    T1.insert(END,speed_amount)
    
Convert = Button(top,text="Convert",command=conversion)
Convert.grid(row=3,column=1)



T1 = Text(top,height=1,width=30)
T1.grid(row=3,column = 2)



top.mainloop()