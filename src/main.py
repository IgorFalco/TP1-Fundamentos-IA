from estado import Estado
from grafo import Grafo
from funcoes import bfs_em_grafo, dfs_em_grafo, gerarTabuleiro, verificaSolvabilidade

def main():
    # Tabuleiro mais embaralhado e solucionável
    tabuleiro = [5, 1, 2, 4,
                 9, 6, 3, 8,
                 13, 10, 7, 12,
                 0, 14, 11, 15]

    estado_inicial = Estado(tabuleiro)
    estado_objetivo = Estado([1, 2, 3, 4,
                              5, 6, 7, 8,
                              9, 10, 11, 12,
                              13, 14, 15, 0])

    print("🧩 Estado inicial:", estado_inicial)
    print("🎯 Estado objetivo:", estado_objetivo)

    # Verifica se o tabuleiro é solucionável
    if not verificaSolvabilidade(tabuleiro):
        print("❌ Tabuleiro não é solucionável.")
        return
    else:
        print("✅ Tabuleiro é solucionável.")

    # Cria e expande o grafo até encontrar o objetivo
    grafo = Grafo()
    encontrado = grafo.construir_grafo(estado_inicial, estado_objetivo)

    if not encontrado:
        print("⚠️ O estado objetivo NÃO foi encontrado na construção do grafo.")
        return
    else:
        print("✅ O estado objetivo foi incluído no grafo.")

    # --- BFS no grafo ---
    caminho_bfs = bfs_em_grafo(grafo, estado_inicial, estado_objetivo)
    if caminho_bfs:
        print("\n✅ BFS (no grafo) encontrou solução!")
        print(f"Movimentos: {len(caminho_bfs) - 1}")
        for i, passo in enumerate(caminho_bfs):
            print(f"Passo {i}: {passo}")
    else:
        print("\n❌ BFS não encontrou solução no grafo.")

    # --- DFS no grafo ---
    caminho_dfs = dfs_em_grafo(grafo, estado_inicial, estado_objetivo)
    if caminho_dfs:
        print("\n✅ DFS (no grafo) encontrou solução!")
        print(f"Movimentos: {len(caminho_dfs) - 1}")
        for i, passo in enumerate(caminho_dfs):
            print(f"Passo {i}: {passo}")
    else:
        print("\n❌ DFS não encontrou solução no grafo (ou bateu no limite de profundidade).")

if __name__ == "__main__":
    main()
