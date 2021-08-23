from tkinter import *
from timeit import default_timer as timer
import random


window = Tk()
window.geometry('450x200')

x = 0

def game():
    global x
    if x==0:
        window.destroy()
        x=x+1
    def check_result():
        if entry.get()==words[word]:
            end=timer()
            print(end-start)
        else:
            print("wrong spelling ")
    words=['programming','coding','samosa','tea','blahblah','youtube','facebook','google']
    word=random.randint(0,(len(words)-1))
    start=timer()
    windows=Tk()
    windows.geometry('450x200')
    x2=Label(windows,text=words[word],font="times 20")
    x2.place(x=150,y=10)
    x3=Label(windows,text="let's see howfast you can type",font="times 20")
    x3.place(x=10, y=50)
    entry=Entry(windows)
    entry.place(x=150,y=90)
    b2=Button(windows,text="submit",command=check_result,width=12,bg='gray')
    b2.place(x=150,y=120)
    b3=Button(windows, text="wanna try again", command=game, width=12, bg='gray')
    b3.place(x=250,y=120)
    windows.mainloop()

x1=Label(window,text="let's start this game ...",font="times 20")
x1.place(x=10,y=50)

b1=Button(window,text="go",command=game,width=12,bg='gray')
b1.place(x=150,y=100)

window.mainloop()