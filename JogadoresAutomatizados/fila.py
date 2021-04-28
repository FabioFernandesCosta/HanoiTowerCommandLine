class fila:

    fila, inicio, final, tamanhoDaFila = None * 4

    def __init__(self) -> None:
        self.fila = list()
        self.inicio = -1
        self.final = -1
        self.tamanhoDaFila = 0
    
    def inserir(self, valor):
        if self.tamanhoDaFila == 0:
            self.final += 1
            self.fila.insert(self.final)