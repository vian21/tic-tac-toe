from tkinter import*

window = Tk()

window.title("Tic Tac Toe")
window.geometry("290x300")

# array 
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
currentPlayer = 1
won=False

def textFor(value):
    if(value == 0):
        return ""

    if(value == 1):
        return "X"

    if(value == 2):
        return "O"


def switchPlayer():
    global currentPlayer
    
    if currentPlayer == 1:
        currentPlayer = 2

    elif currentPlayer == 2:
        currentPlayer = 1

    
    #print(currentPlayer)


def play(x, y):
    if won==False:
        global board
        
        if board[x][y] == 0:
            board[x][y] = currentPlayer

            checkWinner()
    Board()
    #print(board[x][y])

def checkWinner():
    #horizontal checks for player one
    if board[0][0]==1 and board[0][1]==1 and board[0][2]==1:
        printWinner()
    elif board[1][0]==1 and board[1][1]==1 and board[1][2]==1:
        printWinner()
    elif board[2][0]==1 and board[2][1]==1 and board[2][2]==1:
        printWinner()

    #vertical checks for player one
    elif board[0][0]==1 and board[1][0]==1 and board[2][0]==1:
        printWinner()
    elif board[0][1]==1 and board[1][1]==1 and board[2][1]==1:
        printWinner()
    elif board[0][2]==1 and board[1][2]==1 and board[2][2]==1:
        printWinner()
    
     #diagonal checks for player one
    elif board[0][0]==1 and board[1][1]==1 and board[2][2]==1:
        printWinner()
    elif board[0][2]==1 and board[1][1]==1 and board[2][0]==1:
        printWinner()
    

    #horizontal checks for player two
    elif board[0][0]==2 and board[0][1]==2 and board[0][2]==2:
        printWinner()
    elif board[1][0]==2 and board[1][1]==2 and board[1][2]==2:
        printWinner()
    elif board[2][0]==2 and board[2][1]==2 and board[2][2]==2:
        printWinner()
    
    #vertical checks for player two
    elif board[0][0]==2 and board[1][0]==2 and board[2][0]==2:
        printWinner()
    elif board[0][1]==2 and board[1][1]==2 and board[2][1]==2:
        printWinner()
    elif board[0][2]==2 and board[1][2]==2 and board[2][2]==2:
        printWinner()
    
     #diagonal checks for player two
    elif board[0][0]==2 and board[1][1]==2 and board[2][2]==2:
        printWinner()
    elif board[0][2]==2 and board[1][1]==2 and board[2][0]==2:
        printWinner()
    
    else:
        switchPlayer()
    

def printWinner():
    global won

    won=True

    print("🎉 winner is: "+str(currentPlayer))

width = 10
height = 5


'''

      x y z
    a
    b
    c

'''
def Board():
    # row one
    ax = Button(window, text=textFor(board[0][0]), width=width, height=height, command=lambda: play(0, 0)).grid(row=0)
    ay = Button(window, text=textFor(board[0][1]), width=width, height=height, command=lambda: play(0, 1)).grid(row=0, column=1)
    az = Button(window, text=textFor(board[0][2]), width=width, height=height, command=lambda: play(0, 2)).grid(row=0, column=2)

    # row 2
    bx = Button(window, text=textFor(board[1][0]), width=width, height=height, command=lambda: play(1, 0)).grid(row=1)
    by = Button(window, text=textFor(board[1][1]), width=width, height=height, command=lambda: play(1, 1)).grid(row=1, column=1)
    bz = Button(window, text=textFor(board[1][2]), width=width, height=height, command=lambda: play(1, 2)).grid(row=1, column=2)

    # row 3
    cx = Button(window, text=textFor(board[2][0]), width=width, height=height, command=lambda: play(2, 0)).grid(row=2)
    cy = Button(window, text=textFor(board[2][1]), width=width, height=height, command=lambda: play(2, 1)).grid(row=2, column=1)
    cz = Button(window, text=textFor(board[2][2]), width=width, height=height, command=lambda: play(2, 2)).grid(row=2, column=2)


Board()

window.mainloop()
