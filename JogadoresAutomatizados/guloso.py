from JogadoresAutomatizados.auxiliares.heuristica import heuristica
from copy import deepcopy
from JogadoresAutomatizados.node import node
from Jogo.regras import regras
from Jogo.game import game

class guloso:
    pilhaDeDecisoes, caminhoDaVitoria, jogo, heuristica = None, None, None, None

    def __init__(self, _jogo: game) -> None:
        self.pilhaDeDecisoes = list()
        self.caminhoDaVitoria = list()
        self.jogo = _jogo
        self.heuristica = heuristica()
        
    
    def criarEspacoDeEstado(self, movimento, espaco_de_estado):
        espaco = deepcopy(espaco_de_estado)
        pilhaOrigem = movimento[0] - 1
        pilhaObjetivo = movimento[1] - 1
        espaco[pilhaObjetivo].inserir(espaco[pilhaOrigem].remover())
        return espaco

    def criarTorresEmLista(self, espaco_de_estado):
        return deepcopy([n.getTorre() for n in espaco_de_estado])
    
    def criarFilhos(self, pai: node, espaco_de_estado):
        espacoGerado = None
        torresDoEspaco = None

        if regras.avaliarJogada(self,1,2,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([1,2],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            heuristicaa = self.heuristica.getHeur(torresDoEspaco)
            pai.inserirFilho(node(pai,[[1,2],espacoGerado,torresDoEspaco, heuristicaa]))

        if regras.avaliarJogada(self,1,3,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([1,3],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            heuristicaa = self.heuristica.getHeur(torresDoEspaco)
            pai.inserirFilho(node(pai,[[1,3],espacoGerado,torresDoEspaco, heuristicaa]))

        if regras.avaliarJogada(self,2,1,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([2,1],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            heuristicaa = self.heuristica.getHeur(torresDoEspaco)
            pai.inserirFilho(node(pai,[[2,1],espacoGerado,torresDoEspaco, heuristicaa]))

        if regras.avaliarJogada(self,2,3,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([2,3],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            heuristicaa = self.heuristica.getHeur(torresDoEspaco)
            pai.inserirFilho(node(pai,[[2,3],espacoGerado,torresDoEspaco, heuristicaa]))
            
        if regras.avaliarJogada(self,3,1,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([3,1],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            heuristicaa = self.heuristica.getHeur(torresDoEspaco)
            pai.inserirFilho(node(pai,[[3,1],espacoGerado,torresDoEspaco, heuristicaa]))

        if regras.avaliarJogada(self,3,2,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([3,2],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            heuristicaa = self.heuristica.getHeur(torresDoEspaco)
            pai.inserirFilho(node(pai,[[3,2],espacoGerado,torresDoEspaco, heuristicaa]))

    def verificarEspacosDeEstadosNaLista(self, filhos, memoria):
        espacosDeEstadoFilhos = [n.pegarValor(3) for n in filhos]
        espacosDeEstadoMemoria = [n.pegarValor(3) for n in memoria]



        return all(n in espacosDeEstadoMemoria for n in espacosDeEstadoFilhos)



    def jogar(self):
        inicial = node(None,[[0,0],self.jogo.getEstadoDoJogo(), self.jogo.getTorres(), self.heuristica.getHeur(self.jogo.getTorres())])

        self.pilhaDeDecisoes.insert(0,inicial)
        self.caminhoDaVitoria.insert(0,inicial)
        escolhido = self.pilhaDeDecisoes[0]

        while(True):

            if escolhido.pegarValor(3) == self.jogo.getEstadoObjetivo():
                print("achamos a vitória")
                return self.caminhoDaVitoria
            
            self.criarFilhos(escolhido, escolhido.pegarValor(2)) 

            filhos = escolhido.pegarFilhos()

            filhos = [x for x in filhos if x.pegarValor(3) not in [n.pegarValor(3) for n in self.caminhoDaVitoria]]
            
            if len(filhos) == 0:
                print("Solução não encontrada")
                return self.caminhoDaVitoria
            else:
                escolhido = min(filhos,key = lambda x: x.pegarValor(4))
            
            self.caminhoDaVitoria.append(escolhido)
    
            

            


