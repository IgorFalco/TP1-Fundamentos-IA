from estado import Estado
import gc
from funcoes import bfs, dfs, a_estrela, avaliar_algoritmos


def main():
    estado_objetivo = Estado([1, 2, 3, 4,
                              5, 6, 7, 8,
                              9, 10, 11, 12,
                              13, 14, 15, 0])

    avaliar_algoritmos("BFS", bfs, estado_objetivo, num_testes=3,
                      max_movimentos=50, tempo_limite=30, caminho_csv="bfs_resultados.csv")
    gc.collect()

    avaliar_algoritmos("DFS", dfs, estado_objetivo, num_testes=3,
                      max_movimentos=50, tempo_limite=30, caminho_csv="dfs_resultados.csv")
    gc.collect()

    avaliar_algoritmos("A*", a_estrela, estado_objetivo, num_testes=3,
                      max_movimentos=100, tempo_limite=30, caminho_csv="a_estrela_resultados.csv")


if __name__ == "__main__":
    main()
