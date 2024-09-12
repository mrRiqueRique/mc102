def achar_elemento(lista, elemento, esquerda, direita):
    while esquerda <= direita:
        indice = (esquerda+direita) // 2
        if int(lista[indice]) == int(elemento):
            return indice
        elif int(lista[indice]) < int(elemento):
            return achar_elemento(lista, elemento, indice + 1, direita)
        else:
            return achar_elemento(lista, elemento, esquerda, indice - 1)
    return -1

entrada = input().split()
procurado = input()
print(achar_elemento(entrada, procurado, 0, len(entrada)-1))