from game import game;

def exibicao(pilhas: list):

    def verificarVazio(valor: int):
        if valor == 0:
            return "( )"
        else:
            return f"({valor})"


    for valor in reversed(range(len(pilhas))):
        for torre in range(len(pilhas)):
            if torre == 0: 
                print('\n'+ f" {verificarVazio(pilhas[torre][valor])}", end=" ")
            else:
                print(f" {verificarVazio(pilhas[torre][valor])}", end=" ")
    
    print("\n"+"________________")
    print("  1  | 2 |  3")

if __name__ == '__main__':
    
    discos = int(input("Com quantos discos você quer jogar?" + '\n'))
    partida = game(discos)

    while True:
        exibicao(partida.getTorres())
        partida.jogada(int(input("Qual a pilha de origem?" + '\n')), int(input("Qual a pilha de destino?" + '\n')))
        if partida.condicaoVitoria():
            print("Vencedor")
            break
        
        
        


