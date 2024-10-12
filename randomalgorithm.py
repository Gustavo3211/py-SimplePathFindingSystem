import numpy as np
import time 
import os
import random
import threading as th
#o 1 é o Robô
#O @ é a Saída



#INSIRA A COORDENADA DO PLAYER
#x: 0 Y: 0 É O CANTO SUPERIOR ESQUERDO
posicaoXInicio = 4
posicaoYInicio = 5

#Posicao Real time


Mapa =[ [".",".",".",".",".","."],
        [".",".","█",".",".","."],
        [".",".","█",".",".","."],
        [".",".","█","█","█","."],
        [".",".",".",".",".","."],
        [".",".",".",".",".","."]]

#Insira a coodenada da saída
#5 5 É O CANTO INFERIOR DIREITO
posicaoXFinal =  3
posicaoYFinal =  2


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



# path finding de verdade
def pathfinding():
    global posicaoX, posicaoY, posicaoXFinal, posicaoYFinal
    
    # Distância do node Principal para o final
    hx = abs(posicaoXFinal - posicaoX)
    hy = abs(posicaoYFinal - posicaoY)
    h = hx + hy

    '''
    Esse algoritmo usa como base o A* porém não com todas as funcionalidades
    pois não temos o valor de G.
    
    O valor que usamos é a soma da distância do node vizinho com o player até o final do labirinto.
    e.g:

    F = DISTANCIA_ATÉ_FINAL + NODE_DISTANCIA_ATÉ_FINAL

    O código então, escolhe o node com menor F pois a distância até o final teoricamente iria levar até o final do labirinto pela menor distância possível.
    
    Algumas regras extras foram adicionadas para melhorar como o algoritmo funciona:
            
            °- Paredes ou borda do mapa ou qualquer coisa que não seja "." setam o F = 99999999 assim o código considera esse NODE um obstáculo.

            °- O caminho passado pelo player, no caso o rastro "0", é considerado 9999999 assim evitando que o algoritmo considere um lugar que ele já passou
            
            °- Se o Player ficar preso, o código retorna o "NÃO ACHEI" como direção, o que irá reiniciar o código e colocar um X na posição que ele travou, de modo que ele vai lentamente desconsiderar locais sem saída.

               e.g:
                    Mapa:
                        ['0' 'X' 'X' '█' 'X' 'X']
                        ['0' '0' 'X' 'X' 'X' 'X']
                        ['█' '0' '█' '█' '█' 'X']
                        ['X' '0' '█' '@' '█' 'X']
                        ['█' '0' '█' '1' '█' 'X']
                        ['.' '0' '0' '0' '█' 'X']

            °- Como não podemos andar na diagonal, temos que verificar se o Node PAI é atravessavel, assim podemos ir para o Node FILHO
                
                MAPA DE NODES:
                    FILHO    PAI   FILHO
                    [NODE1][NODE2][NODE3]
                PAI [NODE4][     ][NODE5]PAI
                    [NODE6][NODE7][NODE8]
                    FILHO    PAI   FILHO

    '''

    # Adicionamos as coordenadas dos nodes ortogonais:
    NODE1 = [posicaoX - 1, posicaoY - 1,0,1]
    NODE2 = [posicaoX    , posicaoY - 1,0,None]
    NODE3 = [posicaoX + 1, posicaoY - 1,0,1]

    
    NODE4 = [posicaoX - 1, posicaoY,0,None]
    NODE5 = [posicaoX + 1, posicaoY,0,None]

    NODE6 = [posicaoX - 1, posicaoY + 1,0,6]
    NODE7 = [posicaoX    , posicaoY + 1,0,None]
    NODE8 = [posicaoX + 1, posicaoY + 1,0,6]

    NODES = [NODE1,NODE2,NODE3,NODE4,NODE5,NODE6,NODE7,NODE8]

    # Agora descobrimos o valor de f para cada node vizinho do player
    for i, NODE in enumerate(NODES):
        try:
            if 0 <= NODE[1] < len(Mapa) and 0 <= NODE[0] < len(Mapa[0]):
                if Mapa[NODE[1]][NODE[0]] == "." or Mapa[NODE[1]][NODE[0]] == "@":  # Caminho livre

                    NODEhx = abs(posicaoXFinal - NODE[0])
                    NODEhy = abs(posicaoYFinal - NODE[1])
                    NODEh = NODEhx + NODEhy
                    f = h + NODEh
                    NODE[2] = f
                    
                else: 
                    NODE[2] = 999999999999  # Obstáculo
            else:  
                NODE[2] = 999999999999  # Fora dos limites do mapa
        
        except IndexError:  # Caso seja fora dos limites do mapa
            NODE[2] = 999999999999

        print("Node ", i + 1, " :", NODE)
    
    # Encontrar o node com menor valor de f
    MENOR = None
    for i, NODE in enumerate(NODES):

        #VERIFICA SE O NODE PAI É ATRAVESSAVEL SE NÃO, O NODE FILHO NÃO É ATRAVESSAVEL TAMBÉM
        if NODE[3] is not None:
            node_pai = NODES[NODE[3]]
            if node_pai[2] == 999999999999:
                NODE[2] = 999999999999

        #se todos os nodes não são atrvessaveis retorne None
        if all(node[2] == 999999999999 for node in NODES):
            direcaoNUM = None
        
        #acha o menor F
        if MENOR is None or NODE[2] < MENOR[2]:
            MENOR = NODE
            direcaoNUM = i + 1


    direcao = {
        # Travei!
        0: "NaoAchei",  
        None : "NaoAchei"
    }

    print("Node menor:", MENOR)
    direcao[1] = "W,A"
    direcao[2] = "W"
    direcao[3] = "W,D"
    direcao[4] = "A"
    direcao[5] = "D"
    direcao[6] = "S,A"
    direcao[7] = "S"
    direcao[8] = "S,D"

    # Caso DirecaoNum retornar vazio (significando que não existe nenhum caminho naquele node a gente retorna o "Nao achei")
    try:
        return direcao[direcaoNUM]
    except UnboundLocalError:        
        return direcao[0]

PARAR = 0 
def preso():
    global PARAR
    
    ultima_posX = posicaoX
    ultima_posY = posicaoY

    time.sleep(0.5)
    if update == True:
        if ultima_posX == posicaoX:
            if ultima_posY == posicaoY:
                print("Não existe Saída ou algo deu errado!")
                PARAR = 1
                return 1
            



def jogar():
    
    
    global tempo, passos, update
    update = True
    global posicaoX, posicaoY
    while update:
        os.system('cls' if os.name == 'nt' else 'clear')  
        
        print("Mapa:")
        print(np.matrix(Mapa))  
        direcao = pathfinding()
        
        
        print("X:", posicaoX)
        print("Y:", posicaoY)    
        print("Direcao: ", direcao)
        print("Tempo: ", tempo, "Segundos")
        print("Passos (teclas apertadas): ", passos)
        
        

        if PARAR == 1:
            break
        
        time.sleep(0.1)
        tempo += 0.1
        Historico.append(direcao)
        posicaoX, posicaoY, update = andar(direcao, posicaoX, posicaoY)  
        
        
        passos += 1


update = False
if update == False:
    
    jogar()
    th.Thread(target=preso).start()
    
    print("Tempo: ", tempo)
    print("Caminho usado:")
    print(Historico)


