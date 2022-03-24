from turtle import *
pensize(5)
color('red', 'yellow')
begin_fill()
while True:
    forward(500)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()