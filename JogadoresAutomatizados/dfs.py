from Jogo.torre import torre
from Jogo.game import game
from JogadoresAutomatizados.node import node
from Jogo.regras import regras
from copy import deepcopy

class dfs:
    #espacos_ja_visitados = None 
    estado_atual, pilha_de_decisoes, caminho_da_vitoria, jogo = None, None, None, None
    
    # espacos_ja_visitados = bbs
    # estado_atual = ec
    # pilha_de_decisoes = lne
    # caminho_da_vitoria = le
    # ---
    # A pilha de decisões contem um nó que representa o espaço de estado, esse nó contem 2 valores
    # A coordenada usada para criar aquele espaço de estado, por exemplo: (1,2)
    # O espaço de estado gerado

    def __init__(self, jogo: game) -> None:
        self.jogo = jogo
        self.estado_atual = None
        self.pilha_de_decisoes = list()
        self.caminho_da_vitoria = list()
        #self.espacos_ja_visitados = list()
    
    #-------------

    def verificarEspacosDeEstadosNaLista(self, filhos, memoria):
        espacosDeEstadoFilhos = [n.pegarValor(3) for n in filhos]
        espacosDeEstadoMemoria = [n.pegarValor(3) for n in memoria]

        return all(n in espacosDeEstadoMemoria for n in espacosDeEstadoFilhos)
    
    #-------------

    def criarEspacoDeEstado(self, movimento, espaco_de_estado):
        espaco = deepcopy(espaco_de_estado)
        pilhaOrigem = movimento[0] - 1
        pilhaObjetivo = movimento[1] - 1
        espaco[pilhaObjetivo].inserir(espaco[pilhaOrigem].remover())
        return espaco
    
    #-------------

    def criarTorresEmLista(self, espaco_de_estado):
        return deepcopy([n.getTorre() for n in espaco_de_estado])
    
    #-------------

    def criarFilhos(self, pai: node, espaco_de_estado):
        espacoGerado = None
        torresDoEspaco = None

        if regras.avaliarJogada(self,1,2,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([1,2],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            pai.inserirFilho(node(pai,[[1,2],espacoGerado,torresDoEspaco]))

        if regras.avaliarJogada(self,1,3,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([1,3],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            pai.inserirFilho(node(pai,[[1,3],espacoGerado,torresDoEspaco]))

        if regras.avaliarJogada(self,2,1,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([2,1],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            pai.inserirFilho(node(pai,[[2,1],espacoGerado,torresDoEspaco]))

        if regras.avaliarJogada(self,2,3,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([2,3],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            pai.inserirFilho(node(pai,[[2,3],espacoGerado,torresDoEspaco]))
            
        if regras.avaliarJogada(self,3,1,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([3,1],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            pai.inserirFilho(node(pai,[[3,1],espacoGerado,torresDoEspaco]))

        if regras.avaliarJogada(self,3,2,espaco_de_estado):
            espacoGerado = self.criarEspacoDeEstado([3,2],espaco_de_estado)
            torresDoEspaco = self.criarTorresEmLista(espacoGerado)
            pai.inserirFilho(node(pai,[[3,2],espacoGerado,torresDoEspaco]))

    #-------------

    def jogar(self):
        inicial = node(None,[[0,0],self.jogo.getEstadoDoJogo(), self.jogo.getTorres()])
        self.estado_atual = inicial
        self.caminho_da_vitoria.insert(0,inicial)
        self.pilha_de_decisoes.insert(0,inicial)
        
        while(len(self.pilha_de_decisoes) != 0):
            
            if self.estado_atual.pegarValor(3) == self.jogo.getEstadoObjetivo():
                print("achamos a vitória")
                return self.caminho_da_vitoria
            
            self.criarFilhos(self.estado_atual, self.estado_atual.pegarValor(2))
            filhos = self.estado_atual.pegarFilhos()

            if any([self.estado_atual.quantidadeDeFilhos == 0, self.verificarEspacosDeEstadosNaLista(filhos,self.caminho_da_vitoria), self.verificarEspacosDeEstadosNaLista(filhos, self.pilha_de_decisoes)]):
                
                while(all([len(self.caminho_da_vitoria) != 0, self.estado_atual == self.caminho_da_vitoria[0]])):
                    
                    self.caminho_da_vitoria.pop(0).pegarValor(3)

                    self.pilha_de_decisoes.pop(0)
                    
                    self.estado_atual = self.pilha_de_decisoes[0]
                
                self.caminho_da_vitoria.insert(0,self.estado_atual)

            else:
                pilhaDeDecisao = [espaco.pegarValor(3) for espaco in self.pilha_de_decisoes]
                caminhoDaVitoria = [espaco.pegarValor(3) for espaco in self.caminho_da_vitoria]

                for filho in range(len(filhos)):
                    if all([not filhos[filho].pegarValor(3) in pilhaDeDecisao, not filhos[filho].pegarValor(3) in caminhoDaVitoria]):
                        self.pilha_de_decisoes.insert(0,filhos[filho])

                self.estado_atual = self.pilha_de_decisoes[0]
                self.caminho_da_vitoria.insert(0,self.estado_atual)
            
        return False




