def printHello():
    print("hello")
def selfIntro():
    print("안녕! ")
    print("난 undefine이야")
def sayHello(name):
    print(f"{name} 반가워")
def sayHelloIntro(name):
    sayHello(name)
    selfIntro()
def quickSay(lst):
    for item in lst:
        sayHelloIntro(item)
def intro(name, age):
    print(f"안녕! 난 {age}세 {name}이야!")
def myFruits(*fruits): # list에 담아 전달
    for item in fruits:
        print("%5s\t좋아!" % item)
def intro2(country = 'korea'):
    print(f"{country}에서 왔어")
def myFunc(a):
    return a*a


nameList=['홍길동','아무개','무명']

printHello()
selfIntro()
sayHello("world")
sayHelloIntro("kim")
print()
quickSay(nameList)
intro("왕","루이14")
intro(age="루이14",name="왕")
print()
myFruits('사과','바나나','배','포도','복숭아','수박')
intro2()
intro2('japan')
print(myFunc(5))