class Car:
    color =""
    speed = 0
    model = ""
    count = 0

    def __init__(self, model, color="검정", speed=0):
        self.color = color
        self.model = model
        self.speed = speed
        Car.count += 1
    def upSpeed(self, value):
        self.speed += value
    def downSpeed(self, value):
        self.speed -=value
    def stop(self):
        self.speed = 0

myCar1 = Car('모닝','검정')
myCar2 = Car('아반떼','흰색')
myCar3 = Car('제네시스','회색')

myCar1.upSpeed(30)
print("%s의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar1.model,myCar1.color, myCar1.speed))

myCar2.upSpeed(60)
print("%s의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar2.model,myCar2.color, myCar2.speed))

myCar3.upSpeed(0)
print("%s의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar3.model,myCar3.color, myCar3.speed))

print("자동차 총 갯수 : ",Car.count)