from estado import Estado
from grafo import Grafo
from funcoes import bfs_em_grafo, dfs_em_grafo, gerarTabuleiro, verificaSolvabilidade, a_estrela, gerar_estado_por_movimentos


def main():
    tabuleiro = gerarTabuleiro()

    while not verificaSolvabilidade(tabuleiro):
        tabuleiro = gerarTabuleiro()

    # Tabuleiro de exemplo solvável rápido
    # tabuleiro = [5, 1, 2, 4,
    #              9, 6, 3, 8,
    #              13, 10, 7, 12,
    #              0, 14, 11, 15]

    # estado_inicial = Estado(tabuleiro)
    estado_inicial = gerar_estado_por_movimentos(50)
    estado_objetivo = Estado([1, 2, 3, 4,
                              5, 6, 7, 8,
                              9, 10, 11, 12,
                              13, 14, 15, 0])

    print("🧩 Estado inicial:", estado_inicial)
    print("🎯 Estado objetivo:", estado_objetivo)

    # Cria e expande o grafo
    grafo = Grafo()
    grafo.construir_grafo(estado_inicial, limite=2000)

    grafoBFS = grafo.copia()
    grafoDFS = grafo.copia()

    print(f"📌 Vértices no grafo: {len(grafo.vertices)}")
    if estado_objetivo not in grafo.vertices:
        print("⚠️ Estado objetivo não gerado no grafo!")
    else:
        print("🎯 Estado objetivo presente no grafo.")

    # # --- BFS no grafo ---
    # caminho_bfs = bfs_em_grafo(
    #     grafoBFS, estado_inicial, estado_objetivo, limite_vertices_total=200000)
    # if caminho_bfs:
    #     print("\n✅ BFS (no grafo) encontrou solução!")
    #     print(f"Movimentos: {len(caminho_bfs) - 1}")
    #     for i, passo in enumerate(caminho_bfs):
    #         print(f"Passo {i}: {passo}")
    # else:
    #     print("\n❌ BFS não encontrou solução no grafo com o limite configurado.")

    # # --- DFS no grafo ---
    # caminho_dfs = dfs_em_grafo(grafoDFS, estado_inicial, estado_objetivo,
    #                            limite_profundidade=10, limite_vertices_total=100000)
    # if caminho_dfs:
    #     print("\n✅ DFS (no grafo) encontrou solução!")
    #     print(f"Movimentos: {len(caminho_dfs) - 1}")
    #     for i, passo in enumerate(caminho_dfs):
    #         print(f"Passo {i}: {passo}")
    # else:
    #     print("\n❌ DFS não encontrou solução no grafo com o limite configurado")

    # --- A* no grafo ---
    caminho_a_estrela = a_estrela(
        grafo, estado_inicial, estado_objetivo, limite_vertices_total=1000000)

    if caminho_a_estrela:
        print("\n✅ A* encontrou solução!")
        print(f"Movimentos: {len(caminho_a_estrela) - 1}")
        for i, passo in enumerate(caminho_a_estrela):
            print(f"Passo {i}: {passo}")
    else:
        print("\n❌ A* não encontrou solução no grafo com o limite configurado")


if __name__ == "__main__":
    main()
