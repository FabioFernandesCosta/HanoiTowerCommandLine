from pilha import pilha

class game:
    auxiliar, listaPilhas, nJogadas, nDiscos = None, None, None, None
     
    # inicializa as 3 pilhas de discos, e insere o numero desejado de discos na primeira pilha
    def __init__(self, numeroDiscos:int):
        self.nDiscos = numeroDiscos
        self.listaPilhas = []
        self.nJogadas = 0

        for _ in range (3):
            self.listaPilhas.append(pilha(numeroDiscos))
        
        for _ in reversed(range(numeroDiscos)):
            self.listaPilhas[0].inserir(_)


    # tenta realizar a jogada, se não for possivel, a jogada é desfeita
    def jogada(self, pilhaOrigem:int, pilhaObjetivo:int):
        # retira disco da pilha de origem
        self.auxiliar = self.listaPilhas[pilhaOrigem].remover()

        if self.auxiliar != -1:
            
            # incrementa 1 ao numero de jogadas
            self.nJogadas += 1
            foiAnulado = False
            # tenta inserir disco na pilha objetivo, se não for possivel tenta devolver o disco a pilha origem
            if not self.listaPilhas[pilhaObjetivo].inserir(self.auxiliar):
                self.listaPilhas[pilhaOrigem].inserir(self.auxiliar)
                # Remove 1 do numero de jogadas em caso de jogada invalida
                print("Jogada invalida um disco não pode ser colocado ejm cima de um disco de valor menor")
                self.nJogadas -= 1
                foiAnulado = True

            if game.condicaoVitoria():
                print("você venceu")
        return([self.nJogadas, game.condicaoVitoria(self.listaPilhas, self.nDiscos)])


    def getAllPilhas(self):
        allPilhas = []
        for _ in range(3):
            allPilhas.append(self.listaPilhas[_].pilhaArray)
        return(allPilhas)


    def condicaoVitoria(self):
        if (len(self.listaPilhas[2].pilhaArray) == self.nDiscos):
            return True
        return False