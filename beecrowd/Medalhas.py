lugar = []
ouro = []
prata = []
bronze = []

def trocar(lista, index1, index2):
    temp = lista[index1]
    lista[index1] = lista[index2]
    lista[index2] = temp
    return lista

def ordenar(l, o, p, b):
    for i in range(len(l)):
        minimo = i
        for j in range(i+1, len(l)):
            if o[j] > o[minimo]:
                minimo = j
            elif o[j] == o[minimo] and p[j] > p[minimo]:
                minimo = j
            elif o[j] == o[minimo] and p[j] == p[minimo] and b[j] > b[minimo]:
                minimo = j
            elif o[j] == o[minimo] and p[j] == p[minimo] and b[j] == b[minimo] and l[j] < l[minimo]:
                minimo = j
        o = trocar(o, i, minimo)
        p = trocar(p, i, minimo)
        b = trocar(b, i, minimo)
        l = trocar(l, i, minimo)
    return l, o, p, b

for x in range(int(input())):
    l, o, p, b = input().split()
    lugar.append(l)
    ouro.append(int(o))
    prata.append(int(p))
    bronze.append(int(b))

lugar, ouro, prata, bronze = ordenar(lugar, ouro, prata, bronze)
for i in range(len(lugar)):
    print(lugar[i], ouro[i], prata[i], bronze[i])