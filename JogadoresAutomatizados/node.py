from typing import Any, Union
from copy import deepcopy

class node:
    filhos, index, valor, pai = None, None, None, None

    def __init__(self, pai, valor) -> None:
        self.pai = pai
        self.valor = valor
        self.index = 0
        self.filhos = list()

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
