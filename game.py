from torre import torre

class game:
    auxiliar, torres, nJogadas, nDiscos, objetivo = None, None, None, None, None
     
    # inicializa as 3 pilhas de discos, e insere o numero desejado de discos na primeira torre
    def __init__(self, numeroDiscos:int):
        self.nDiscos = numeroDiscos
        self.torres = []
        self.nJogadas = 0
        self.objetivo = [n+1 for n in reversed(range(numeroDiscos))]

        for _ in range (3):
            self.torres.append(torre(numeroDiscos))
        
        for disco in reversed(range(numeroDiscos)):
            self.torres[0].inserir(disco+1)

    def condicaoVitoria(self) -> bool:
        if self.getTorres()[2] == self.objetivo:
            return True
        return False

    def avaliarMovimento(self, pilhaOrigem: int, pilhaObjetivo: int) -> bool:
        if (pilhaOrigem > 0) and (pilhaObjetivo > 0) and (pilhaObjetivo <= 3) and (pilhaOrigem <= 3):
            return True
        else:
            return False

    # tenta realizar a jogada, se não for possivel, a jogada é desfeita
    def jogada(self, pilhaOrigem:int, pilhaObjetivo:int) -> bool:
        # Avalia o movimento 
        if self.avaliarMovimento(pilhaOrigem,pilhaObjetivo):
            pilhaObjetivo -= 1
            pilhaOrigem -= 1
            #Remove o valor da torre de origem
            self.auxiliar = self.torres[pilhaOrigem].remover()
            
            if self.auxiliar != 0:
                # incrementa 1 ao numero de jogadas
                self.nJogadas += 1
                # tenta inserir disco na torre objetivo, se não for possivel tenta devolver o disco a torre origem
                if not self.torres[pilhaObjetivo].inserir(self.auxiliar):
                    self.nJogadas -= 1
                    self.torres[pilhaOrigem].inserir(self.auxiliar)
                    print("Você tentou mover um disco maior para cima de um disco menor")
                if self.condicaoVitoria():
                    print("Vencedor")
                    return True
            else:
                print("Você tentou mover um disco que não existe")
        else:
            print("Você tentou manipular torres inexistentes") 
        
        return False
    
    def getTorres(self):
        return [n.getTorre() for n in self.torres]
