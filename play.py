from Jogo.game import game
from JogadoresAutomatizados.dfs import dfs
from JogadoresAutomatizados.bfs import bfs
import time


def exibicao(pilhas: list):
    def verificarVazio(valor: int):
        if valor == 0:
            return "( )"
        else:
            return f"({valor})"
    print('\n')
    for valor in reversed(range(len(pilhas[0]))):
        for torre in range(len(pilhas)):
            if torre == 0:
                print(
                    '\n' + f" {verificarVazio(pilhas[torre][valor])}", end=" ")
            else:
                print(f" {verificarVazio(pilhas[torre][valor])}", end=" ")

    print("\n"+"________________")
    print("  1  | 2 |  3")


if __name__ == '__main__':

    discos = int(input("Com quantos discos você quer jogar?" + '\n'))
    partida = game(discos)

    print("Quem vai jogar?")
    print("1 - Humano")
    print("2 - Agente BFS")
    print("3 - Agente DFS")

    player = int(input())

    if player == 1:
        print("Você escolheu jogar")
        while True:
            exibicao(partida.getTorres())
            partida.jogada(int(input("Qual a pilha de origem?" + '\n')),
                           int(input("Qual a pilha de destino?" + '\n')))
            if partida.condicaoVitoria():
                print("Vencedor")
                break
    elif player == 2:
        print("Você escolheu o jogador BFS")
        machine = bfs(partida)
        print("Buscando ações, por favor aguarde")
        manual = machine.jogar()
        exibicao(partida.getTorres())
        while len(manual) != 0:

            if(len(manual) > 14):
                tempo = 30/len(manual)
            else:
                tempo = 1.5

            time.sleep(tempo)
            comando = manual.pop(0)
            origem = comando[0]
            destino = comando[1]
            partida.jogada(origem, destino)
            exibicao(partida.getTorres())
        else:
            print("\n Vencedor")
            


    elif player == 3:
        print("Você escolheu o jogador DFS")
        machine = dfs(partida)
        print("Buscando ações, por favor aguarde")
        manual = reversed(machine.jogar())
        manual = [n.pegarValor(1) for n in manual]
        manual.pop(0)  # o primeiro comando é 0,0
        exibicao(partida.getTorres())
        while len(manual) != 0:
            

            if(len(manual) > 14):
                tempo = 30/len(manual)
            else:
                tempo = 1.5

            time.sleep(tempo)
            comando = manual.pop(0)
            origem = comando[0]
            destino = comando[1]
            partida.jogada(origem, destino)
            exibicao(partida.getTorres())
            if partida.condicaoVitoria():
                print("\n Vencedor")
                
                break

#exibicao(partida.getTorres())
