def achar_maior(lista, maior, indice):
    if indice == len(lista):
        return maior
    else:
        if lista[indice] > maior:
            return achar_maior(lista, lista[indice], indice + 1)
        else:
            return achar_maior(lista, maior, indice + 1)
entrada = list(map(int, input().split()))
print(achar_maior(entrada, entrada[0], 0))