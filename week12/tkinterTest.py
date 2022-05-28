from tkinter import *
window = Tk()
window.title('윈도우 창 연습')
window.geometry("400x400+100+0") #
window.resizable(True, False) #
label1 = Label(window, text='파이썬을')
label2 = Label(window, text='열심히', font=('함초롬바탕', 30), fg='#6799FF')
label3 = Label(window, text='공부 중 입니다', font=('맑은고딕', 15), bg='#FFD9EC',width=100, height=2, anchor=SE)
label1.pack()
label2.pack()
label3.pack()
window.mainloop()