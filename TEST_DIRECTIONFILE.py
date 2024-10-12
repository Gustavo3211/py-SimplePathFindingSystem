import numpy as np
import time 
import os
import random
#o 1 é o Robô
#O @ é a Saída

#esse aqui é só pra testar o codigo
def list_to_str(lista):
    string = ','.join(lista)
    return string

direcao = list_to_str(['S,D', 'S', 'S', 'S', 'S,D', 'D', 'W', 'W'])

#INSIRA A COORDENADA DO PLAYER
#x: 0 Y: 0 É O CANTO SUPERIOR ESQUERDO
posicaoXInicio = 0
posicaoYInicio = 0

#Posicao Real time


Mapa =[ [".",".",".","█",".","."],
        [".",".",".",".",".","."],
        ["█",".","█","█","█","."],
        [".",".","█",".","█","."],
        ["█",".","█",".","█","."],
        [".",".",".",".","█","."]]

#Insira a coodenada da saída
#5 5 É O CANTO INFERIOR DIREITO
posicaoXFinal = 3
posicaoYFinal = 3


Historico = []

def adicionarPlayer():
    posicaoX = posicaoXInicio
    posicaoY = posicaoYInicio

    Mapa[posicaoY][posicaoX]= 1
    Mapa[posicaoYFinal][posicaoXFinal]= "@"


    return posicaoX, posicaoY


posicaoX, posicaoY = adicionarPlayer()


'''
Mapa =[ ["█","█","█","█","█","█"],
        [".",".",".",".",".","█"],
        ["█",".","█",".","█","█"],
        [".",".","█",".",".","."],
        ["█","█","█",".","█","."],
        [".",".",".",".","█","."]]
'''

'''
Mapa = [[".",".",".",".",".","."],
        ["█","█","█","█","█","."],
        [".",".",".",".",".","."],
        [".","█",".","█","█","█"],
        [".","█",".",".",".","█"],
        [".","█",".","█",".","."]]
        
'''
'''
Mapa = [[".",".",".",".",".","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."]]
'''

'''
Mapa = [[".","█",".",".",".","."],
        [".",".",".",".",".","."],
        ["█","█",".",".","█","█"],
        [".",".",".",".",".","."],
        [".",".",".",".","█","."],
        [".",".",".",".","█","."]]
        
'''




tempo = 0
passos = 0


def andar(direcao, posicaoX, posicaoY):
    global pontoES, pontoDIR, pontoBAI, pontoCIM

    if direcao in ["NaoAchei"]:

        #apaga o caminho feito pelo player
        for y in range(len(Mapa)):
            for x in range(len(Mapa[y])):
                if Mapa[y][x] == "0":
                    Mapa[y][x] = "."
        #guarda o local aonde o player travou
        travouX = posicaoX
        travouY = posicaoY
        #faz o local intransitavel
        Mapa[travouY][travouX] = "X"
        #limpa o historico de teclas
        Historico.clear()

        #renicia o player
        posicaoX, posicaoY = adicionarPlayer()
    else:
        direcao = direcao.split(",")
        print(direcao)

        for i, direcao in enumerate(direcao):

            if direcao in ["D", "d"] and posicaoX < 5:
                if Mapa[posicaoY][posicaoX + 1] == "@": 
                    return posicaoX, posicaoY, False
                if Mapa[posicaoY][posicaoX + 1] == "." or Mapa[posicaoY][posicaoX + 1] == "0":    

                    Mapa[posicaoY][posicaoX] = "0"
                    posicaoX += 1
                    Mapa[posicaoY][posicaoX] = 1

            if direcao in ["A", "a"] and posicaoX > 0:
                if Mapa[posicaoY][posicaoX - 1] == "@":
                    return posicaoX, posicaoY, False
                if Mapa[posicaoY][posicaoX - 1] == "." or Mapa[posicaoY][posicaoX - 1] == "0":

                    Mapa[posicaoY][posicaoX] = "0"
                    posicaoX -= 1
                    Mapa[posicaoY][posicaoX] = 1

            if direcao in ["S", "s"] and posicaoY < 5:
                if Mapa[posicaoY + 1][posicaoX] == "@":
                    return posicaoX, posicaoY, False
                if Mapa[posicaoY + 1][posicaoX] == "." or Mapa[posicaoY + 1][posicaoX] == "0": 

                    Mapa[posicaoY][posicaoX] = "0"
                    posicaoY += 1
                    Mapa[posicaoY][posicaoX] = 1  

            if direcao in ["W", "w"] and posicaoY > 0:
                if Mapa[posicaoY - 1][posicaoX] == "@":
                    return posicaoX, posicaoY, False
                if Mapa[posicaoY - 1][posicaoX] == "." or Mapa[posicaoY - 1][posicaoX] == "0":

                    Mapa[posicaoY][posicaoX] = "0"
                    posicaoY -= 1
                    Mapa[posicaoY][posicaoX] = 1





    

    return posicaoX, posicaoY, True


def jogar():
    
    global tempo, passos, update
    update = True
    global posicaoX, posicaoY
    while update:
        os.system('cls' if os.name == 'nt' else 'clear')  
        Historico.append(direcao)
        posicaoX, posicaoY, update = andar(direcao, posicaoX, posicaoY)  

i = 0

update = False
if update == False:
    jogar()
    i += 1
    Mapa[posicaoY][posicaoX] = 1
    print(np.matrix(Mapa)) 
    print("O Caminho Funciona!")


