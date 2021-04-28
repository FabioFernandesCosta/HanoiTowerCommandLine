from Jogo.torre import torre
import copy


class regras:
    def __init__(self) -> None:
        pass

    def avaliarRequisicao(self, pilhaOrigem: int, pilhaObjetivo: int) -> bool:
        return all([pilhaOrigem > 0, pilhaObjetivo > 0, pilhaObjetivo <= 3, pilhaOrigem <= 3, pilhaOrigem != pilhaObjetivo])

    def avaliarJogada(self, pilhaOrigem, pilhaObjetivo, torres: list) -> bool:
        torresA = copy.deepcopy(torres)

        if not regras.avaliarRequisicao(self,pilhaOrigem, pilhaObjetivo):
            return False
        
        pilhaOrigem -= 1
        pilhaObjetivo -= 1

        auxiliar = torresA[pilhaOrigem].remover() 
       
        if auxiliar != 0:
            return torresA[pilhaObjetivo].inserir(auxiliar)

        return False
