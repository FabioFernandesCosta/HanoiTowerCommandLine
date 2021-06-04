from JogadoresAutomatizados.nodestar import nodeStar
from Jogo.torre import torre
from Jogo.game import game
from Jogo.regras import regras
from copy import deepcopy
import time

'''
Use g(x)=depth of the node,
 and h (x)= (the total number of disks of left and middle poles) + 2*（number of disks that in the right pole and smaller than any disk that in left or middle poles）.
'''


class aEstrela:
    abertos, X, fechados = None,None,None

    def __init__(self, jogo):
        self.jogo = jogo
        self.abertos = [nodeStar(None,[[0,0],self.jogo.getEstadoDoJogo(), self.jogo.getTorres()])] #:list[node]
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
                
                #print(f"{cmdWin} \n \n")
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

                    af =  self.fechados
                    for i in af:
                        if(_.pegarValor(3) == i.pegarValor(3)):
                            self.X.removerFilho(_)
                            break
                
                #lista de filhos recuperados
                filhos = self.X.pegarFilhos()
                #print(fil.pegarValor(3) for fil in filhos) ###################


                for _ in filhos:
                    self.abertos.append(_)

                self.abertos.sort(key=lambda x: x.getFdx())


                

        print(f"falha")





    def criarFilhos(self, pai: nodeStar, espaco_de_estado):
        
        espacoGerado = None
        torresDoEspaco = None

        for i in range(1,4):
            for j in range(1,4):
                if(i != j):
                    
                    if regras.avaliarJogada(self,i,j,espaco_de_estado):
                        espacoGerado = self.criarEspacoDeEstado([i,j],espaco_de_estado)
                        torresDoEspaco = self.criarTorresEmLista(espacoGerado)
                        #### ponto de falha, morrendo na criação do filho
                        fil = nodeStar(pai,[[i,j],espacoGerado,torresDoEspaco])
                        
                        pai.inserirFilho(fil)   
                        ####

    def criarTorresEmLista(self, espaco_de_estado):
        return deepcopy([n.getTorre() for n in espaco_de_estado])

    def criarEspacoDeEstado(self, movimento, espaco_de_estado):
        espaco = deepcopy(espaco_de_estado)
        pilhaOrigem = movimento[0] - 1
        pilhaObjetivo = movimento[1] - 1
        espaco[pilhaObjetivo].inserir(espaco[pilhaOrigem].remover())
        return espaco