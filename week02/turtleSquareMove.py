import turtle as t

t.shape("turtle")
t.speed(20)

h=50
w=100

for i in range(4):
    if(i%2==0):
        t.forward(h)
        t.right(90)
    else:
        t.forward(w)
        t.right(90)
t.done()