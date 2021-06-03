from copy import deepcopy
from typing import Counter


class heuristica:

    def __init__(self) -> None:
        pass

    def getHeur(self,torres) -> int:
        torreUm = len(torres[0]) - torres[0].count(0)
        torreDois = len(torres[0]) - torres[1].count(0)

        print("Heuristica")
        print(torres)
        print(self.calc(torreUm))
        print(self.calc(torreDois))
        print(self.dist(self,torres[2]))
        return (self.calc(torreUm) + self.calc(torreDois) + self.dist(self,torres[2]))
    
    @staticmethod
    def calc(valor):
        return ((2 ** valor) - 1)

    @staticmethod
    def dist(self, torre):
        reverso = deepcopy(list(reversed(torre)))
        valor = 0
        for x in range(len(reverso)):
            if not self.f(x,reverso):
                valor += 1

        return self.calc(valor) + valor
    
    @staticmethod
    def f(x,lista):
        if lista[x] == 0:
            return True
        elif lista[x] == x+1:
            return True
        else:
            return False

        



