import tkinter
from tkinter import *
import random

root = Tk()
check=0
theBoard = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
character = ["X", "O"]
indexx = 0
winner = "no winner"
isWin = False
playerHistory=1
turn = 0
randomizedIndex = int
botHistory=1

def checkWin():
    global winner
    global isWin
    global theBoard
    global check
    #horizontal win con
    if theBoard[0]==theBoard[1] == theBoard[2]:
        isWin= True
        winner=theBoard[0]
    if theBoard[3]==theBoard[4]==theBoard[5]:
        isWin= True
        winner=theBoard[4]
    if theBoard[6]==theBoard[7]==theBoard[8]:
        isWin= True
        winner=theBoard[7]
    #vertical win con
    if theBoard[0]==theBoard[3]==theBoard[6]:
        isWin= True
        winner=theBoard[0]
    if theBoard[1]==theBoard[4]==theBoard[7]:
        isWin= True
        winner=theBoard[1]
    if theBoard[2] == theBoard[5]== theBoard[8]:
        isWin = True
        winner = theBoard[2]
    #diagonal win con
    if theBoard[0] == theBoard[4] == theBoard[8]:
        isWin = True
        winner = theBoard[0]
    if theBoard[2] == theBoard[4]== theBoard[6]:
        isWin = True
        winner = theBoard[2]
    if winner== "X" or winner == "O":
        pemenang = tkinter.Label(root, text="the winner is " + winner).place(x=150, y=0)
        return
    if check == 9 and isWin != True:
        pemenang = tkinter.Label(root, text="Draw").place(x=150, y=0)

def cornerSolution(thesign):
    global theBoard
    if theBoard[1]==theBoard[3] == thesign and theBoard[0]=="1":
        return 0
    elif theBoard[1]==theBoard[5] == thesign and theBoard[2]=="3":
        return 2
    elif theBoard[7]==theBoard[3] == thesign and theBoard[6]=="7":
        return 6
    elif theBoard[7]==theBoard[5] == thesign and theBoard[8]=="9":
        return 8
    else:
        return 10

def lineWinSolution(thesign):
    global  theBoard

    # 123 horizontal
    if theBoard[0]==theBoard[1] == thesign and theBoard[2]=="3":
        return 2
    elif theBoard[1]==theBoard[2] ==thesign and theBoard[0]=="1":
        return 0
    elif theBoard[2]==theBoard[0] ==thesign and theBoard[1]=="2":
        return 1

    # 456
    elif theBoard[3]==theBoard[4] ==thesign and theBoard[5]=="6":
        return 5
    elif theBoard[3]==theBoard[5] ==thesign and theBoard[4]=="5":
        return 4
    elif theBoard[5]==theBoard[4] ==thesign and theBoard[3]=="4":
        return 3

    # 789
    elif theBoard[6] == theBoard[7] ==thesign and theBoard[8] == "9":
        return 8
    elif theBoard[6] == theBoard[8] ==thesign and theBoard[7] == "8":
        return 7
    elif theBoard[7] == theBoard[8] ==thesign and theBoard[6] == "7":
        return 6

    #147 vertical
    elif theBoard[0] == theBoard[3] ==thesign and theBoard[6] == "7":
        return 6
    elif theBoard[0] == theBoard[6] ==thesign and theBoard[3] == "4":
        return 3
    elif theBoard[6] == theBoard[3] ==thesign and theBoard[0] == "7":
        return 0

    # 258
    elif theBoard[1] == theBoard[4] ==thesign and theBoard[7] == "8":
        return 7
    elif theBoard[1] == theBoard[7] ==thesign and theBoard[4] == "5":
        return 4
    elif theBoard[6] == theBoard[3] ==thesign and theBoard[1] == "2":
        return 1

    # 369
    elif theBoard[2] == theBoard[5] ==thesign and theBoard[8] == "9":
        return 8
    elif theBoard[2] == theBoard[8] ==thesign and theBoard[5] == "6":
        return 5
    elif theBoard[8] == theBoard[5] ==thesign and theBoard[2] == "3":
        return 2

    # 159 diagonal
    elif theBoard[0] == theBoard[4] ==thesign and theBoard[8] == "9":
        return 8
    elif theBoard[0] == theBoard[8] ==thesign and theBoard[4] == "5":
        return 4
    elif theBoard[8] == theBoard[4] ==thesign and theBoard[0] == "1":
        return 0

    # 357
    elif theBoard[2] == theBoard[4] ==thesign and theBoard[6] == "7":
        return 6
    elif theBoard[2] == theBoard[6] ==thesign and theBoard[4] == "5":
        return 4
    elif theBoard[4] == theBoard[6] ==thesign and theBoard[2] == "1":
        return 2

    else:
        return 10

def crossSolution(thevariable):
    if thevariable == 1:
        return 9
    elif thevariable == 2:
        return 8
    elif thevariable == 3:
        return 7
    elif thevariable == 4:
        return 6
    elif thevariable == 6:
        return 4
    elif thevariable == 7:
        return 3
    elif thevariable == 8:
        return 2
    elif thevariable == 9:
        return 1

def positionForY(thenumber):
    if thenumber==1 or thenumber ==2 or thenumber ==3:
        return 0
    if thenumber==4 or thenumber ==5 or thenumber ==6:
        return 1
    if thenumber==7 or thenumber == 8 or thenumber == 9:
        return 2

def randomizedSolution():
    global theBoard
    randomizedIndex=1
    while (True):
        randomizedIndex = random.randint(0, 8)
        if theBoard[randomizedIndex] != character[0] and theBoard[randomizedIndex] != character[1]:
            break
    theBoard[randomizedIndex] = character[1]
    label = tkinter.Label(text=character[1]).place(x=randomizedIndex % 3 * 50 + 17,
                                                   y=positionForY(randomizedIndex + 1) * 50 + 13)
    print("randomizedIndex ", randomizedIndex)

def bot():
    global turn
    global theBoard
    global randomizedIndex
    global botHistory
    xpad=0
    ypad=0
    #turn 1
    if turn ==1:
        #if player didn't choose mid
        if theBoard[4] == "5":
            theBoard[4] = character[1]
            Label = tkinter.Label(text=character[1]).place(x=50+17, y=50+13)
            botHistory=4
            return
        #if player choose mid
        elif theBoard[4] == "X":
            randomizedIndex=random.randint(0,1)
            theBoard[randomizedIndex]= character[1]
            Label = tkinter.Label(text=character[1]).place(x=randomizedIndex*50+17, y=13)
            botHistory=randomizedIndex
            return

    elif turn ==2:
        print(lineWinSolution("X"))
        if cornerSolution(character[0])!=10:
            numberIndex = int(cornerSolution(character[0]))
            theBoard[numberIndex] = character[1]
            Label = tkinter.Label(text=character[1]).place(x=numberIndex % 3 * 50 + 17,
                                                           y=positionForY(numberIndex + 1) * 50 + 13)
            botHistory = numberIndex
            return

        elif botHistory!=4 and lineWinSolution(character[0])!=10:
            print("1")
            numberIndex=int(crossSolution(playerHistory+1)-1)
            theBoard[numberIndex]=character[1]
            Label = tkinter.Label(text=character[1]).place(x=numberIndex%3 * 50 + 17, y= positionForY(numberIndex+1)*50+13)
            botHistory= numberIndex
            return

        elif (botHistory!=4 and (lineWinSolution(character[0]))==10) or (botHistory==4 and (lineWinSolution(character[0]))==10):
            randomizedSolution()

        elif botHistory ==4 and lineWinSolution(character[0])!=10:
            print("2")
            numberIndex=int(lineWinSolution(character[0]))
            theBoard[numberIndex]=character[1]
            label= tkinter.Label(text= character[1]).place(x=numberIndex%3 *50 +17, y= positionForY(numberIndex+1)*50+13)
            return
    else:
        if lineWinSolution(character[1])!=10:
            numberIndex = int(lineWinSolution(character[1]))
            theBoard[numberIndex]=character[1]
            label= tkinter.Label(text= character[1]).place(x=numberIndex%3 *50 +17, y= positionForY(numberIndex+1)*50+13)
            return

        elif lineWinSolution(character[0])!=10:
            numberIndex = int(lineWinSolution(character[0]))
            theBoard[numberIndex] = character[1]
            label = tkinter.Label(text=character[1]).place(x=numberIndex % 3 * 50 + 17,
                                                           y=positionForY(numberIndex + 1) * 50 + 13)
            return

        elif lineWinSolution(character[0])==10 and lineWinSolution(character[0])==10:
            randomizedSolution()


def setToInactive2(index,kolom,baris):
    global check
    global indexx
    global winner
    global playerHistory
    global botHistory
    global turn


    checkWin()
    if turn == 4:
        print ("it's a Draw")
        pemenang = tkinter.Label(root, text="Draw").place(x=150, y=0)
        a=0
        while(True):
            if theBoard[a]!=character[0] and theBoard[a]!=character[1]:
                theBoard[a] = character[0]
                label = tkinter.Label(text=character[0]).place(x=a % 3 * 50 + 17,
                                                                          y=positionForY(a + 1) * 50 + 13)
                break
            a+=1
        return
    if theBoard[index]=="X" or theBoard[index]=="O":
        return

    if isWin==True:
        return

    turn += 1
    print(turn)

    theBoard[index] = character[0]
    Label = tkinter.Label(text=character[indexx]).place(x=kolom*50+17,y=baris*50+13)
    check+=1
    playerHistory = index

    checkWin()
    bot()
    checkWin()


tombol1 = Button(root, text="  ", command=lambda: setToInactive2(0, 0, 0), padx=17, pady=13).place(x=0, y=0)
tombol2 = Button(root, text="  ", command=lambda: setToInactive2(1, 1, 0), padx=17, pady=13).place(x=50, y=0)
tombol3 = Button(root, text="  ", command=lambda: setToInactive2(2, 2, 0), padx=17, pady=13).place(x=100, y=0)
tombol4 = Button(root, text="  ", command=lambda: setToInactive2(3, 0, 1), padx=17, pady=13).place(x=0, y=50)
tombol5 = Button(root, text="  ", command=lambda: setToInactive2(4, 1, 1), padx=17, pady=13).place(x=50, y=50)
tombol6 = Button(root, text="  ", command=lambda: setToInactive2(5, 2, 1), padx=17, pady=13).place(x=100, y=50)
tombol7 = Button(root, text="  ", command=lambda: setToInactive2(6, 0, 2), padx=17, pady=13).place(x=0, y=100)
tombol8 = Button(root, text="  ", command=lambda: setToInactive2(7, 1, 2), padx=17, pady=13).place(x=50, y=100)
tombol9 = Button(root, text="  ", command=lambda: setToInactive2(8, 2, 2), padx=17, pady=13).place(x=100, y=100)

label1= Label(root, text=" ticTacToe Bot By Aikhusy :D ").place(x=0,y=150)
root.title("Artificial Stupidity")
root.mainloop()