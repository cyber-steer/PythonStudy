from tkinter import *
window = Tk()

def myFun():
    print('clicked button')
b1 = Button(window,text='파이썬 버튼', command=myFun)
b1.pack()
window.mainloop()