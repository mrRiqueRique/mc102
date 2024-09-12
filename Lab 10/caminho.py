from math import cos, sin, pi
import math as m
from sys import stdin

lab = open("./labirinto.txt")

def ler_matriz():
    matriz = []
    caminho = []
    i = 0
    for line in lab:
        matriz.append([])
        for x in line:
            matriz[i].append(x)
            if x == "E":
                caminho.append((i, line.index("E")))
        i += 1
    return matriz, caminho

def posicoes(angulo, posicao, lista, matriz):
    if len(lista) == 4:
        return lista
    else:
        direcao = [round(m.sin(angulo)), round(m.cos(angulo))]
        if 0 <= posicao[0] + direcao[0] < len(matriz) and 0 <= posicao[1] + direcao[1] < len(matriz[0]):
            lista.append((posicao[0] + direcao[0], posicao[1] + direcao[1]))
        return posicoes(angulo + m.pi/2, posicao, lista, matriz)

def bob_construtor(matriz, caminho, passos):
    counter = 0
    lista = posicoes(-m.pi/2, [caminho[passos][0], caminho[passos][1]], [], matriz)
    for x in lista:
        if matriz[x[0]][x[1]] != "#" and x not in caminho:
            counter += 1

    if counter == 0:
        matriz[caminho[passos][0]][caminho[passos][1]] = "#"
        caminho.remove(caminho[passos])
        return bob_construtor(matriz, caminho, passos-1)
    
    else:
        return matriz, caminho
    
def ariadne(labirinto, fio, angulo, caminho):
    direcao = [round(m.sin(angulo)), round(m.cos(angulo))]
    if 0 <= fio[0] + direcao[0] < len(labirinto) and 0 <= fio[1] + direcao[1] < len(labirinto[0]):
        fio[0] += direcao[0]
        fio[1] += direcao[1]
    else:
        return ariadne(labirinto, fio, angulo + m.pi/2, caminho)

    if labirinto[fio[0]][fio[1]] == "S":
        caminho.append((fio[0], fio[1]))
        return labirinto, caminho
    elif labirinto[fio[0]][fio[1]] == "#" or (fio[0], fio[1]) in caminho:
        labirinto, caminho = bob_construtor(labirinto, caminho, len(caminho)-1)
        return ariadne(labirinto, [caminho[-1][0], caminho[-1][1]], angulo + m.pi/2, caminho)
    else:
        caminho.append((fio[0], fio[1]))
        return ariadne(labirinto, fio, 0, caminho)
    
labirinto, caminho = ler_matriz()


if caminho[0][1] != 7:
    labirinto, caminho = ariadne(labirinto, [caminho[0][0], caminho[0][1]], 0, caminho)
else:
    labirinto, caminho = ariadne(labirinto, [caminho[0][0], caminho[0][1]], m.pi/2, caminho)


for z in labirinto:
    print(" ".join(map(str, z)))

for i in range(len(caminho)):
    print(caminho[i][0], caminho[i][1])
