from turtle import *
import turtle

turtle.title("Chess with a Creative Name")

screen = turtle.Screen()
screen.setup(900,900)
screen.bgcolor("Antiquewhite2")


board = Pen("turtle")
board.ht()
board.speed(0)


board2 = Pen("turtle")
board2.ht()
board2.speed(0)


board2.up()
board2.goto(300,300)
board2.down()
# Grid
grid = Pen("turtle")
grid.ht()
grid.speed(0)
grid.up()
grid.goto(-315, 320)
grid.down()
gridX = -315
gridY = 320
letters = ["a", "b","c","d","e","f","g","h"]
for i in (letters):
    grid.write(i,font = ('Ariel', 10, 'bold'))
    gridX += 60
    grid.up()
    grid.goto(gridX,gridY)
    grid.down()

grid.up()
grid.goto(-360,270)
gridX = -360
gridY = 270
numbers = ["8", "7","6","5","4","3","2","1"]
for i in (numbers):
    grid.write(i,font = ('Ariel', 10, 'bold'))
    gridY -= 60
    grid.up()
    grid.goto(gridX,gridY)
    grid.down()
    
    
# Side Screens

board2.fillcolor("burlywood4")
board2.begin_fill()
for i in range(4):
    board2.forward(100)
    board2.right(90)
    board2.forward(100)
board2.end_fill()

board2.up()
board2.goto(245,250)
board2.write("White Captured", font = ('Ariel', 15, 'bold'))


board2. up()
board2.goto(300,0)

board2.fillcolor("burlywood4")
board2.begin_fill()
for i in range(4):
    board2.forward(100)
    board2.right(90)
    board2.forward(100)
board2.end_fill()

board2.up()
board2.goto(245,-50)
board2.down()
board2.write("Black Captured", font = ('Ariel', 15, 'bold'))
board2.down()
# Reset Button

reset = Pen("turtle")
reset.ht()
reset.speed(0)
reset.up()
reset.goto(-340,-300)
reset.down()

reset.fillcolor("red")
reset.begin_fill()
reset.forward(100)
reset.right(90)
reset.forward(50)
reset.right(90)
reset.forward(100)
reset.right(90)
reset.forward(50)
reset.end_fill()

reset.up()
reset.goto(-317,-335)
reset.down()
reset.setheading(0)
reset.write("RESET", font = ('Ariel', 20, 'normal',))
reset.up()
reset.goto(-306,-345)
reset.down()
reset.write("Press r", font = ('Ariel', 10, 'bold',))


#Checks

def light():
    board.fillcolor("azure2")
    board.begin_fill()
    for i in range (4):
        board.forward(30)
        board.right(90)
        board.forward(30)
    board.end_fill()
def dark():
    board.fillcolor("cadetblue4")
    board.begin_fill()
    for i in range(4):
        board.forward(30)
        board.right(90)
        board.forward(30)

    board.end_fill()


def row(x, y,z):
    board.up()
    board.goto(x,y)
    board.down()
    for i in range(8):
        if z % 2 == 0:
            dark()
        else:
            light()
        x += 60
        z += 1
        board.up()
        board.goto(x,y)
        board.down()



checkXStart = -310
checkYStart= 300
firstSquare = 1
for i in range(8):
    row(checkXStart,checkYStart, firstSquare)
    checkYStart -= 60
    firstSquare += 1

    
    
# White Pieces

screen.register_shape('wKing.gif')
wK = Pen()
wK.speed(0)
wK.shape('wKing.gif')
wK.up()
wK.goto(-70,-150)


screen.register_shape('wQ.gif')
wQ = Pen()
wQ.speed(0)
wQ.shape('wQ.gif')
wQ.up()
wQ.goto(-130,-150)

screen.register_shape('wBishop.gif')
wB = Pen()
wB.speed(0)
wB.shape('wBishop.gif')
wB.up()
wB.goto(-190,-150)

wB2 = Pen()
wB2.speed(0)
wB2.shape('wBishop.gif')
wB2.up()
wB2.goto(-10,-150)

screen.register_shape('wKn.gif')
wKn = Pen()
wKn.speed(0)
wKn.shape('wKn.gif')
wKn.up()
wKn.goto(50,-150)

wKn2 = Pen()
wKn2.speed(0)
wKn2.shape('wKn.gif')
wKn2.up()
wKn2.goto(-250,-150)

screen.register_shape('wR.gif')
wR = Pen()
wR.speed(0)
wR.shape('wR.gif')
wR.up()
wR.goto(110,-150)

wR2 = Pen()
wR2.speed(0)
wR2.shape('wR.gif')
wR2.up()
wR2.goto(-310,-150)

screen.register_shape('wP.gif')
wP = Pen()
wP.speed(0)
wP.shape('wP.gif')
wP.up()
wP.goto(110,-90)

wP2 = Pen()
wP2.speed(0)
wP2.shape('wP.gif')
wP2.up()
wP2.goto(-310,-90)

wP3 = Pen()
wP3.speed(0)
wP3.shape('wP.gif')
wP3.up()
wP3.goto(-250,-90)

wP4 = Pen()
wP4.speed(0)
wP4.shape('wP.gif')
wP4.up()
wP4.goto(50,-90)

wP5 = Pen()
wP5.speed(0)
wP5.shape('wP.gif')
wP5.up()
wP5.goto(-10,-90)

wP6 = Pen()
wP6.speed(0)
wP6.shape('wP.gif')
wP6.up()
wP6.goto(-190,-90)

wP7 = Pen()
wP7.speed(0)
wP7.shape('wP.gif')
wP7.up()
wP7.goto(-130,-90)

wP8 = Pen()
wP8.speed(0)
wP8.shape('wP.gif')
wP8.up()
wP8.goto(-70,-90)

# Black Pieces

screen.register_shape('bKing.gif')
bK = Pen()
bK.speed(0)
bK.shape('bKing.gif')
bK.up()
bK.goto(-70,270)

screen.register_shape('bQ.gif')
bQ = Pen()
bQ.speed(0)
bQ.shape('bQ.gif')
bQ.up()
bQ.goto(-130,270)

screen.register_shape('bBishop.gif')
bB = Pen()
bB.speed(0)
bB.shape('bBishop.gif')
bB.up()
bB.goto(-190,270)

bB2 = Pen()
bB2.speed(0)
bB2.shape('bBishop.gif')
bB2.up()
bB2.goto(-10,270)

screen.register_shape('bKn.gif')
bKn = Pen()
bKn.speed(0)
bKn.shape('bKn.gif')
bKn.up()
bKn.goto(50,270)

bKn2 = Pen()
bKn2.speed(0)
bKn2.shape('bKn.gif')
bKn2.up()
bKn2.goto(-250,270)

screen.register_shape('bR.gif')
bR = Pen()
bR.speed(0)
bR.shape('bR.gif')
bR.up()
bR.goto(110,270)

bR2 = Pen()
bR2.speed(0)
bR2.shape('bR.gif')
bR2.up()
bR2.goto(-310,270)

screen.register_shape('bP.gif')
bP = Pen()
bP.speed(0)
bP.shape('bP.gif')
bP.up()
bP.goto(110,210)

bP2 = Pen()
bP2.speed(0)
bP2.shape('bP.gif')
bP2.up()
bP2.goto(-310,210)

bP3 = Pen()
bP3.speed(0)
bP3.shape('bP.gif')
bP3.up()
bP3.goto(-250,210)

bP4 = Pen()
bP4.speed(0)
bP4.shape('bP.gif')
bP4.up()
bP4.goto(50,210)

bP5 = Pen()
bP5.speed(0)
bP5.shape('bP.gif')
bP5.up()
bP5.goto(-10,210)

bP6 = Pen()
bP6.speed(0)
bP6.shape('bP.gif')
bP6.up()
bP6.goto(-190,210)


bP7 = Pen()
bP7.speed(0)
bP7.shape('bP.gif')
bP7.up()
bP7.goto(-130,210)

bP8 = Pen()
bP8.speed(0)
bP8.shape('bP.gif')
bP8.up()
bP8.goto(-70,210)


# Piece Functions

def move1(x, y):
    wK.goto(x,y)
def move2(x,y):
    wQ.goto(x,y)
def move3(x,y):
    wB.goto(x,y)
def move4(x,y):
    wB2.goto(x,y)
def move5(x,y):
    wKn.goto(x,y)
def move6(x,y):
    wKn2.goto(x,y)
def move7(x,y):
    wR.goto(x,y)
def move8(x,y):
    wR2.goto(x,y)
def move9(x,y):
    wP.goto(x,y)
def move10(x,y):
    wP2.goto(x,y)
def move11(x,y):
    wP3.goto(x,y)
def move12(x,y):
    wP4.goto(x,y)
def move13(x,y):
    wP5.goto(x,y)
def move14(x,y):
    wP6.goto(x,y)
def move15(x,y):
    wP7.goto(x,y)
def move16(x,y):
    wP8.goto(x,y)


def move17(x,y):
    bK.goto(x,y)
def move18(x,y):
    bQ.goto(x,y)
def move19(x,y):
    bB.goto(x,y)
def move20(x,y):
    bB2.goto(x,y)
def move21(x,y):
    bKn.goto(x,y)
def move22(x,y):
    bKn2.goto(x,y)
def move23(x,y):
    bR.goto(x,y)
def move24(x,y):
    bR2.goto(x,y)
def move25(x,y):
    bP.goto(x,y)
def move26(x,y):
    bP2.goto(x,y)
def move27(x,y):
    bP3.goto(x,y)
def move28(x,y):
    bP4.goto(x,y)
def move29(x,y):
    bP5.goto(x,y)
def move30(x,y):
    bP6.goto(x,y)
def move31(x,y):
    bP7.goto(x,y)
def move32(x,y):
    bP8.goto(x,y)

# White Piece On Drag

wK.ondrag(move1)
wQ.ondrag(move2)
wB.ondrag(move3)
wB2.ondrag(move4)
wKn.ondrag(move5)
wKn2.ondrag(move6)
wR.ondrag(move7)
wR2.ondrag(move8)
wP.ondrag(move9)
wP2.ondrag(move10)
wP3.ondrag(move11)
wP4.ondrag(move12)
wP5.ondrag(move13)
wP6.ondrag(move14)
wP7.ondrag(move15)
wP8.ondrag(move16)

# Black Piece On drag
bK.ondrag(move17)
bQ.ondrag(move18)
bB.ondrag(move19)
bB2.ondrag(move20)
bKn.ondrag(move21)
bKn2.ondrag(move22)
bR.ondrag(move23)
bR2.ondrag(move24)
bP.ondrag(move25)
bP2.ondrag(move26)
bP3.ondrag(move27)
bP4.ondrag(move28)
bP5.ondrag(move29)
bP6.ondrag(move30)
bP7.ondrag(move31)
bP8.ondrag(move32)

# Reset Button

def reset1():
    wK.goto(-70,-150)
    wQ.goto(-130,-150)
    wB.goto(-190,-150)
    wB2.goto(-10,-150)
    wKn.goto(50,-150)
    wKn2.goto(-250,-150)
    wR.goto(110,-150)
    wR2.goto(-310,-150)
    wP.goto(110,-90)
    wP2.goto(-310,-90)
    wP3.goto(-250,-90)
    wP4.goto(50,-90)
    wP5.goto(-10,-90)
    wP6.goto(-190,-90)
    wP7.goto(-130,-90)
    wP8.goto(-70,-90)
    bK.goto(-70,270)
    bQ.goto(-130,270)
    bB.goto(-190,270)
    bB2.goto(-10,270)
    bKn.goto(50,270)
    bKn2.goto(-250,270)
    bR.goto(110,270)
    bR2.goto(-310,270)
    bP.goto(110,210)
    bP2.goto(-310,210)
    bP3.goto(-250,210)
    bP4.goto(50,210)
    bP5.goto(-10,210)
    bP6.goto(-190,210)
    bP7.goto(-130,210)
    bP8.goto(-70,210)


screen.onkey(reset1(), "r")


    
    

