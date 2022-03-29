import turtle as t

t.shape('turtle')
t.speed(20)

def f():
    for radius in range(1, 150):
        if radius % 6 == 0:
            t.pencolor('red')
        elif radius % 5 == 0:
            t.pencolor('orange')
        elif radius % 4 == 0:
            t.pencolor('yellow')
        elif radius % 3 == 0:
            t.pencolor('green')
        elif radius % 2 == 0:
            t.pencolor('blue')
        elif radius % 1 == 0:
            t.pencolor('navyblue')
        else:
            t.pencolor('purple')
            print(i)
        t.circle(radius)
for i in range(12):
    f()
    t.left(30)

t.done()