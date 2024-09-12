def comparar(soma, palavra, indice):
    if indice == len(palavra):
        return soma
    else:
        if palavra[indice] != palavra[len(palavra)-indice-1]:
            return comparar(soma + 1, palavra, indice + 1)
        else:
            return comparar(soma, palavra, indice + 1)

if int(input()) == comparar(0, input(), 0):
    print("sim")
else:
    print("não")
