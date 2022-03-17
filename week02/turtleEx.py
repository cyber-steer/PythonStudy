import turtle as t

t.pensize(5);
t.speed(20)
t.shape("turtle");
t.color("blue")
t.bgcolor("gray")
t.fillcolor("red")

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.right(90)
t.end_fill();

t.right(180)
t.forward(200)
t.fillcolor("green")
t.begin_fill()
t.circle(100)
t.end_fill()


t.done()