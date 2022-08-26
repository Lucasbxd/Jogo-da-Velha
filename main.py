from tkinter import *
from tkinter import ttk
import tkinter as tk
from random import randint
import PIL.Image
from PIL import ImageTk
from tkinter import messagebox

vez_do_jogador = randint(0,1)
finalizar_jogo = False
finalizar_e_voltar = False
jogador_X = []
jogador_O = []
pontuacao_X = 0 
pontuacao_O = 0
condicao_de_vitoria = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]

cor_cinza_ton1 = '#2e3031'
cor_cinza_ton2 = '#252627'
cor_branco_ton1 = 'white'
cor_preto_ton1 = 'black'

def redimensionar_imagem(local, nova_largura, nova_altura):
  return ImageTk.PhotoImage(PIL.Image.open(local).resize((nova_largura, nova_altura)))

def centralizar_janela(width, height):
    global app
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    app.geometry('%dx%d+%d+%d' % (width, height, x, y))

def encerrar_jogo():
  global modo_de_jogo
  global finalizar_e_voltar
  global finalizar_jogo
  global jogador_O
  global jogador_X
  global pontuacao_O
  global pontuacao_X

  if modo_de_jogo.get() == 1:
    if pontuacao_X == 2 or pontuacao_O == 2:
      finalizar_e_voltar = True
  elif modo_de_jogo.get() == 2:
      if pontuacao_X == 3 or pontuacao_O == 3:
          finalizar_e_voltar = True
  elif modo_de_jogo.get() == 3:
      if pontuacao_X == 4 or pontuacao_O == 4:
          finalizar_e_voltar = True
  elif modo_de_jogo.get() == 4:
      if pontuacao_X == 5 or pontuacao_O == 5:
          finalizar_e_voltar = True
    
  if(finalizar_e_voltar == True):
      if(vez_do_jogador == 0):
        string_jogador = 'X'
      else:
        string_jogador = 'O'

      messagebox.showinfo('Partida Finalizada', f'O Jogador {string_jogador} ganhou a partida.')
      pontuacao_O = 0
      pontuacao_X = 0
      jogador_X = []
      jogador_O = []
      finalizar_jogo = False
      finalizar_e_voltar = False
      app.destroy()
      menu()

def finalizar_partida():
  global imagem_win_on
  global label_imagem_win_on
  global pontuacao_X
  global pontuacao_O
  global finalizar_jogo

  imagem_win_on = redimensionar_imagem('./img/win_on.png',30,30)
  label_imagem_win_on = Label(app, bg=cor_cinza_ton2, image=imagem_win_on)

  if(vez_do_jogador == 0):
    label_imagem_win_on.place(x=45, y=20)
    pontuacao_X += 1
    texto_pontuacao_x.set(pontuacao_X)
  else:
    label_imagem_win_on.place(x=260, y=20)
    pontuacao_O += 1
    texto_pontuacao_o.set(pontuacao_O)
 
  if(modo_de_jogo.get() != 0):
    encerrar_jogo()

def play():
  global imagem_win_on
  global texto_pontuacao_o
  global texto_pontuacao_x

  imagem_jogar_player1 = PhotoImage(file='./img/player1.png')
  imagem_jogar_player2 = PhotoImage(file='./img/player2.png')

  def Executar_jogada_player(indice, posicao_x, posicao_y, largura=100, altura=100):
    if(finalizar_jogo == False):
      if vez_do_jogador == 0:
        globals()[f"label_jogada{indice}"] = Label(app, bg=cor_cinza_ton1,image=imagem_jogar_player1)
        jogador_X.append(indice)
      elif vez_do_jogador == 1:
        globals()[f"label_jogada{indice}"] = Label(app, bg=cor_cinza_ton1,image=imagem_jogar_player2)
        jogador_O.append(indice)
      globals()[f"label_jogada{indice}"].place(x=posicao_x, y=posicao_y, width=largura, height=altura)
      trocar_player()

  def Executar_jogada_cpu():
    quantidade_total_de_jogadas = len(jogador_X) + len(jogador_O)
    if(quantidade_total_de_jogadas < 9 ):
      escolher_jogada = False
      while(escolher_jogada == False):
        cpu = randint(0,8)
        if((cpu not in jogador_O) and (cpu not in jogador_X)):
          escolher_jogada = True
          break

      if cpu == 0:
          Executar_jogada_player(0,10,70)
      if cpu == 1:
          Executar_jogada_player(1,120,70)
      if cpu == 2:
          Executar_jogada_player(2,230,70)
      if cpu == 3:
          Executar_jogada_player(3,10,180)
      if cpu == 4:
          Executar_jogada_player(4,120,180)
      if cpu == 5:
          Executar_jogada_player(5,230,180)
      if cpu == 6:
          Executar_jogada_player(6,10,290)
      if cpu == 7:
          Executar_jogada_player(7,120,290)
      if cpu == 8:
          Executar_jogada_player(8,230,290)
    
  def trocar_player():
    if(verificar_vitoria(jogador_O) == False and verificar_vitoria(jogador_X) == False):
      global vez_do_jogador
      if(vez_do_jogador == 0):
        vez_do_jogador = 1
        frame_layout7['bg'] = cor_preto_ton1
        frame_layout8['bg'] = cor_branco_ton1
        if(escolher_cpu.get() == True):
          Executar_jogada_cpu()
      else:
        vez_do_jogador = 0
        frame_layout7['bg'] = cor_branco_ton1
        frame_layout8['bg'] = cor_preto_ton1
    else:
      finalizar_partida()

  def verificar_vitoria(historico_de_jogadas):
    global finalizar_jogo
    for item in range(0,len(condicao_de_vitoria)):
      contador = 0
      for posicao in range(0,3):
        if(condicao_de_vitoria[item][posicao] in historico_de_jogadas):
          contador += 1
        if contador == 3:
          finalizar_jogo = True
          return True
    return False

  def resetar_jogo():
    global jogador_X
    global jogador_O
    global vez_do_jogador
    global finalizar_jogo

    for indice in range(0, 9):
        try:
          globals()[f"label_jogada{indice}"].destroy()
        except Exception:
          pass
    try:
      label_imagem_win_on.destroy()
    except:
      pass
    
    jogador_X = []
    jogador_O = []
    finalizar_jogo = False
    vez_do_jogador = randint(0,1)
    trocar_player()

  texto_pontuacao_x = IntVar()
  texto_pontuacao_x.set(pontuacao_X)

  texto_pontuacao_o = IntVar()
  texto_pontuacao_o.set(pontuacao_O)

  frame_layout1 = Frame(app, bg=cor_cinza_ton2)
  frame_layout1.place(x=0, y=0, width=339, height=400)

  frame_layout2 = Frame(app, bg=cor_branco_ton1)
  frame_layout2.place(x=110, y=70, width=10, height=320)

  frame_layout3 = Frame(app, bg=cor_branco_ton1)
  frame_layout3.place(x=220, y=70, width=10, height=320)

  frame_layout4 = Frame(app, bg=cor_branco_ton1)
  frame_layout4.place(x=9, y=170, width=320, height=10)

  frame_layout5 = Frame(app, bg=cor_branco_ton1)
  frame_layout5.place(x=9, y=280, width=320, height=10)

  frame_layout6 = Frame(app, bg=cor_cinza_ton2)
  frame_layout6.place(x=0, y=0, width=339, height=60)

  label_pontuacao_x = Label(app, textvariable=texto_pontuacao_x, bg=cor_cinza_ton2, fg=cor_branco_ton1,font=('Calibri','25','bold'))
  label_pontuacao_x.place(x=120, y=20, width=30, height=30)

  label_pontuacao_o = Label(app, textvariable=texto_pontuacao_o, bg=cor_cinza_ton2, fg=cor_branco_ton1,font=('Calibri','25','bold'))
  label_pontuacao_o.place(x=190, y=20, width=30, height=30)

  label_texto_doispontos = Label(app, text=':', bg=cor_cinza_ton2, fg=cor_branco_ton1,font=('Calibri','25','bold'))
  label_texto_doispontos.place(x=155, y=20, width=30, height=30)

  imagem_win_off = redimensionar_imagem('./img/win_off.png',30,30)
  label_imagem_win_off1 = Label(app, bg=cor_cinza_ton2, image=imagem_win_off)
  label_imagem_win_off1.place(x=45, y=20)

  label_imagem_win_off2 = Label(app, bg=cor_cinza_ton2, image=imagem_win_off)
  label_imagem_win_off2.place(x=260, y=20)

  imagem_player1 = redimensionar_imagem('./img/player1.png',33,36)
  label_imagem_player1 = Label(app, bg=cor_cinza_ton2, image=imagem_player1)
  label_imagem_player1.place(x=80, y=15)

  imagem_player2 = redimensionar_imagem('./img/player2.png',33,32)
  label_imagem_player2 = Label(app, bg=cor_cinza_ton2, image=imagem_player2)
  label_imagem_player2.place(x=220, y=16)

  button_area0 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(0,10,70))
  button_area0.place(x=10, y=70, width=100, height=100)

  button_area1 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(1,120,70))
  button_area1.place(x=120, y=70, width=100, height=100)

  button_area2 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(2,230,70))
  button_area2.place(x=230, y=70, width=100, height=100)

  button_area3 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(3,10,180))
  button_area3.place(x=10, y=180, width=100, height=100)

  button_area4 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(4,120,180))
  button_area4.place(x=120, y=180, width=100, height=100)

  button_area5 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(5,230,180))
  button_area5.place(x=230, y=180, width=100, height=100)

  button_area6 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(6,10,290))
  button_area6.place(x=10, y=290, width=100, height=100)

  button_area7 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(7,120,290))
  button_area7.place(x=120, y=290, width=100, height=100)

  button_area8 = Button(app, 
    bg=cor_cinza_ton1, 
    activebackground=cor_cinza_ton1, 
    bd=0, 
    relief=FLAT, 
    command=lambda: Executar_jogada_player(8,230,290))
  button_area8.place(x=230, y=290, width=100, height=100)

  imagem_replay = redimensionar_imagem('./img/replay.png',20,20)
  button_reset = Button(app, command=resetar_jogo, bg=cor_cinza_ton2, image=imagem_replay,relief=FLAT, activebackground=cor_cinza_ton2, bd=0)
  button_reset.place(x=310, y=5)

  frame_layout7 = Frame(app, bg=cor_preto_ton1)
  frame_layout7.place(x=81, y=58, width=35, height=5)

  frame_layout8 = Frame(app, bg=cor_preto_ton1)
  frame_layout8.place(x=221, y=58, width=35, height=5)

  trocar_player()
  app.mainloop()

def menu():
  global app
  global escolher_cpu
  global escolher_jogo
  global modo_de_jogo

  app = tk.Tk()
  app.title('Menu')
  app.resizable(0, 0)
  centralizar_janela(340,400)

  style = ttk.Style()
  style.configure('rd1.TRadiobutton', background=cor_cinza_ton1, foreground=cor_branco_ton1)

  frame_layout1 = Frame(app, bg=cor_cinza_ton2)
  frame_layout1.place(x=0, y=0, width=341, height=400)

  frame_layout2 = Frame(app, bg=cor_cinza_ton1)
  frame_layout2.place(x=10, y=70, width=320, height=320)

  label_texto_modo = Label(app, bg=cor_cinza_ton1, text='Escolha o modo de jogo:',fg=cor_branco_ton1, font=('Calibri','12','bold'))
  label_texto_modo.place(x=40, y=75)

  imagem_list = redimensionar_imagem('./img/list.png',20,20)
  label_imagem_list = Label(app, bg=cor_cinza_ton1, image=imagem_list)
  label_imagem_list.place(x=15, y=75)
  
  modo_de_jogo = IntVar()
  modo_de_jogo.set(0)

  escolher_cpu = BooleanVar()
  escolher_cpu.set(False)

  escolher_jogo_opcao1 = ttk.Radiobutton(app, 
    text="Melhor de 1", 
    variable=modo_de_jogo, 
    value=0,
    style='rd1.TRadiobutton', 
    takefocus=False)
  escolher_jogo_opcao1.place(x=15, y=110)

  escolher_jogo_opcao2 = ttk.Radiobutton(app, 
    text="Melhor de 3", 
    variable=modo_de_jogo, 
    value=1,
    style='rd1.TRadiobutton', 
    takefocus=False)
  escolher_jogo_opcao2.place(x=15, y=135)

  escolher_jogo_opcao3 = ttk.Radiobutton(app, 
    text="Melhor de 5", 
    variable=modo_de_jogo, 
    value=2,
    style='rd1.TRadiobutton', 
    takefocus=False)
  escolher_jogo_opcao3.place(x=15, y=160)

  escolher_jogo_opcao4 = ttk.Radiobutton(app, 
    text="Melhor de 7", 
    variable=modo_de_jogo, 
    value=3,
    style='rd1.TRadiobutton', 
    takefocus=False)
  escolher_jogo_opcao4.place(x=15, y=185)

  escolher_jogo_opcao5 = ttk.Radiobutton(app, 
    text="Melhor de 9", 
    variable=modo_de_jogo, 
    value=4,
    style='rd1.TRadiobutton', 
    takefocus=False)
  escolher_jogo_opcao5.place(x=15, y=210)

  label_texto_adversario = Label(app, bg=cor_cinza_ton1, text='Escolha o adversário:', fg=cor_branco_ton1, font=('Calibri','12','bold'))
  label_texto_adversario.place(x=40, y=245)

  imagem_team = redimensionar_imagem('./img/team.png',20,20)
  label_imagem_team = Label(app, bg=cor_cinza_ton1, image=imagem_team)
  label_imagem_team.place(x=15, y=245)

  label_texto_creditos = Label(app, bg=cor_cinza_ton2, text='Jogo da Velha Desenvolvido por: Lucasbxd',fg=cor_branco_ton1, font=('Calibri','12','bold'))
  label_texto_creditos.place(x=20, y=25)

  escolher_opcao_pvp = ttk.Radiobutton(app, 
    text="Player vs Player", 
    variable=escolher_cpu, 
    value=False,
    style='rd1.TRadiobutton', 
    takefocus=False)
  escolher_opcao_pvp.place(x=15, y=285)

  escolher_opcao_cpu = ttk.Radiobutton(app, 
    text="Player vs CPU", 
    variable=escolher_cpu, 
    value=True,
    style='rd1.TRadiobutton', 
    takefocus=False)
  escolher_opcao_cpu.place(x=15, y=310)

  imagem_play = redimensionar_imagem('./img/play.png',20,20)
  button_jogar = Button(app, bg=cor_cinza_ton2, compound=LEFT, image=imagem_play, text=" Jogar",command=play, fg=cor_branco_ton1)
  button_jogar.place(x=120, y=350, width=100, height=30)

  app.mainloop()
menu()