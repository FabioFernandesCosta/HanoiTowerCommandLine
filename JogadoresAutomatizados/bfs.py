from Jogo.torre import torre
from Jogo.game import game
from JogadoresAutomatizados.node import node
from Jogo.regras import regras
from copy import deepcopy
import time

class bfs:
    abertos, fechados, inicial, X, jogo = None, None, None, None, None

    def __init__(self, jogo):
        self.jogo = jogo
        self.inicial = node(None,[[0,0],self.jogo.getEstadoDoJogo(), self.jogo.getTorres()])
        self.abertos = [self.inicial] #:list[node]
        self.fechados = [] #:list


    def jogar(self):
        start_time = time.time()
        while(self.abertos):
            self.X = self.abertos.pop(0) 
            tam = None
            #obtem o objetivo
            if not(tam):
                tam = len(self.X.pegarValor(3)[2])
                res = []
                for _ in reversed(range(tam)):
                    res.append(_ + 1)
                


            if self.X.pegarValor(3)[2] == res: 
                
                ####gerar caminho inverso pegando os pais a partir do X até chegar no ponto onde n se tem pai
                cmdWin = []
                while(self.X.pegarPai() != None):
                    cmdWin.append(self.X.pegarValor(1))
                    self.X = self.X.pegarPai()
                
                cmdWin = list(reversed(cmdWin))
                
                print(f"{cmdWin} \n \n")
                print("--- %s seconds ---" % (time.time() - start_time))
                return(cmdWin)


            else:
                #filhos são gerados
                self.criarFilhos(self.X, self.X.pegarValor(2))

                #X adicionado em fechados
                self.fechados.append(self.X)

                #filhos ja registrados retirados
                filhos = self.X.pegarFilhos()
                for _ in filhos:

                    af = self.abertos + self.fechados
                    for i in af:
                        if(_.pegarValor(3) == i.pegarValor(3)):
                            self.X.removerFilho(_)
                            break

                #lista de filhos recuperados
                filhos = self.X.pegarFilhos()
                for _ in filhos:
                    self.abertos.append(_)
        else:
            print("FALHA")

    def criarFilhos(self, pai: node, espaco_de_estado):
        espacoGerado = None
        torresDoEspaco = None

        for i in range(1,4):
            for j in range(1,4):
                if(i != j):

                    if regras.avaliarJogada(self,i,j,espaco_de_estado):
                        espacoGerado = self.criarEspacoDeEstado([i,j],espaco_de_estado)
                        torresDoEspaco = self.criarTorresEmLista(espacoGerado)
                        pai.inserirFilho(node(pai,[[i,j],espacoGerado,torresDoEspaco]))

    def criarTorresEmLista(self, espaco_de_estado):
        return deepcopy([n.getTorre() for n in espaco_de_estado])

    def criarEspacoDeEstado(self, movimento, espaco_de_estado):
        espaco = deepcopy(espaco_de_estado)
        pilhaOrigem = movimento[0] - 1
        pilhaObjetivo = movimento[1] - 1
        espaco[pilhaObjetivo].inserir(espaco[pilhaOrigem].remover())
        return espaco
        