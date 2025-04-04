from estado import Estado
from funcoes import gerarTabuleiro, verificaSolvabilidade
from grafo import Grafo


def main():
    # Gera um tabuleiro inicial solvável
    tabuleiro = gerarTabuleiro()
    while not verificaSolvabilidade(tabuleiro):
        tabuleiro = gerarTabuleiro()

    estado_inicial = Estado(tabuleiro)
    print("Estado inicial: " + str(estado_inicial))

    # Inicializa e constrói o grafo a partir do estado inicial
    grafo = Grafo()
    grafo.construir_grafo(estado_inicial, limite=10)

    print("\nGrafo construído com os seguintes estados:")
    grafo.exibir_grafo()


if __name__ == "__main__":
    main()
