import random
import turtle as t

#사용할 색깔을 list로 저장
col = ['red', 'yellow', 'green', 'blue', 'white', 'black', 'orange', 'pink']

#우클릭 함수
def screenLeftClick(x,y):
    #거북이 크기를 랜덤으로 설정
    tSize = random.randrange(2,10)
    t.shapesize(tSize)

    #색깔을 랜덤으로 설정
    r = random.random()
    g = random.random()
    b = random.random()
    t.color((r,g,b))

    #거북이가 바라보는 방향을 랜덤으로 설정
    tAngle = random.randrange(0, 360)

    #펜을 올리고 마우스 위치로 이동한뒤 도장을 찍는다
    t.penup()
    t.goto(x,y)
    t.left(tAngle)
    t.stamp()

#거북이 모양으로 설정
t.shape('turtle')

#화면을 좌클릭했을시 screenLeftCLick함수 실행
t.onscreenclick(screenLeftClick, 1)

t.done()
