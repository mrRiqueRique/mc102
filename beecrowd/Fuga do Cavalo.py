from math import sin, cos, sqrt
import math as m

def ajeitar_pos(posicao):
    nums = ["1", "2", "3", "4", "5", "6", "7", "8"]
    letras = ["a", "b", "c", "d", "e", "f", "g", "h"]
    n = nums.index(posicao[0])
    l = letras.index(posicao[1])
    return [n, l]

def pontos_cavalo(posicao):
    w = 0                                               # w é o ângulo que vai variar
    pontos = []

    for z in range(12):
        w += m.pi/6                                     # incrementa 30 graus em w
        if abs(m.sin(w)) == 1 or abs(m.cos(w)) == 1:    # foge dos ângulos 0, 90, 180 e 270
           continue
    
# solução inspirada pela fórmula trigonométrica dos números complexos: a ou b é o seno ou cosseno do ângulo multiplicado pela distância, no caso igual à raiz de 5

        n = posicao[0] + round(abs(sqrt(5))*m.sin(w))   # os números representam o eixo y, então usamos seno
        l = posicao[1] + round(abs(sqrt(5))*m.cos(w))   # as letras representam o eixo x, então usamos cosseno
        
        if 0 <= n <= 7 and 0 <= l <= 7:                 # foge dos pontos fora do tabuleiro
            pontos.append([n, l])
    return pontos

def reboot():
    global ans, counter
    print(f"Caso de Teste #{counter}: {ans} movimento(s).")
    counter += 1
    ans = 0
    
ans = 0
counter = 1

cpos = input()
while True:
    if cpos == "0":
        break
    cpos = ajeitar_pos(cpos)

    tabuleiro = [[0]*8 for _ in range(8)]

    ppos = []
    for x in range(8):
        ppos.append(input())
        ppos[x] = ajeitar_pos(ppos[x])
        tabuleiro[ppos[x][0]][ppos[x][1]] = 1
    
    for y in pontos_cavalo(cpos):
        if y[0]+1 > 7:
            ans += 1
        elif y[1]-1 < 0:
            if tabuleiro[y[0]+1][y[1]+1] == 0:
                ans += 1
        elif y[1]+1 > 7:
            if tabuleiro[y[0]+1][y[1]-1] == 0:
                ans += 1
        else:
            if tabuleiro[y[0]+1][y[1]-1] == 0 and tabuleiro[y[0]+1][y[1]+1] == 0:
                ans += 1
 
    reboot()
    cpos = input()