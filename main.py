from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import randint
import PIL.Image
from PIL import ImageTk
from tkinter import messagebox

def center_window(width, height):
    global app
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))

def finish():
    global finish_game
    global var1
    global var2
    global player1_score
    global player2_score
    global lb4_2
    global finish_state

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
            if win == 3 and finish_game == False:
                finish_game = True
                lb4_2 = Label(app, bg='#252627', image=red_img5)
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
    
    if choose_game.get() == 1:
        if player1_score == 2 or player2_score == 2:
            finish_state = True
    elif choose_game.get() == 2:
        if player1_score == 3 or player2_score == 3:
            finish_state = True
    elif choose_game.get() == 3:
        if player1_score == 4 or player2_score == 4:
            finish_state = True
    elif choose_game.get() == 4:
        if player1_score == 5 or player2_score == 5:
            finish_state = True
        
    if(finish_state == True):
        messagebox.showinfo('Partida Finalizada', 'O Jogador {} ganhou a partida.'.format(player[j-1]))
        app.destroy()
        menu()

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
    global finish_state
    finish_game = False
    states = ['', '', '', '', '', '', '', '', '']
    player = ['X', 'O']
    player_play = randint(0, 1)
    player1_score = 0
    player2_score = 0
    finish_state = False
    app.title('Jogar')
    img1 = PhotoImage(file='player1.png')
    img2 = PhotoImage(file='player2.png')

    def change_player():
        global cpu_choose
        global player_play
        if finish_game == False:
            finish()
        if player_play == 0 and finish_game == False:
            player_play = 1
            fr7['bg'] = 'black'
            fr8['bg'] = 'white'
            if cpu_choose.get() == True:
                ver3 = False
                while(ver3 == False):
                    cpu = randint(0, 8)
                    if states[cpu] == '':
                        ver3 = True
                if cpu == 0:
                    action_Play1()
                if cpu == 1:
                    action_Play2()
                if cpu == 2:
                    action_Play3()
                if cpu == 3:
                    action_Play4()
                if cpu == 4:
                    action_Play5()
                if cpu == 5:
                    action_Play6()
                if cpu == 6:
                    action_Play7()
                if cpu == 7:
                    action_Play8()
                if cpu == 8:
                    action_Play9()
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

    def action(f, x, y, w, h):
        if finish_game == False:
            if player_play == 0:
                globals()[f"lb{f}"] = label(app, img1)
            elif player_play == 1:
                globals()[f"lb{f}"] = label(app, img2)
            globals()[f"lb{f}"].place(x=x, y=y, width=w, height=h)
            states[f-1] = player[player_play]
            change_player()

    d_w = 100
    d_h = 100
    def action_Play1():
        action(1, 10, 70, d_w, d_h)
    def action_Play2():
        action(2, 120, 70, d_w, d_h)
    def action_Play3():
        action(3, 230, 70, d_w, d_h)
    def action_Play4():
        action(4, 10, 180, d_w, d_h)
    def action_Play5():
        action(5, 120, 180, d_w, d_h)
    def action_Play6():
        action(6, 230, 180, d_w, d_h)
    def action_Play7():
        action(7, 10, 290, d_w, d_h)
    def action_Play8():
        action(8, 120, 290, d_w, d_h)
    def action_Play9():
        action(9, 230, 290, d_w, d_h)

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

    bt1 = button(app, action_Play1).place(x=10, y=70, width=100, height=100)
    bt2 = button(app, action_Play2).place(x=120, y=70, width=100, height=100)
    bt3 = button(app, action_Play3).place(x=230, y=70, width=100, height=100)
    bt4 = button(app, action_Play4).place(x=10, y=180, width=100, height=100)
    bt5 = button(app, action_Play5).place(x=120, y=180, width=100, height=100)
    bt6 = button(app, action_Play6).place(x=230, y=180, width=100, height=100)
    bt7 = button(app, action_Play7).place(x=10, y=290, width=100, height=100)
    bt8 = button(app, action_Play8).place(x=120, y=290, width=100, height=100)
    bt9 = button(app, action_Play9).place(x=230, y=290, width=100, height=100)
    bt9 = Button(app, command=reset, bg='#252627', image=red_img3,relief=FLAT, activebackground='#252627', bd=0).place(x=310, y=5)

    fr7 = Frame(app, bg='black')
    fr7.place(x=81, y=58, width=35, height=5)
    fr8 = Frame(app, bg='black')
    fr8.place(x=221, y=58, width=35, height=5)
    change_player()
    app.mainloop()

def menu():
    global app
    global cpu_choose
    global choose_game
    app = tk.Tk()
    center_window(340,400)
    app.title('Menu')
    app.resizable(0, 0)
    s = ttk.Style()
    s.configure('rd1.TRadiobutton', background='#2e3031', foreground='white')
    fr0_0 = Frame(app, bg='#252627').place(x=0, y=0, width=341, height=400)
    fr0_1 = Frame(app, bg='#2e3031').place(x=10, y=70, width=320, height=320)
    red_img1_1 = ImageTk.PhotoImage(PIL.Image.open('list.png').resize((20, 20)))
    red_img1_2 = ImageTk.PhotoImage(PIL.Image.open('team.png').resize((20, 20)))
    red_img1_3 = ImageTk.PhotoImage(PIL.Image.open('play.png').resize((20, 20)))
    lb0_0 = Label(app, bg='#2e3031', text='Escolha o modo de jogo:',fg='white', font="Calibri 12 bold").place(x=40, y=75)
    lb0_1 = Label(app, bg='#2e3031', image=red_img1_1).place(x=15, y=75)
    choose_game = IntVar()
    choose_game.set(0)
    cpu_choose = BooleanVar()
    cpu_choose.set(False)
    ttk.Radiobutton(app, text="Melhor de 1", variable=choose_game, value=0,style='rd1.TRadiobutton', takefocus=False).place(x=15, y=110)
    ttk.Radiobutton(app, text="Melhor de 3", variable=choose_game, value=1,style='rd1.TRadiobutton', takefocus=False).place(x=15, y=135)
    ttk.Radiobutton(app, text="Melhor de 5", variable=choose_game, value=2,style='rd1.TRadiobutton', takefocus=False).place(x=15, y=160)
    ttk.Radiobutton(app, text="Melhor de 7", variable=choose_game, value=3,style='rd1.TRadiobutton', takefocus=False).place(x=15, y=185)
    ttk.Radiobutton(app, text="Melhor de 9", variable=choose_game, value=4,style='rd1.TRadiobutton', takefocus=False).place(x=15, y=210)
    lb0_2 = Label(app, bg='#2e3031', text='Escolha o adversário:', fg='white', font="Calibri 12 bold").place(x=40, y=245)
    lb0_3 = Label(app, bg='#2e3031', image=red_img1_2).place(x=15, y=245)
    lb0_4 = Label(app, bg='#252627', text='Jogo da Velha Desenvolvido por: Lucasbxd',fg='white', font="Calibri 12 bold").place(x=20, y=25)
    ttk.Radiobutton(app, text="Player vs Player", variable=cpu_choose, value=False,style='rd1.TRadiobutton', takefocus=False).place(x=15, y=285)
    ttk.Radiobutton(app, text="Player vs CPU", variable=cpu_choose, value=True,style='rd1.TRadiobutton', takefocus=False).place(x=15, y=310)
    bt0_0 = Button(app, bg='#252627', compound=LEFT, image=red_img1_3, text=" Jogar",command=play, fg='white').place(x=120, y=350, width=100, height=30)
    app.mainloop()
menu()