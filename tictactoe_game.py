from tkinter import *
import random

def next_turn(row, column):
    global the_player
    #if the square's text is blank and there isnt a winner
    if buttons[row][column]['text'] == "" and winner_exist() is False:
        #if the first participant is x
        if the_player == players[0]:
            #place their symbol in that square
            buttons[row][column]['text'] = the_player
            #x_label_photo = Label(window, image=x_photo)
            #buttons[row][column]['image'] = x_label_photo
            #x_label_photo.pack()
            
            #after they play, if there isnt a winner...
            if winner_exist() is False:
                #then its the next participant's turn and change the label
                the_player = players[1]
                label.config(text=(players[1]+" turn"))
            #if there is a winner
            elif winner_exist() is True:
                label.config(text=(players[0]+" wins!!"))
            #if there is a tie
            elif winner_exist() == "Draw":
                label.config(text=("Draw!!"))
        
        #if it is o turn...
        else:
            #place their symbol in that square
            buttons[row][column]['text'] = the_player
            #after they play, if there isnt a winner...
            if winner_exist() is False:
                #then its the next participant's turn and change the label
                the_player = players[0]
                label.config(text=(players[0]+" turn"))
            #if there is a winner
            elif winner_exist() is True:
                label.config(text=(players[1]+" wins!!"))
            #if there is a tie
            elif winner_exist() == "Draw":
                label.config(text=("Draw!!"))

def winner_exist():
    #horizontal win
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#fffbf5")
            buttons[row][1].config(bg="#fffbf5")
            buttons[row][2].config(bg="#fffbf5")
            return True
    #verticle win
    for row in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#fffbf5")
            buttons[1][column].config(bg="#fffbf5")
            buttons[2][column].config(bg="#fffbf5")
            return True
    #diagonal win
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#fffbf5")
        buttons[1][1].config(bg="#fffbf5")
        buttons[2][2].config(bg="#fffbf5")
        return True
    elif buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        buttons[0][2].config(bg="#fffbf5")
        buttons[1][1].config(bg="#fffbf5")
        buttons[2][0].config(bg="#fffbf5")
        return True
    #no winners
    elif empty_spaces() is False:
        return "Draw"
    #game isn't done yet
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    
    if spaces == 0:
        return False
    else:
        return True

def reset_game():
    global the_player

    the_player = random.choice(players)
    label.config(text= the_player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#fff0f0")

#if the text == o then make label a star..? then configure label to have an image

window = Tk()
window.title("Tic-Tac-Toe")
window.configure(bg='#fff0f0')

x_photo = PhotoImage(file='star.png')
o_photo = PhotoImage(file='love.png')

#the people
players = ["x", "o"]
#whose turn it is picked randomly
the_player = random.choice(players)
#button 2D array
buttons = [[0,0,0], [0,0,0],[0,0,0]]

#the label title
label = Label(text=the_player + " turn", font=("Verdana", 24), fg="#ff9999", bg ='#fff0f0') 
label.pack(side="top")

#the reset button
reset_button = Button(text="restart", font=("Verdana", 14),relief='flat', bd=10, fg="#ff9999",bg ='#fff0f0', command=reset_game)
reset_button.pack(side="bottom")

frame = Frame(window)
frame.pack()

#build the buttons 
for row in range(3):
    for column in range(3):
        #creates a new button for each square location
        buttons[row][column] = Button(frame, text="",font=("Verdana", 24), bg='#fff0f0',relief='groove', width=5, height=2,
        #passes that square's coordinate to next_turn method
         command = lambda row=row, column=column: next_turn(row,column))
    
        #adds button to the frame
        buttons[row][column].grid(row=row,column=column)

window.mainloop()