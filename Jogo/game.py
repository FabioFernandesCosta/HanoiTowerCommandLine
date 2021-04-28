from typing import Sequence
from Jogo.torre import torre
from Jogo.regras import regras
from copy import deepcopy

class game:
    torres, nJogadas, nDiscos, objetivo, regras = None, None, None, None, None


    # inicializa as 3 pilhas de discos, e insere o numero desejado de discos na primeira torre
    def __init__(self, numeroDiscos: int):
        self.nDiscos = numeroDiscos
        self.torres = list()
        self.nJogadas = 0
        self.regras = regras()

        for _ in range(3):
            self.torres.append(torre(numeroDiscos))

        for disco in reversed(range(numeroDiscos)):
            self.torres[0].inserir(disco+1)
        
        self.objetivo = deepcopy(list(reversed(self.getTorres())))


    def condicaoVitoria(self) -> bool:
        if self.getTorres() == self.objetivo:
            return True
        return False


    # tenta realizar a jogada, se não for possivel, a jogada é desfeita
    def jogada(self, pilhaOrigem, pilhaObjetivo) -> bool:
        
        # Avalia o movimento 
        if self.regras.avaliarRequisicao(pilhaOrigem, pilhaObjetivo):
            pilhaObjetivo -= 1
            pilhaOrigem -= 1
            # Remove o valor da torre de origem
            auxiliar = self.torres[pilhaOrigem].remover()

            if auxiliar != 0:
                # incrementa 1 ao numero de jogadas
                self.nJogadas += 1
                # tenta inserir disco na torre objetivo, se não for possivel tenta devolver o disco a torre origem
                if not self.torres[pilhaObjetivo].inserir(auxiliar):
                    self.nJogadas -= 1
                    self.torres[pilhaOrigem].inserir(auxiliar)
                    print(
                        "Você tentou mover um disco maior para cima de um disco menor")
                    return False
                return True
            else:
                print("Você tentou mover um disco que não existe")
        elif pilhaObjetivo == pilhaOrigem:
            print("Você tentou mover um disco para sua localização atual")
        else:
            print("Você tentou manipular torres inexistentes")
        
        return False

    def getEstadoDoJogo(self):
        return deepcopy(self.torres) 
    
    def getTorres(self):
        return [n.getTorre() for n in self.torres]

    def getEstadoObjetivo(self):
        return deepcopy(self.objetivo)
