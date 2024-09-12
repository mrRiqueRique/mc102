from math import pi, cos, sin
import math as m

def andar(passos, matriz, f_pos, angulo):
    if passos == 0:
        return matriz
    else:
        if matriz[f_pos[0]][f_pos[1]] == ".":
            matriz[f_pos[0]][f_pos[1]] = "#"
            angulo += m.pi/2
            direcao = [round(m.sin(angulo)), round(m.cos(angulo))]
            return andar(passos - 1, matriz, [f_pos[0] + direcao[0], f_pos[1] + direcao[1]], angulo)
        else:
            matriz[f_pos[0]][f_pos[1]] = "."
            angulo -= m.pi/2
            direcao = [round(m.sin(angulo)), round(m.cos(angulo))]
            return andar(passos - 1, matriz, [f_pos[0] + direcao[0], f_pos[1] + direcao[1]], angulo)
        
passos, i, j = map(int, input().split())
matriz = andar(passos, [[y for y in input()] for x in range(i)], [(i//2), (j//2)], m.pi/2)
for z in matriz:
    print(" ".join(map(str, z)))