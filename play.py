from Jogo.game import game
from JogadoresAutomatizados.dfs import dfs


def exibicao(pilhas: list):
    def verificarVazio(valor: int):
        if valor == 0:
            return "( )"
        else:
            return f"({valor})"

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

    if player == 3:
        print("Você escolheu o jogador DFS")
        machine = dfs(partida)
        print("Buscando ações, por favor aguarde")
        manual = reversed(machine.jogar())
        manual = [n.pegarValor(1) for n in manual]
        manual.pop(0)  # o primeiro comando é 0,0
        while len(manual) != 0:
            exibicao(partida.getTorres())
            comando = manual.pop(0)
            origem = comando[0]
            destino = comando[1]
            partida.jogada(origem, destino)
            if partida.condicaoVitoria():
                print("Vencedor")
                break

exibicao(partida.getTorres())
