class torre:
    pilhaArray, topo = None, None

    # inicializa
    def __init__(self, nDiscos):
        self.pilhaArray = [n * 0 for n in range(nDiscos)]
        self.topo = -1

    def inserir(self, disco: int) -> bool:
        if self.topo == -1:
            self.topo += 1
            self.pilhaArray[self.topo] = disco
            return True
        elif self.pilhaArray[self.topo] > disco:
            self.topo += 1
            self.pilhaArray[self.topo] = disco
            return True
        else:
            return False

    # remove o disco que esta no topo
    def remover(self) -> int:
        if self.topo > -1:
            discoRemovido = self.pilhaArray[self.topo]
            self.pilhaArray[self.topo] = 0
            self.topo -= 1
            return discoRemovido
        else:
            return 0

    def getTorre(self) -> list:
        return self.pilhaArray

