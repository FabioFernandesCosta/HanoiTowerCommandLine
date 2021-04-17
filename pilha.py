

class pilha:
    pilhaArray, topo = None, None
    
    # inicializa
    def __init__(self):
        self.pilhaArray = []
        self.topo = -1
        pass

    # insere um disco no topo
        #retorna True ou False, para facilitar o controle sobre as pilhas
            #EX: se o disco não puder ser inserido será retornado false para para que o manipulador possa devolver o disco ao seu lugar original
    def inserir(self, disco:int):
        if not self.pilhaArray:
            self.topo += 1
            self.pilhaArray.append(disco)
            return True

        elif disco < self.pilhaArray[self.topo]:
            self.topo += 1
            self.pilhaArray.append(disco)
            return True

        else:
            # jogada jogada não será feita
            # avisar jogada invalida
            return False
            pass


    # remove o disco que esta no topo
    def remover(self):
        if self.pilhaArray:
            discoRemovido = self.pilhaArray.pop(self.topo)
            self.topo -= 1
            return discoRemovido
        else:
            print('ERROR: P1')
            # avisar erro pois isso não deveria ser chamado se a pilha de discos estiver vazia
            print
            pass
        



    # descobre o topo
    def getTopo(self):
        return self.topo

    # descobre o disco que está no topo
    def getDiscoTopo(self):
        return self.pilhaArray[self.topo]


    
        
