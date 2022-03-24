import random
import turtle
import turtle as t

t.shape('turtle')
t.pensize(10)
t.shapesize(3)
t.setup(800,800)

while True:
    distance = random.randrange(50,300)
    angle = random.randrange(0,180)
    r = random.random()
    g = random.random()
    b = random.random()

    curX = t.xcor()
    curY = t.ycor()

    t.left(angle)
    t.pencolor((r,g,b))
    t.forward(distance)
    if (curX >400 or curX < -400) or (curY>400 or curY<-400) :
        t.up()
        t.goto(0,0)
        t.down()
t.done()