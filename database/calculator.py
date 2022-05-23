from tkinter import *
import tkinter
class myCalculator(object):
    def __init__(self, win):
        self.inp_lable_one = Label(win,text="Enter number One : ")
        self.inp_lable_one.place(x=50, y=20)
        self.inp_lable_one = Label(win,text="Enter number Two : ")
        self.inp_lable_one.place(x=50, y=70)
        self.inp_one = Entry()
        self.inp_one.place(x=200, y=20)
        self.inp_two = Entry()
        self.inp_two.place(x=200, y=80)


window = tkinter.Tk()
clsObj = myCalculator(window)
window.title("My Calculator")
window.geometry("500x500")
window.mainloop()
        
        