import random
import  turtle as t

def screenLeftClick(x,y):
    circleSize = random.randrange(10,100)
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(circleSize)

def screenRightClcik(x,y):
    squareSize = random.randrange(10,100)
    t.up()
    t.goto(x,y)
    t.down()
    for i in range(4):
        t.forward(squareSize)
        t.left(90)
t.shape('circle')
t.speed(10)
t.pensize(5)
t.onscreenclick(screenLeftClick, 1)
t.onscreenclick(screenRightClcik, 3)

t.done()