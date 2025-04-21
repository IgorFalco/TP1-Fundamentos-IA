from estado import Estado
import gc
from funcoes import bfs, bfs_otimizada, dfs, gerarTabuleiro, verificaSolvabilidade, a_estrela, gerar_estado_por_movimentos, avaliar_algoritmo


def main():

    estado_objetivo = Estado([1, 2, 3, 4,
                              5, 6, 7, 8,
                              9, 10, 11, 12,
                              13, 14, 15, 0])

    avaliar_algoritmo("BFS", bfs_otimizada, estado_objetivo,
                      num_testes=10, movimentos_iniciais=30)
    gc.collect()
    avaliar_algoritmo("DFS", dfs, estado_objetivo,
                      num_testes=10, movimentos_iniciais=30)
    gc.collect()
    avaliar_algoritmo("A*", a_estrela, estado_objetivo,
                      num_testes=10, movimentos_iniciais=100)


if __name__ == "__main__":
    main()
