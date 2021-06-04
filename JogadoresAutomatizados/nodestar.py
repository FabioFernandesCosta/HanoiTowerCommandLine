from typing import Any, Union
from copy import deepcopy
from JogadoresAutomatizados.auxiliares.heuristicAStar import heuristica

class nodeStar:
    filhos, index, valor, pai,  inicial, hdx, gdx, fdx = None, None, None, None, None, None, None, None

    def __init__(self, pai, valor) -> None:
        self.pai = pai
        self.valor = valor
        self.index = 0
        self.filhos = list()



        self.hdx = heuristica.getHeurisitica(deepcopy(self.valor[2]))
        # Use g(x)=depth of the node
        self.gdx = self.getGdx(self.pai)
        #print(f"\n  {self.filhos}  {self.index}  {self.valor}  {self.pai}  {self.hdx}  {self.gdx}  {self.fdx} \n")
        #f(x)= g(x) + h(x)
        self.fdx = self.gdx + self.hdx
        pass



    def pegarPai(self):
        return self.pai

    def inserirFilho(self, filho):
        
        self.filhos.append(filho)
        

    def inserirFilhos(self, filhos: list):
        self.filhos = list(set(Union(self.filhos, filhos)))

    def quantidadeDeFilhos(self) -> int:
        return len(self.filhos)

    def pegarValor(self, index: int):
        index -= 1
        return deepcopy(self.valor[index])

    def pegarFilhos(self):
        return self.filhos

    def reiniciarNos(self):
        self.index = 0

    def removerFilho(self, deserdado):
        self.filhos.remove(deserdado)

    
    def getFdx(self):
        return self.fdx

    @staticmethod
    def getGdx(pai):
        gdx = 0
        searchPai = pai
        while searchPai != None:
            gdx += 1
            searchPai = searchPai.pegarPai()
        return gdx


