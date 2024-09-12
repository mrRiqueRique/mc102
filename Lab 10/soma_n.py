from itertools import combinations_with_replacement

ans = []
def somar(elemento, indice):
    global ans
    if indice == elemento:
        ans = sorted(ans)
        for i in ans:
            print(f"{i}={elemento}")
        print(f"{indice}={elemento}")
    else:
        numeros = []
        for x in range(1, indice+1):
            numeros.append(x)

        possiveis = combinations_with_replacement(numeros, elemento - indice + 1)

        for y in possiveis:
            soma = 0
            for z in y:
                soma += z
            if soma == elemento:
                lista = []
                for w in y:
                    lista.append(str(w))
                ans.append("+".join(lista))
        return somar(elemento, indice + 1)

num = int(input())
somar(num, 1)