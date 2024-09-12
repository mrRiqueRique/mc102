from sys import stdin
for line in stdin:
    entrada = line.strip()
    N, Q = entrada.split()
    notas = []
    for x in range(int(N)):
        notas.append(int(input()))
    for i in range(len(notas)):
        maximo = i
        for j in range(i+1, len(notas)):
            if notas[j] >= notas[maximo]:
                maximo = j
        temp = notas[i]
        notas[i] = notas[maximo]
        notas[maximo] = temp
    for y in range(int(Q)):
        print(notas[int(input())-1])
