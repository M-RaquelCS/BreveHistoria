import pygame
def musica_tema():
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
while True: #loop infinito do jogo
    acertos = 0 #contador que será zerado toda vez que um rada acabar e outra iniciar
    erros = 0
    musica_tema()
    print("Bem vindo ao Breve História.")
    print("Bom jogo meu caro brasileiro.")
    nomeUsuario = input("Qual o seu nome? ")
    from random import sample    #importando biblioteca para criar um lista de numeros aleatorios sem repetição
    numeroPergunta = sample(range(1,25),10) #criando a lista de numeros aleatorios sempre com 10 espaços pois nosso jogo sempre tera 10 perguntas
    for i in range(len(numeroPergunta)): #lendo a lista por posição. ex: na posição 0 tem o numero 8
        num = str(numeroPergunta[i]) #salvando numa variavel o conteudo de cada posição em forma de str
        arquivoPerguntas = open("perguntas{}.txt".format(num), "r") #salvando em uma variavel a pergunta lida (pergunta essa 'escolida' depois de adicionar o numero lido na lista anterior)
        for i,elementos in enumerate(arquivoPerguntas.readlines()): #transformando o arquivo em uma lista com enumerate cada linha é um posição (i) e dentro (elementos) esta a frase
            if i != 5: #nao imprimir a posição 5 que é onde esta armazenada a resposta
                print(elementos) #fazendo com que imprimisse apenas a pergunta e as alternativas
            else:
                respostaPergunta = elementos #salvando em uma variavel o elemento da posição 5 pra poder a comparação abaixo, de se acertou ou nao
        respostaUsuario = input("Sua resposta: ")
        if respostaUsuario == "a" or respostaUsuario == "A" or respostaUsuario == "b" or respostaUsuario == "B" or respostaUsuario == "c" or respostaUsuario == "C" or respostaUsuario == "d" or respostaUsuario == "D":
            if respostaUsuario == respostaPergunta or respostaUsuario == respostaPergunta.lower():
                musica_acertou()
                acertos += 1
                print("Acertou Mizeravi.\n".title())
            elif respostaUsuario != respostaPergunta or respostaUsuario != respostaPergunta.lower():
                musica_errou()
                erros += 1
                print("Lamento.\n".title())
        else: #criando um condição para caso seja digitado uma opção invalida e pedindo novamete para digitar uma resposta valida
            print("Opção digitada inválida.")
            respostaUsuario = input("Sua resposta: ")
            if respostaUsuario == respostaPergunta or respostaUsuario == respostaPergunta.lower():
                musica_acertou()
                acertos += 1
                print("Acertou Mizeravi\n".title())
            elif respostaUsuario != respostaPergunta or respostaUsuario != respostaPergunta.lower():
                musica_errou()
                erros += 1
                print("Lamento.\n".upper())
    print("Sua quantidade de acertos foi:", acertos)
    if 9 <= acertos <= 10:
        musicawinner()
        print("Valeime, quem é Tom Hanks perto de você?")
    elif 6 <= acertos <=8:
        musicawinner2()
        print("Você até sabe história mas podia melhorar né não?")
    elif 4 <= acertos <= 5:
        musicawinner3()
        print("Amoreeeeeee, vamo assistir umas videos aulas hein?" + "\nVamo cuida vai pro Youtube, cuida anda")
    elif 0 <= acertos <= 3:
        musicawinner4()
        print("Queridx, te preserva mulher, vai estudar")
    dadosUsuario = open("dadosUsuario.txt", "a")#abrindo o arquivo no modo append para adicionar a quantidade de acertos e o nome do usuario em um linha com um espaço entre eles para conseguir fazer o ranking
    dadosUsuario.write(str(acertos)+ " " + nomeUsuario + "\n")
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
        print(*a)
    escolhaUsuario = input("Deseja jogar novamente?" +"\nDigite sim ou não: ")
    if escolhaUsuario == "sim" or escolhaUsuario == "SIM" or escolhaUsuario == "não" or escolhaUsuario == "NÃO" or escolhaUsuario == "nao" or escolhaUsuario == "NAO":
        if escolhaUsuario == "sim" or escolhaUsuario == "SIM":
            continue
        elif escolhaUsuario == "não" or escolhaUsuario == "NÃO" or escolhaUsuario == "nao" or escolhaUsuario == "NAO":
            break
    else:#criando uma condição para respostas invalidas perguntando de novo ate digitar um resposta valida
        print("Opção digitada inválida.")
        escolhaUsuario = input("Deseja jogar novamente?" +"\nDigite sim ou não: ")
        if escolhaUsuario == "sim" or escolhaUsuario == "SIM":
            continue
        elif escolhaUsuario == "não" or escolhaUsuario == "NÃO" or escolhaUsuario == "nao" or escolhaUsuario == "NAO":
            break