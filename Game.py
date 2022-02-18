from email.mime import image
import random
from tkinter import *
from tkinter import font
from turtle import bgcolor, color
from PIL import ImageTk, Image

#Main Screen 
GameBoard = Tk()

#Title of the window
GameBoard.title("Rock, Paper Scissors")

#Board size
GameBoard.geometry('800x600')

# Creating canvas
canvas = Canvas(GameBoard,width=800, height=600)
canvas.grid(row=0,column=0)

# Score board 
pscore = 0
cscore = 0

# Creating labels on GUI window
l1 = Label(GameBoard,text='Player',font=('Algerian', 25),fg='#006400')
l2 = Label(GameBoard,text='Computer',font=('Algerian', 25),fg='#006400')
l3 = Label(GameBoard, text='Vs',font=('Algerian', 40),fg='#FF0000')
exit_butten = Button(GameBoard, text="Exit", bg='#FF0000', fg='#000000', command=GameBoard.destroy)

# placing Labels on Window
l1.place(x=80, y=20)
l2.place(x=560, y=20)
l3.place(x=370, y=220)
exit_butten.place(x=360, y=540)

# Default images
DImage = Image.open("Images/default.jpg")
DImage = DImage.resize((300,300))

# Move the image from left to right
DImageFlip = DImage.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
DImage = ImageTk.PhotoImage(DImage)
DImageFlip = ImageTk.PhotoImage(DImageFlip)

# Rock image
RImage = Image.open("Images/rock.jpg")
RImage = RImage.resize((300,300))

# Flip Rock image from left to right
RImageFlip = RImage.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
RImage = ImageTk.PhotoImage(RImage)
RImageFlip = ImageTk.PhotoImage(RImageFlip)

# Paper image
PImage = Image.open("Images/paper.jpg")
PImage = PImage.resize((300,300))

# Flip Paper image from left to right
PImageFlip = PImage.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
PImage = ImageTk.PhotoImage(PImage)
PImageFlip = ImageTk.PhotoImage(PImageFlip)

# Scissor image
SImage = Image.open("Images/scissor.jpg")
SImage = SImage.resize((300,300))

# Flip Scisseors image from left to right
SImageFlip = SImage.transpose(Image.FLIP_LEFT_RIGHT)

# Loading images to put on canvas
SImage = ImageTk.PhotoImage(SImage)
SImageFlip = ImageTk.PhotoImage(SImageFlip)

# Selection Image
SelectImage = Image.open("Images/Selection.jpg")
SelectImage = SelectImage.resize((300,130))
SelectImage = ImageTk.PhotoImage(SelectImage)

# Putting image on canvas on specific coordinates
canvas.create_image(0, 100, anchor=NW, image=DImage)
canvas.create_image(500, 100, anchor=NW, image=DImageFlip)
canvas.create_image(0, 400, anchor=NW, image=SelectImage)
canvas.create_image(500, 400, anchor=NW, image=SelectImage)

# Game logic based on player, if all player moves are wrong then the computer is the winner of the round 
def gamerules(playerchoice, computerchoice) :
    score = 0
    if playerchoice == 1 and computerchoice == 3 :
        score += 1
    elif playerchoice == 2 and computerchoice == 1 :
        score += 1
    elif playerchoice == 3 and computerchoice == 2 :
        score += 1
    return score

# Game start 
def game(player) :
    clear()
    select = [1, 2, 3]

    # Random Computer select 
    computer = random.choice(select)
    print("Computer:",computer)
    # Setting Player image on canvas
    if player == 1:
        canvas.create_image(0, 100, anchor=NW, image=RImage)
    elif player == 2: 
        canvas.create_image(0, 100, anchor=NW, image=PImage)
    else:  
        canvas.create_image(0, 100, anchor=NW, image=SImage)

    # Setting computer image on canvas
    if computer == 1:
        canvas.create_image(500, 100, anchor=NW, image=RImageFlip)
    elif computer == 2: 
        canvas.create_image(500, 100, anchor=NW, image=PImageFlip)
    else:
        canvas.create_image(500, 100, anchor=NW, image=SImageFlip)

    if player == computer:
            res = 'Drew'
    else:
        statue = gamerules(player,computer)
        if statue >= 1: 
            global pscore 
            pscore = pscore +1
            res = "Player win"
            print(pscore)
        else:
            global cscore
            cscore = cscore +1 
            res = "Computer Win"
            

     # Putting result on canvas
    canvas.create_text(390, 580, text='Result: ' + res,fill="black", font=('Algerian', 25), tag='result')
    canvas.create_text(120,100,text="Player "+(str(pscore)),font=('Algerian', 25),fill='red',tag='pscore')
    canvas.create_text(600,100,text="Computer "+(str(cscore)),font=('Algerian', 25),fill='red',tag='cscore')

    # Prints the winner of the Game after 3 rounds on the board 
    if (pscore == 3 or cscore ==3):
        if pscore > cscore:
            canvas.delete('result')
            canvas.create_text(390, 580, text='The Winner is: Player',fill="black", font=('Algerian', 25), tag='result')
            canvas
        else:
            canvas.delete('result')
            canvas.create_text(390, 580, text='The Winner is: Computer',fill="black", font=('Algerian', 25), tag='result')

# Clears the board 
def clear():
    #Remove result from canvas 
    canvas.delete('result')
    canvas.delete('pscore')
    canvas.delete('cscore')
    # Sets duafult imges bacl to the canvas
    canvas.create_image(0, 100, anchor=NW, image=DImage)
    canvas.create_image(500, 100, anchor=NW, image=DImageFlip)


#Button for selecting rock 
rock_b = Button(GameBoard,text='Rock',fg='#FF0000', command=lambda: game(1))
rock_b.place(x=10,y=500)
#Button for paper
paper_b = Button(GameBoard,text='Paper',fg='#FF0000',command=lambda: game(2))
paper_b.place(x=103,y=500)
#Button for scissors 
scissor_b = Button(GameBoard,text='Scissor',fg='#FF0000', command=lambda: game(3))
scissor_b.place(x=195, y=500)

#Button for clear 
#clear_b = Button(GameBoard,text="CLEAR",font=('Times', 10, 'bold'),width=10, command=clear).place(x=370, y=28)


GameBoard.mainloop()
