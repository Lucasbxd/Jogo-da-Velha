from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import randint
import PIL.Image
from PIL import ImageTk


def finish():
    global finish_game
    global var1
    global var2
    global player1_score
    global player2_score
    global lb4_2

    win_condition = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    ver2 = 0
    while(ver2 < 8):
        j = 0
        while(j < 2):
            i, win = 0, 0
            while(i < 3):
                if states[win_condition[ver2][i]] == player[j]:
                    win += 1
                i += 1
            if win == 3:
                finish_game = True
                lb4_2 = Label(app, bg='#252627',image=red_img5)
                if(player[j] == 'X'):
                    player1_score += 1
                    var1.set(player1_score)
                    lb4_2.place(x=45, y=20)
                else:
                    player2_score += 1
                    var2.set(player2_score)
                    lb4_2.place(x=260, y=20)

                pass
            j += 1
        ver2 += 1

    if(finish_game == False):
        ver = 0
        for state in states:
            if state != '':
                ver = ver + 1
            if ver == 9:
                finish_game = True


def play():
    global app
    global states
    global finish_game
    global player
    global player_play
    global choose_field
    global var1
    global var2
    global player1_score
    global player2_score
    global red_img5
    global lb4_2
    finish_game = False
    states = ['', '', '', '', '', '', '', '', '']
    player = ['X', 'O']
    player_play = randint(0, 1)
    player1_score = 0
    player2_score = 0
    app = tk.Tk()
    app.geometry('339x400')
    app.title('Jogo da velha: Lucasbxd')
    app.resizable(0, 0)

    img1 = PhotoImage(file='player1.png')
    img2 = PhotoImage(file='player2.png')

    def change_player():
        global player_play
        if finish_game == False:
            finish()
        if player_play == 0 and finish_game == False:
            player_play = 1
            fr7['bg'] = 'black'
            fr8['bg'] = 'white'
        elif player_play == 1 and finish_game == False:
            player_play = 0
            fr7['bg'] = 'white'
            fr8['bg'] = 'black'

    def reset():
        global states
        global finish_game
        global lb4_2
        try:
            lb4_2.destroy()
        except Exception:
            isrunning = 0
        for x in range(1, 10):
            try:
                globals()[f"lb{x}"].destroy()
            except Exception:
                isrunning = 0
            states = ['', '', '', '', '', '', '', '', '']
            finish_game = False
            change_player()

    class label(Label):
        def __init__(self, parent, img):
            super().__init__()
            self['image'] = img
            self['bg'] = '#2e3031'

    class button(Button):
        def __init__(self, parent, command):
            super().__init__()
            self['bg'] = '#2e3031'
            self['bd'] = 0
            self['relief'] = FLAT
            self['activebackground'] = '#2e3031'
            self['command'] = command

    class frame(Frame):
        def __init__(self, parent):
            super().__init__()
            self['bg'] = 'White'

    def action1():
        global lb1
        if finish_game == False:
            if player_play == 0:
                lb1 = label(app, img1)
            elif player_play == 1:
                lb1 = label(app, img2)
            lb1.place(x=10, y=70, width=100, height=100)
            states[0] = player[player_play]
            change_player()

    def action2():
        global lb2
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb2 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb2 = label(app, img2)
            lb2.place(x=120, y=70, width=100, height=100)
            states[1] = player[player_play]
            change_player()

    def action3():
        global lb3
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb3 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb3 = label(app, img2)
            lb3.place(x=230, y=70, width=100, height=100)
            states[2] = player[player_play]
            change_player()

    def action4():
        global lb4
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb4 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb4 = label(app, img2)
            lb4.place(x=10, y=180, width=100, height=100)
            states[3] = player[player_play]
            change_player()

    def action5():
        global lb5
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb5 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb5 = label(app, img2)
            lb5.place(x=120, y=180, width=100, height=100)
            states[4] = player[player_play]
            change_player()

    def action6():
        global lb6
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb6 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb6 = label(app, img2)
            lb6.place(x=230, y=180, width=100, height=100)
            states[5] = player[player_play]
            change_player()

    def action7():
        global lb7
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb7 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb7 = label(app, img2)
            lb7.place(x=10, y=290, width=100, height=100)
            states[6] = player[player_play]
            change_player()

    def action8():
        global lb8
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb8 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb8 = label(app, img2)
            lb8.place(x=120, y=290, width=100, height=100)
            states[7] = player[player_play]
            change_player()

    def action9():
        global lb9
        if finish_game == False:
            if player_play == 0 and finish_game == False:
                lb9 = label(app, img1)
            elif player_play == 1 and finish_game == False:
                lb9 = label(app, img2)
            lb9.place(x=230, y=290, width=100, height=100)
            states[8] = player[player_play]
            change_player()

    red_img1 = ImageTk.PhotoImage(PIL.Image.open('player1.png').resize((33, 36)))
    red_img2 = ImageTk.PhotoImage(PIL.Image.open('player2.png').resize((33, 32)))
    red_img3 = ImageTk.PhotoImage(PIL.Image.open('replay.png').resize((20, 20)))
    red_img4 = ImageTk.PhotoImage(PIL.Image.open('win_off.png').resize((30, 30)))
    red_img5 = ImageTk.PhotoImage(PIL.Image.open('win_on.png').resize((30, 30)))

    var1 = IntVar()
    var1.set(player1_score)

    var2 = IntVar()
    var2.set(player2_score)

    fr1 = Frame(app, bg='#252627').place(x=0, y=0, width=339, height=400)
    fr2 = frame(app).place(x=110, y=70, width=10, height=320)
    fr3 = frame(app).place(x=220, y=70, width=10, height=320)
    fr4 = frame(app).place(x=9, y=170, width=320, height=10)
    fr5 = frame(app).place(x=9, y=280, width=320, height=10)
    fr6 = Frame(app, bg='#252627').place(x=0, y=0, width=339, height=60)

    lb1_1 = Label(app, textvariable=var1, bg='#252627', fg='white',font="Calibri 25 bold").place(x=120, y=20, width=30, height=30)
    lb2_1 = Label(app, textvariable=var2, bg='#252627', fg='white',font="Calibri 25 bold").place(x=190, y=20, width=30, height=30)
    lb3_1 = Label(app, text=':', bg='#252627', fg='white',font="Calibri 25 bold").place(x=155, y=20, width=30, height=30)
    lb4_1 = Label(app, bg='#252627', image=red_img4).place(x=45, y=20)
    lb5_1 = Label(app, bg='#252627', image=red_img4).place(x=260, y=20)
    lb6_1 = Label(app, bg='#252627', image=red_img1).place(x=80, y=15)
    lb7_1 = Label(app, bg='#252627', image=red_img2).place(x=220, y=16)

    bt1 = button(app, action1).place(x=10, y=70, width=100, height=100)
    bt2 = button(app, action2).place(x=120, y=70, width=100, height=100)
    bt3 = button(app, action3).place(x=230, y=70, width=100, height=100)
    bt4 = button(app, action4).place(x=10, y=180, width=100, height=100)
    bt5 = button(app, action5).place(x=120, y=180, width=100, height=100)
    bt6 = button(app, action6).place(x=230, y=180, width=100, height=100)
    bt7 = button(app, action7).place(x=10, y=290, width=100, height=100)
    bt8 = button(app, action8).place(x=120, y=290, width=100, height=100)
    bt9 = button(app, action9).place(x=230, y=290, width=100, height=100)
    bt9 = Button(app, command=reset, bg='#252627', image=red_img3,relief=FLAT, activebackground='#252627', bd=0).place(x=310, y=5)

    fr7 = Frame(app, bg='black')
    fr7.place(x=81, y=58, width=35, height=5)
    fr8 = Frame(app, bg='black')
    fr8.place(x=221, y=58, width=35, height=5)
    change_player()
    app.mainloop()
play()
