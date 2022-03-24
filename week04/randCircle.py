import random
import turtle as t



t.shape('turtle')
t.setup(800,800)
t.speed(50)
t.hideturtle()
t.pencolor('red')

while True:
    x = random.randrange(-600,600)
    y = random.randrange(-600,600)

    t.up()
    t.goto(x,y)
    t.down()
    t.circle(100)

    if (x >300 or x < -300) or (y>300 or y<-300) :
        if t.pencolor() == 'red':
            t.pencolor('blue')
            t.up()
            t.goto(0,0)
            t.down()
        else:
            t.pencolor('red')
            t.up()
            t.goto(0,0)
            t.down()


t.done()