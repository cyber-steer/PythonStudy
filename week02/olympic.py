import turtle as t
#거북이의 속도와 펜 사이즈 설정 모양을 거북이로
t.speed(20)
t.pensize(20)
t.shape("turtle")

#원을 그린다
t.circle(100)

#펜을 올리고 이동시켜 빨간 원을 그린다
t.up()
t.forward(240)
t.down()
t.pencolor("red")
t.circle(100)


#펜을 올리고 이동시켜 파란 원을 그린다
t.up()
t.backward(480)
t.down()
t.pencolor("blue")
t.circle(100)


#펜을 올리고 이동시켜 노란 원을 그린다
t.up()
t.right(60)
t.forward(70)
t.down()
t.pencolor("yellow")
t.circle(100)


#펜을 올리고 이동시켜 초록 원을 그린다
t.up()
t.left(60)
t.forward(240)
t.right(60)
t.down()
t.pencolor("green")
t.circle(100)

t.done()