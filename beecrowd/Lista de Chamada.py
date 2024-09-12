sala, sorteio = input().split()
alunos = []
for x in range(int(sala)):
    alunos.append(input())

for i in range(len(alunos)):
        minimo = i
        for j in range(i+1, len(alunos)):
            if alunos[j] <= alunos[minimo]:
                minimo = j
        temp = alunos[i]
        alunos[i] = alunos[minimo]
        alunos[minimo] = temp

print(alunos[int(sorteio)-1])