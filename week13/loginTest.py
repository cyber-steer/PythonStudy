from tkinter import * # window_entry3.py
def show() :
    print ("이름 : %s \n나이 : %s" % (e1.get(), e2.get()))
    d_frame.destroy()
    b_frame.destroy()
window = Tk()
window.geometry("400x200")
u_frame = Frame(window, height=30)
u_frame.grid(row=0)
d_frame = Frame(window)
d_frame.grid(row=1)
b_frame = Frame(window, height=10)
b_frame.grid(row=2)
Label(d_frame, text="이름", font=('함초롬바탕', 15), fg='#1F50B5').grid(row=0, column=0, padx=20)
Label(d_frame, text="나이", font=('함초롬바탕', 15), fg='#1F50B5').grid(row=1, column=0)
e1 = Entry(d_frame, font=('맑은고딕', 15), fg='#1F50B5')
e2 = Entry(d_frame, font=('맑은고딕', 15), fg='#1F50B5', show='*')
e1.grid(row=0, column=1, ipady=5, pady=5)
e2.grid(row=1, column=1, ipady=5, pady=5)
Button(b_frame, text="보이기", font=('맑은고딕', 10), command=show).grid(row=0, column=0,
padx=10, pady=14, ipadx=5, ipady=5)
Button(b_frame, text="종료", font=('맑은고딕', 10), command=quit).grid(row=0, column=1,
padx=10, pady=14, ipadx=5, ipady=5)
window.mainloop()