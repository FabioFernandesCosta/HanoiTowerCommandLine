from game import game;

def exibicao(pilhas: list):

    for i in reversed(range(len(pilhas))):
        print(f"({pilhas[0][i]})")
        

if __name__ == '__main__':
    
    discos = int(input("Com quantos discos você quer jogar?" + '\n'))
    partida = game(discos)

    while(not partida.condicaoVitoria()):
        print("Entrou")
        print(partida.getAllPilhas())
        print("")
        exibicao(partida.getAllPilhas())
        break


