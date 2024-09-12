from sys import stdin

def contar(lista, elemento):
    vezes = 0
    for x in lista:
        if x == elemento:
            vezes += 1
    return vezes

def trocar(lista, index1, index2):
    temp = lista[index1]
    lista[index1] = lista[index2]
    lista[index2] = temp
    return lista

def ordenar(ords, reps):
    for i in range(len(reps)):
        minimo = i
        for j in range(i+1, len(reps)):
            if reps[j] < reps[minimo]:
                minimo = j
            elif reps[j] == reps[minimo] and ords[j] > ords[minimo]:
                minimo = j
        reps = trocar(reps, i, minimo)
        ords = trocar(ords, i, minimo)
    return ords, reps

def montar(entrada, ords, reps):
    dicionario = {}
    for x in entrada:
        if dicionario.get(x) == None:
            dicionario[x] = contar(entrada, x)
            reps.append(dicionario[x])
            ords.append(ord(x))
    return ords, reps

for line in stdin:
    entrada = line.strip()
    reps = []
    ords = []
    ords, reps = montar(entrada, ords, reps)
    ords, reps = ordenar(ords, reps)

    for z in range(len(reps)):
        print(ords[z], reps[z])
