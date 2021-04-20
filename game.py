from torre import torre

class game:
    auxiliar, torres, nJogadas, nDiscos = None, None, None, None
     
    # inicializa as 3 pilhas de discos, e insere o numero desejado de discos na primeira torre
    def __init__(self, numeroDiscos:int):
        self.nDiscos = numeroDiscos
        self.torres = []
        self.nJogadas = 0

        for _ in range (3):
            self.torres.append(torre(numeroDiscos))
        
        for _ in reversed(range(numeroDiscos)):
            self.torres[0].inserir(_)


    # tenta realizar a jogada, se não for possivel, a jogada é desfeita
    def jogada(self, pilhaOrigem:int, pilhaObjetivo:int):
        # retira disco da torre de origem
        self.auxiliar = self.torres[pilhaOrigem].remover()

        if self.auxiliar != -1:
            
            # incrementa 1 ao numero de jogadas
            self.nJogadas += 1
            foiAnulado = False
            # tenta inserir disco na torre objetivo, se não for possivel tenta devolver o disco a torre origem
            if not self.torres[pilhaObjetivo].inserir(self.auxiliar):
                self.torres[pilhaOrigem].inserir(self.auxiliar)
                # Remove 1 do numero de jogadas em caso de jogada invalida
                print("Jogada invalida um disco não pode ser colocado ejm cima de um disco de valor menor")
                self.nJogadas -= 1
                foiAnulado = True

            if game.condicaoVitoria():
                print("você venceu")
        return([self.nJogadas, game.condicaoVitoria(self.torres, self.nDiscos)])


    def getAllPilhas(self):
        allPilhas = []
        for _ in range(3):
            allPilhas.append(self.torres[_].pilhaArray)
        return(allPilhas)


    def condicaoVitoria(self):
        if (len(self.torres[2].pilhaArray) == self.nDiscos):
            return True
        return False