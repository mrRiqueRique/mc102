boas = 0
malvadas = 0
criancas = []
for x in range(int(input())):
    carater, crianca = input().split()
    criancas.append(crianca)
    if carater == "+":
        boas += 1
    else: 
        malvadas += 1

for i in range(len(criancas)):
        minimo = i
        for j in range(i+1, len(criancas)):
            if criancas[j] <= criancas[minimo]:
                minimo = j
        temp = criancas[i]
        criancas[i] = criancas[minimo]
        criancas[minimo] = temp

for y in criancas:
    print(y)

print(f"Se comportaram: {boas} | Nao se comportaram: {malvadas}")