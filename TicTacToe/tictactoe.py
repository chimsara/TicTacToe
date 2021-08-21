from tkinter import*
import tkinter.messagebox

window = Tk()
window.title("Tic-Tac-Toe")
window.resizable(width=False,height=False)

click= True
count=0

b1 = StringVar()
b2 = StringVar()
b3 = StringVar()
b4 = StringVar()
b5 = StringVar()
b6 = StringVar()
b7 = StringVar()
b8 = StringVar()
b9 = StringVar()

x_photo = PhotoImage(file='star.png')
o_photo = PhotoImage(file='love.png')

def play():
    button1 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b1, command=lambda:press(1,0,0))
    button1.grid(row=0,column=0)

    button2 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b2, command=lambda:press(2,0,1))
    button2.grid(row=0,column=1)

    button3 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b3, command=lambda:press(3,0,2))
    button3.grid(row=0,column=2)

    button4 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b4, command=lambda:press(4,1,0))
    button4.grid(row=1,column=0)

    button5 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b5, command=lambda:press(5,1,1))
    button5.grid(row=1,column=1)

    button6 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b6, command=lambda:press(6,1,2))
    button6.grid(row=1,column=2)

    button7 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b7, command=lambda:press(7,2,0))
    button7.grid(row=2,column=0)

    button8 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b8, command=lambda:press(8,2,1))
    button8.grid(row=2,column=1)

    button9 = Button(window,height=9,width=19,
    relief='solid',borderwidth=1,background ='#fff0f0', textvariable= b9, command=lambda:press(9,2,2))
    button9.grid(row=2,column=2)

    

def press(num,r,c):
    global count,click

    if click == True:
        label_photo = Label(window, image=x_photo)
        label_photo.grid(row=r,column=c)
        click = False
    else:
        label_photo = Label(window, image=o_photo)
        label_photo.grid(row=r,column=c)
        click = True
    
#def clear():
    

#def check_winner():
    









window.mainloop()
