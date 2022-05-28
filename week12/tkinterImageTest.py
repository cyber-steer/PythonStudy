from tkinter import *
from tkinter import messagebox

def myFunc() :
    button2.configure(text='와우~')
    messagebox.showinfo("강아지 버튼", "강아지가 귀엽죠 ^^")

window = Tk()
window.title("윈도우 창 연습")

photo = PhotoImage(file="img/mokoko.png")
photo = PhotoImage(file="img/cat.png")
button1 = Button(window, image=photo, command=myFunc)

photo2 = PhotoImage(file="img/mokoko.png")
label2 = Label(window, image=photo2)

button2 = Button(window, text="종료", command=window.destroy, width=10, height=2)
button1.pack(side=LEFT)

label2.pack()
button2.pack()

window.mainloop()
