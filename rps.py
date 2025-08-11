from tkinter import *
import random
Pscore = 0
Cscore = 0
options = [('rock',0), ('paper',1),('scissors',2)]
def Computer_Wins():  
    global Cscore,Pscore
    Cscore += 1
    Winner.config(text= "Computer Won")
    Computer_score.config(text="Computer Score "+str(Cscore))
    Player_score.config(text="Player Score "+str(Pscore))
def Player_Wins():
    global Cscore,Pscore
    Pscore += 1
    Winner.config(text= "Player Won")
    Computer_score.config(text="Computer Score "+str(Cscore))
    Player_score.config(text="Player Score "+str(Pscore))
def tie():
    global Cscore,Pscore
    Winner.config(text= "Tie")
    Computer_score.config(text="Computer Score "+str(Cscore))
    Player_score.config(text="Player Score "+str(Pscore))
def player_choice(Player_input):
    global Pscore,Cscore
    print(Player_input)
    Computer_input = get_computer_choice()
    print(Computer_input)
    Player_choice.config(text="You Selected "+Player_input[0])
    Computer_choice.config(text="Computer Selected "+Computer_input[0])
    if Player_input == Computer_input:
        tie()
    if Player_input[1] == 0:
        if Computer_input[1] == 1:
            Computer_Wins()
        elif Computer_input[1] == 2:
            Player_Wins()
    elif Player_input[1] == 1:
        if Computer_input[1] == 0:
            Player_Wins()
        elif Computer_input[1] == 2:
            Computer_Wins()
    elif Player_input[1] == 2:
        if Computer_input[1] == 1:
            Player_Wins()
        elif Computer_input[1] == 0:
            Computer_Wins()
def get_computer_choice():
    return random.choice(options)
top = Tk()

top.title("Rock Paper Scissors")

top.geometry("450x450")

top.config(background="Black")

label = Label(top,text= "Rock Paper Scissors")
label.pack()

Winner = Label(top,text="Winner",pady=10)
Winner.pack()

Inputframe = Frame(top)
Inputframe.pack()

player = Label(Inputframe,text="Your Options")
player.grid(row=0,column=0,pady=10)

Rock = Button(Inputframe,text="Rock",command= lambda: player_choice(options[0]))
Rock.grid(row=1,column=1,padx=8,pady=5)

Paper = Button(Inputframe,text="Paper",command= lambda: player_choice(options[1]))
Paper.grid(row=1,column=2,padx=8,pady=5)

Scissors = Button(Inputframe,text="Scissors", command= lambda: player_choice(options[2]))
Scissors.grid(row=1,column=3,padx=8,pady=5)

Score = Label(Inputframe,text="Score")
Score.grid(row=2,column=0)

Player_choice = Label(Inputframe,text="You Selected")
Player_choice.grid(row=3,column=1,pady=5)

Player_score = Label(Inputframe,text="Player Score")
Player_score.grid(row=3,column=2,pady=5)

Computer_choice = Label(Inputframe,text="Computer's Choice")
Computer_choice.grid(row=4,column=1,pady=5)

Computer_score = Label(Inputframe,text="Computer Score")
Computer_score.grid(row=4,column=2,padx=(10,0),pady=5)




top.mainloop()