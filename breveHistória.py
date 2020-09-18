from tkinter import *
import pygame, random
from random import sample

respostaPergunta = ''  
altA = ''
altB = ''
altC = ''
altD = ''
perguntas = ''
acertos = 0

nomeUser = ''
numeroPergunta = sample(range(1,25),10) #parte para gerar a lista de perguntas aleatorias e sem repetição, salvando cada parte da questão em uma variavel
listaPergs = [i for i in sample(range(1,25),10)]

def musica_tema(): #função para tocar a música durante o jogo
    pygame.mixer.init()
    pygame.mixer.music.load("musica_tema.mp3")
    pygame.mixer.music.play()
def musica_acertou():
    pygame.mixer.init()
    pygame.mixer.music.load('musica_acertou.mp3')
    pygame.mixer.music.play()

def musica_errou():
    pygame.mixer.init()
    pygame.mixer.music.load('musica_erro.mp3')
    pygame.mixer.music.play()

def musicawinner():
    # Inicializando o mixer PyGame
    pygame.mixer.init()
    # Iniciando o Pygame
    pygame.mixer.music.load('fimjogo9q.mp3')
    pygame.mixer.music.play()

def musicawinner2():
    pygame.mixer.init()
    pygame.mixer.music.load('fimjogo8q.mp3')
    pygame.mixer.music.play()

def musicawinner3():
    pygame.mixer.init()
    pygame.mixer.music.load('fimjogo5q.mp3')
    pygame.mixer.music.play()

def musicawinner4():
    pygame.mixer.init()
    pygame.mixer.music.load('fimjogo3p.mp3')
    pygame.mixer.music.play()

janelaPrincipal = Tk() #abrir a janela TK 
janelaPrincipal.geometry("600x600+600+200")
janelaPrincipal.title("Do you know?")
janelaPrincipal.resizable(width=FALSE, height=FALSE) #linha feita para janela nao aumentar de tamanho
#janelaPrincipal["bg"] = "SlateGray1" 
musica_tema()
imagem = PhotoImage(file = "InicioF.png")
lbImagem = Label(janelaPrincipal, image = imagem) #abrindo a imagem no tamanho da janela
lbImagem.pack()

imagem2 = PhotoImage(file = "perguntas.png")
lbImagem2 = Label(janelaPrincipal, image = imagem2)
lbImagem2.pack()

def button1_click(): #função para encerrar a janela 
    exit()

bt1 = Button(janelaPrincipal, width=20, text="Encerrar jogo", command = button1_click) #criando um botão com a função
bt1.place(x=100, y=520)

lb1 = Label(janelaPrincipal, text= "Vamos Começar...",wraplength = 450,pady=20, bg = "lemon chiffon", font = "mathjax_math 30") #criação de Label
lb2 = Label(janelaPrincipal, text = "Qual o seu nome?", bg = "lemon chiffon",  font = "mathjax_math 11 ")
ed = Entry(janelaPrincipal) #abrindo caixa de texto para o usario digitar

def verificar(respUser):
    if respUser == respostaPergunta:
        global acertos
        acertos += 1
        musica_acertou()
        getPergunta()
    else:
        musica_errou()
        getPergunta()

def getPergunta():

    if len(listaPergs) == 0:
        print('acabou')
        lb3.destroy()
        A.destroy()
        B.destroy()
        C.destroy()
        D.destroy()
        ranking()

    else:
        n = random.choice(listaPergs)
        listaPergs.remove(n)

        arquivoPerguntas = open("perguntas{}.txt".format(n), "r")

        for i,elemento in enumerate(arquivoPerguntas.readlines()):
            global altA, altB, altC, altD, perguntas

            print(elemento)

            if i == 0:
                lb3['text'] = elemento
                perguntas = elemento
            elif i == 1:
                A['text'] = elemento
                altA = elemento
            elif i == 2:
                B['text'] = elemento
                altB = elemento
            elif i == 3:
                C['text'] = elemento
                altC = elemento
            elif i == 4:
                D['text'] = elemento
                altD = elemento
            else:
                #print(elemento)
                global respostaPergunta
                respostaPergunta = elemento

#criando uma label e quatro botões com dada parte da pergunta (as variaveis) como texto       
lb3 = Label(janelaPrincipal, wraplength = 535,pady=20, bg = "lemon chiffon", font = "mathjax_math")

A = Button(janelaPrincipal, width = 55, wraplength = 500, bg = "lemon chiffon", font = "mathjax_math", command =lambda: verificar('A'))
B = Button(janelaPrincipal, width = 55, wraplength = 500, bg = "lemon chiffon", font = "mathjax_math", command =lambda: verificar('B'))
C = Button(janelaPrincipal, width = 55, wraplength = 500, bg = "lemon chiffon", font = "mathjax_math", command =lambda: verificar('C'))
D = Button(janelaPrincipal, width = 55, wraplength = 500, bg = "lemon chiffon", font = "mathjax_math", command =lambda: verificar('D'))

lb4 = Label(janelaPrincipal, text = "Ranking",wraplength = 250, bg = "lemon chiffon", font = "mathjax_math 30")
bt4 = Button(janelaPrincipal, width=20, text="Encerrar jogo", command = button1_click) #criando um botão com a função

def ranking():
    lb4.place(x=200 , y=100)
    bt4.place(x=350, y=500)
    global nomeUser
    global acertos
    dadosUsuario = open("dadosUsuario.txt", "a")#abrindo o arquivo no modo append para adicionar a quantidade de acertos e o nome do usuario em um linha com um espaço entre eles para conseguir fazer o ranking
    print('Ranking: ' +nomeUser)
    
    dadosUsuario.write(str(acertos)+ " " + nomeUser + "\n")
    dadosUsuario.close()
    ranking = open("dadosUsuario.txt", "r") #abrindo o mesmo arquivo porem agora no modo read e começar o ranking
    posição = 0 
    numerosPosições = " " 
    nomesJogadores = " "
    lista = []
    for x in ranking:
        for p, a in enumerate(x):
            if a == " " :
                posição = p
        for y in range(0, posição):
            numerosPosições += x[y]
        for z in range(posição+1 , len(x)):
            nomesJogadores += x[z]
        lista.append((float(numerosPosições),nomesJogadores))
        posição = 0
        numerosPosições = " "
        nomesJogadores = " "
    novalista = sorted(lista, reverse = True) #organizando a lista com a ordem do ranking em ordem decrescente
    for a in novalista:
        lb5 = Label(janelaPrincipal, text= a ,wraplength = 250, anchor=W, justify=CENTER, bg = "lemon chiffon", font = "mathjax_math")
        lb5.place(x=200, y= 200)

    if 9 <= acertos <= 10:
        musicawinner()
    elif 6 <= acertos <=8:
        musicawinner2()
    elif 4 <= acertos <= 5:
        musicawinner3()
    elif 0 <= acertos <= 3:
        musicawinner4()

def questoes(): #função para especificar onde cada um vai ficar
    lb3.place(x=58 , y=95)
    A.place(x=58, y=235)
    B.place(x=58, y=305)
    C.place(x=58, y=375)
    D.place(x=58, y=445)

def button3_click(): #função do terceiro botão
    global nomeUser
    nomeUser = ed.get()
    print(nomeUser)
    getPergunta()
    lbImagem.destroy()
    lb1.destroy()
    lb2.destroy()
    ed.destroy()
    bt3.destroy()
    lbImagem2.pack()
    questoes()

bt3 = Button(janelaPrincipal, width = 20, text = "Avançar", command = button3_click) #criando o terceiro botão com a funçao imbutida

def button2_click(): #função de segundo botão que ira disponibilizar o terceiro botão 
    
    bt1.destroy()
    bt2.destroy()
    lb1.place(x=102.3 , y=180)
    lb2.place(x=102.3, y = 440)
    ed.place(x = 240, y = 440)
    bt3.place(x=320, y=520)
    
bt2 = Button(janelaPrincipal, width=20, text="Iniciar jogo", command = button2_click) #criando o segundo botão 
bt2.place(x=250, y=520)

janelaPrincipal.mainloop()
"""
        Label(master, text=longtext, anchor=W, justify=LEFT"""