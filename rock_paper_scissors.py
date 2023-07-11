import random
from tkinter import *

choices = ["rock", "paper", "scissors"]
computer = None
player = None
# ==============================


def again():
    resultlabel.pack_forget()
    tieLabel.pack_forget()
    winLabel.pack_forget()
    lossLabel.pack_forget()
    againButton.pack_forget()
    exitButton.pack_forget()
    introlabel.pack(fill=BOTH)
    rockButton.pack()
    paperButton.pack()
    scissorsButton.pack()


def rock():
    global player
    global computer
    computer = random.choice(choices)
    player = "rock"
    resultlabel.config(
        text=f"""Computer: {computer}
Player: {player}"""
    )
    if computer == player:
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        tieLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)

    elif computer == "scissors":
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        winLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)

    elif computer == "paper":
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        lossLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)


def paper():
    global player
    global computer
    computer = random.choice(choices)
    player = "paper"
    resultlabel.config(
        text=f"""Computer: {computer}
Player: {player}"""
    )
    if computer == player:
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        tieLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)

    elif computer == "scissors":
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        lossLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)

    elif computer == "rock":
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        winLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)


def scissors():
    global player
    global computer
    computer = random.choice(choices)
    player = "scissors"
    resultlabel.config(
        text=f"""Computer: {computer}
Player: {player}"""
    )
    if computer == player:
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        tieLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)

    elif computer == "paper":
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        winLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)

    elif computer == "rock":
        rockButton.pack_forget()
        paperButton.pack_forget()
        scissorsButton.pack_forget()
        introlabel.pack_forget()
        resultlabel.pack()
        lossLabel.pack()
        againButton.pack(side=LEFT, expand=True, padx=5)
        exitButton.pack(side=RIGHT, expand=True, padx=5)


# ==============================
window = Tk()

rockImage = PhotoImage(file="assets\\rock.png")
paperImage = PhotoImage(file="assets\\paper.png")
scissorsImage = PhotoImage(file="assets\\scissors.png")

window.title("Rock Paper Scissors")
window.geometry("600x500")
window.iconphoto(True, scissorsImage)
window.resizable(False, False)

introlabel = Label(
    window, text="Rock, paper, or scissors?", font=("Comic Sans", 30, "bold"), fg="red"
)
introlabel.pack(fill=BOTH)
tieLabel = Label(window, text="Tie!", font=("Comic Sans", 40, "bold"), fg="blue")
winLabel = Label(window, text="You win!", font=("Comic Sans", 40, "bold"), fg="#00FF00")
lossLabel = Label(window, text="You lose!", font=("Comic Sans", 40, "bold"), fg="red")
resultlabel = Label(
    window,
    text=f"""Computer: {computer}
Player: {player}""",
    font=("Comic Sans", 20, "bold"),
    fg="black",
)
# ==============================

rockButton = Button(
    window,
    text="Rock",
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    image=rockImage,
    compound="bottom",
    height=140,
    width=170,
    command=rock,
)
rockButton.pack()

paperButton = Button(
    window,
    text="Paper",
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    image=paperImage,
    compound="bottom",
    height=140,
    width=170,
    command=paper,
)
paperButton.pack()

scissorsButton = Button(
    window,
    text="Scissors",
    font=("Comic Sans", 30),
    fg="#00FF00",
    bg="black",
    activeforeground="#00FF00",
    activebackground="black",
    image=scissorsImage,
    compound="bottom",
    height=140,
    width=170,
    command=scissors,
)
scissorsButton.pack()

againButton = Button(
    window,
    text="Play again",
    font=("Comic Sans", 20),
    fg="cyan",
    bg="black",
    activeforeground="cyan",
    activebackground="black",
    command=again,
)

exitButton = Button(
    window,
    text="Exit",
    font=("Comic Sans", 20),
    fg="red",
    bg="black",
    activeforeground="red",
    activebackground="black",
    command=quit,
)


window.mainloop()
