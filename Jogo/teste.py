from Jogo.torre import torre
from Jogo.game import game
from JogadoresAutomatizados.node import node
from Jogo.regras import regras
from copy import deepcopy

class bfs:
    bbs, estado_atual, pilha_de_decisoes, caminho_da_vitoria, jogo, interface = None, None, None, None, None, None
    # bbs = lixo
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
        self.bbs = list()

    def verificarSeExiste(self, filhos: list, memoria: list):
        memoriaF = [[x[0].getTorre(),x[1].getTorre(),x[2].getTorre()] for x in [n.pegarValor()[1] for n in memoria]]
        filhosF = [[x[0].getTorre(),x[1].getTorre(),x[2].getTorre()] for x in [n.pegarValor()[1] for n in filhos]]

        print(f"Memória que está vindo = {memoriaF}")
        print(f"Filhos que estão vindo = {filhosF}")

        return (filhosF in memoriaF)

    def criarEspacoDeEstado(self, espaco_atual, movimento: list):
        auxiliar = deepcopy(espaco_atual) 
        pilhaOrigem = movimento[0] - 1
        pilhaDestino = movimento[1] - 1
        auxiliar[pilhaDestino].inserir(auxiliar[pilhaOrigem].remover())
        return auxiliar

    def criarEspacosDeEstados(self, espaco_de_estado, dono_do_espaco: node):
        novoEspaco = None
        if regras.avaliarJogada(self, 1, 2, espaco_de_estado):
            
            novoEspaco = self.criarEspacoDeEstado(espaco_de_estado, [1, 2])

            dono_do_espaco.inserirFilho(
                node(dono_do_espaco, [[1, 2], novoEspaco]))

        if regras.avaliarJogada(self, 1, 3, espaco_de_estado):

            novoEspaco = self.criarEspacoDeEstado(espaco_de_estado, [1, 3])

            dono_do_espaco.inserirFilho(
                node(dono_do_espaco, [[1, 3], novoEspaco]))

        if regras.avaliarJogada(self, 2, 3, espaco_de_estado):
            
            novoEspaco = self.criarEspacoDeEstado(espaco_de_estado, [2, 3])

            dono_do_espaco.inserirFilho(
                node(dono_do_espaco, [[2, 3], novoEspaco]))

        if regras.avaliarJogada(self, 3, 1, espaco_de_estado):

            novoEspaco = self.criarEspacoDeEstado(espaco_de_estado, [3, 1])

            dono_do_espaco.inserirFilho(
                node(dono_do_espaco, [[3, 1], novoEspaco]))

        if regras.avaliarJogada(self, 3, 2, espaco_de_estado):

            novoEspaco = self.criarEspacoDeEstado(espaco_de_estado, [3, 2])
            
            dono_do_espaco.inserirFilho(
                node(dono_do_espaco, [[3, 2], novoEspaco]))

        if regras.avaliarJogada(self, 2, 1, espaco_de_estado):

            novoEspaco = self.criarEspacoDeEstado(espaco_de_estado, [2, 1])
            
            dono_do_espaco.inserirFilho(
                node(dono_do_espaco, [[2, 1], novoEspaco]))

    def jogar(self):
        self.estado_atual = node(None, [[1, 1], self.jogo.getEstadoDoJogo()])
        self.caminho_da_vitoria.append(self.estado_atual)
        self.pilha_de_decisoes.append(self.estado_atual)
        contador = 0
        while(len(self.pilha_de_decisoes) != 0 and contador != 5):
            print(
                f"tamanho da pilha de decisões {len(self.pilha_de_decisoes)}")
            contador += 1
            print(contador)
            origem = self.estado_atual.pegarValor()[0][0]
            destino = self.estado_atual.pegarValor()[0][1]
            self.jogo.jogada(origem, destino)

            if self.jogo.condicaoVitoria():
                return self.caminho_da_vitoria
            
            self.criarEspacosDeEstados(self.estado_atual.pegarValor()[1], self.estado_atual)

            filhos = self.estado_atual.pegarFilhos()

            if any([self.estado_atual.quantidadeDeFilhos() == 0, self.verificarSeExiste(filhos, self.bbs), self.verificarSeExiste(filhos, self.caminho_da_vitoria), self.verificarSeExiste(filhos, self.pilha_de_decisoes)]):
                print("entrou aqui")
                while(len(self.caminho_da_vitoria) != 0 and self.estado_atual == self.caminho_da_vitoria[0]):
                    self.jogo.jogada(
                        list(reversed(self.estado_atual.pegarValor()[0])))
                    self.bbs.append(self.estado_atual)
                    self.caminho_da_vitoria.pop(0)
                    self.pilha_de_decisoes.pop(0)
                    self.estado_atual = self.pilha_de_decisoes[0]
                self.caminho_da_vitoria.append(self.estado_atual)

            else:
                bbs = [[x[0].getTorre(),x[1].getTorre(),x[2].getTorre()] for x in [n.pegarValor()[1] for n in self.bbs]]
                caminhoDaVitoria = [[x[0].getTorre(),x[1].getTorre(),x[2].getTorre()] for x in [n.pegarValor()[1] for n in self.caminho_da_vitoria]]
                pilhaDeDecisao = [[x[0].getTorre(),x[1].getTorre(),x[2].getTorre()] for x in [n.pegarValor()[1] for n in self.pilha_de_decisoes]]
                for filho in range(len(filhos)):
                    torres = [n.getTorre() for n in filhos[filho].pegarValor()[1]]
                    if all([not torres in bbs, not torres in pilhaDeDecisao, not torres in caminhoDaVitoria]):
                        self.pilha_de_decisoes.insert(0,filhos[filho])
                        pilhaDeDecisao.insert(0,torres)
                self.estado_atual = self.pilha_de_decisoes[0]

        return False
