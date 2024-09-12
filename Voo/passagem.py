3# RA 281783

class Data:
    def __init__(self, mes, dia, ano):
        self._dia = int(dia)
        self._mes = int(mes)
        self._ano = int(ano)
    

    @property
    def dia(self):
        return self._dia

    @property
    def mes(self):
        return self._mes
    
    @property
    def ano(self):
        return self._ano

    @mes.setter
    def mes(self, mes):
        if mes < 0 or mes > 12:
            raise ValueError("data inválida...")
        self._mes = mes
    
    @dia.setter
    def dia(self, dia):
        ossinhos = [1, -2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
        if dia < 0 or dia > 30 + ossinhos[self.mes]:
            raise ValueError("data inválida...")
        self._dia = dia

    @ano.setter
    def ano(self, ano):
        if ano > 2022 or ano < 2021:
            raise ValueError("data inválida")
        self._ano = ano

class Voo:

    def __init__(self, origem, destino, data, custo):
        self.origem = origem  
        self.destino = destino
        self.data = data   
        self.custo = float(custo)       

        @property
        def origem(self):
            return self._origem
        
        @property
        def destino(self):
            return self._destino
        
        @property
        def data(self):
            return self._data
        
        @property
        def custo(self):
            return self._custo
        
        @origem.setter
        def origem(self, origem):
            if type(origem) != str:
                raise TypeError("código de aeroporto inválido")
            self._origem = origem

        @destino.setter
        def destino(self, destino):
            if type(destino) != str:
                raise TypeError("código de aeroporto inválido")
            self._destino = destino

        @data.setter
        def data(self, data):
            self._data = data

        @custo.setter
        def custo(self, custo):
            if type(custo) != int or float:
                raise TypeError("valor inválido")
            self._custo = custo

    def alterar(self, novo_custo):
        self.custo = novo_custo

def ajeitar_data(data):
    ossinhos = [1, -2, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    dias = 0
    dias += data.dia
    if data.mes > 1:
        for x in range(data.mes):
            dias += 30 + ossinhos[data.mes - 1]
    return dias

def comparar_datas(data1, data2):
    dias1 = ajeitar_data(data1)
    dias2 = ajeitar_data(data2)
    if data2.ano > data1.ano:
        dias2 += (data2.ano - data1.ano) * 365
    return dias2 - dias1

def achar_melhor(lista, origem, ida, volta):
    possiveis_idas = {}
    melhor_ida = float('inf')
    melhor_volta = float('inf')

    for x in lista:
        if lista[x].origem == origem and comparar_datas(ida, lista[x].data) <= 4:
            possiveis_idas[x] = []
            for y in lista:
                if lista[y].destino == origem and comparar_datas(lista[y].data, volta) <= 4:
                    possiveis_idas[x].append(y)

    for i in possiveis_idas:
        melhor_ida = min(melhor_ida, float(lista[i].custo))
        for j in possiveis_idas[i]:
            melhor_volta = min(melhor_volta, float(lista[j].custo))

    for w in possiveis_idas:
        for u in possiveis_idas[w]:
            if melhor_ida == float(lista[w].custo) and melhor_volta == float(lista[u].custo):
                return w, u

voos = {}
operacao = input()

while True:
    if operacao == "registrar":
        n = input()
        orig, dest = input().split()
        d, m, a = input().split("/")
        c = input()
        voos[n] = Voo(orig, dest, Data(m, d, a), c)
        
    elif operacao == "alterar":
        n, c = input().split()
        print(f"{n} valor alterado de {voos[n].custo} para {c}")
        voos[n].alterar(c)

    elif operacao == "cancelar":
        del voos[input()]

    elif operacao == "planejar":
        origem = input()
        ida, volta = input().split()
        d, m, a = ida.split("/")
        ida = Data(m, d, a)
        d, m, a = volta.split("/")
        volta = Data(m, d, a)
        boa1, boa2 = achar_melhor(voos, origem, ida, volta)
        print(boa1)
        print(boa2)
        break

    operacao = input()