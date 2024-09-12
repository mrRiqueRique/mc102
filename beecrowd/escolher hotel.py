class Hotel:
    def __init__(self, preco, camas):
        self._preco = preco
        self._camas = camas

    @property
    def preco(self):
        return self._preco

    @property
    def camas(self):
        return self._camas
    
    @preco.setter
    def preco(self, preco):
        self._preco = preco

    @camas.setter
    def camas(self, camas):
        self.camas = camas

    def possivel(self, pessoas, dinheiro):
        for x in self.camas:
            custo = self.preco*pessoas
            if x >= pessoas and custo <= dinheiro:
                return self, custo
        return self, float("inf")

def achar_melhor(possiveis):
    melhor = float("inf")
    for x in possiveis:
        if possiveis[x] < melhor:
            melhor = possiveis[x]
    return melhor

pessoas, dinheiro, hoteis, semanas = map(int, input().split())
hoteln = []
for x in range(hoteis):
    hoteln.append(Hotel(int(input()), list(map(int, input().split()))))

possiveis = {}
for y in hoteln:
    hotel, custo = y.possivel(pessoas, dinheiro)
    possiveis[hotel] = custo

barato = achar_melhor(possiveis)
if barato < float("inf"):
    print(barato)
else:
    print("stay home")