from tkinter import *
import cv2

def switch():
    print("hello")
    img = PhotoImage(file="tmp2.png")

    label.configure(image=img)
    label.image = img


window = Tk()
img = PhotoImage(file="tmp.png")


label = Label(window, image=img)
label.configure(background='gray')
label.pack()
Button(window, text="변경", command=switch).pack()
window.mainloop()