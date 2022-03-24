import turtle
t = turtle.Turtle()
t.shape('turtle')
t.up()
t.goto(-100,-100)
t.down()
t.color('green')

for i in range(4):
    t.forward(100)
    t.right(90)


turtle.done()