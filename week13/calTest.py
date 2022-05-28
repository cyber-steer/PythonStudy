from tkinter import *
from math import *
def calculate(event) :
    label.configure(text="결과: " + str(eval(entry.get())))
    entry.delete(0, END)

window = Tk()

Label(window, text="파이썬 수식 입력 : ").pack()
entry = Entry(window)
entry.bind("<Return>", calculate)
entry.pack()

label = Label(window, text="결과 : ")
label.pack()

window.mainloop()