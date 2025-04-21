# TP 1 - Fundamentos de IA
# Julia Machado, Igor Falco, Eduardo Fernandes

import random
import gc
from tqdm import tqdm
import time
from collections import deque
import heapq
from estado import Estado
from grafo import Grafo

#########   Tarefa 1   #########


def verificaSolvabilidade(tabuleiro):
    inversoes = 0
    posicaoVazia = -1

    for i in range(15):  # Percorre até o penúltimo elemento
        for j in range(i+1, 16):  # Compara com os elementos à frente

            if tabuleiro[i] > tabuleiro[j] and tabuleiro[i] != 0 and tabuleiro[j] != 0:
                inversoes += 1

    # Encontra a posição do número 0 (espaço vazio)
    posicaoVazia = tabuleiro.index(0)

    if posicaoVazia != -1:
        linhaVazia = posicaoVazia//4  # Linha em que está o espaço vazio

    # Verifica se é solucionável
    if (inversoes % 2 == 0 and linhaVazia % 2 != 0) or (inversoes % 2 != 0 and linhaVazia % 2 == 0):
        return True
    else:
        return False

#########   Tarefa 2   #########


def gerarTabuleiro():
    tabuleiro = list(range(16))  # [0, 1, ..., 15]
    random.shuffle(tabuleiro)
    return tabuleiro


def gerar_estado_por_movimentos(n, estado_objetivo=None):
    if estado_objetivo is None:
        estado_objetivo = Estado([
            1, 2, 3, 4,
            5, 6, 7, 8,
            9, 10, 11, 12,
            13, 14, 15, 0
        ])

    estado_atual = estado_objetivo
    anterior = None

    for _ in range(n):
        vizinhos = estado_atual.get_neighbors()

        # Evita desfazer o último movimento
        if anterior is not None:
            vizinhos = [v for v in vizinhos if v != anterior]

        if not vizinhos:
            break  # Sem opções de movimento

        anterior, estado_atual = estado_atual, random.choice(vizinhos)

    return estado_atual


#########   Tarefa 3   #########


def bfs(grafo, estado_inicial, estado_objetivo, limite_vertices_total=1000000):
    pbar = tqdm(total=limite_vertices_total, desc="BFS Expandindo nós")
    fila = deque([estado_inicial])
    visitados = set()
    predecessores = {estado_inicial: None}
    nos_expandidos = 0

    grafo.adicionar_vertice(estado_inicial)

    while fila:
        atual = fila.popleft()
        visitados.add(atual)
        nos_expandidos += 1
        pbar.update(1)

        if atual == estado_objetivo:
            pbar.close()
            caminho = []
            while atual:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            print(f"🔎 BFS - Nós expandidos: {nos_expandidos}")
            grafo.nos_expandidos = nos_expandidos
            return caminho

        for vizinho in atual.get_neighbors():
            if vizinho not in grafo.vertices:
                if len(grafo.vertices) >= limite_vertices_total:
                    continue
                grafo.adicionar_vertice(vizinho)
                grafo.adicionar_aresta(atual, vizinho)

            if vizinho not in visitados and vizinho not in fila:
                fila.append(vizinho)
                predecessores[vizinho] = atual

    print(f"⚠️ BFS - Limite de nós atingido. Nós expandidos: {nos_expandidos}")
    grafo.nos_expandidos = nos_expandidos
    pbar.close()
    return None


def dfs(grafo, estado_inicial, estado_objetivo, limite_profundidade=1000, limite_vertices_total=1000000):
    pbar = tqdm(total=limite_vertices_total, desc="DFS Expandindo nós")
    stack = [(estado_inicial, 0)]  # Pilha com (nó, profundidade)
    visitados = set()
    predecessores = {estado_inicial: None}
    nos_expandidos = 0

    grafo.adicionar_vertice(estado_inicial)

    while stack:
        atual, profundidade = stack.pop()

        # Evita ciclos
        if atual in visitados:
            continue
        visitados.add(atual)
        nos_expandidos += 1
        pbar.update(1)

        # Se encontrou o estado objetivo
        if atual == estado_objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            print(f"🔎 DFS - Nós expandidos: {nos_expandidos}")
            grafo.nos_expandidos = nos_expandidos
            pbar.close()
            return caminho

        # Limite de profundidade
        if profundidade < limite_profundidade:
            for vizinho in atual.get_neighbors():
                if len(grafo.vertices) >= limite_vertices_total:
                    continue
                if vizinho not in visitados:
                    if vizinho not in grafo.vertices:
                        grafo.adicionar_vertice(vizinho)
                        grafo.adicionar_aresta(atual, vizinho)

                    predecessores[vizinho] = atual
                    # Aumenta a profundidade
                    stack.append((vizinho, profundidade + 1))

    print(
        f"⚠️ DFS - Nenhuma solução encontrada. Nós expandidos: {nos_expandidos}")
    grafo.nos_expandidos = nos_expandidos
    pbar.close()
    return None


#########   Tarefa 4   #########


def heuristica_distancia_manhattan(estado_atual, estado_objetivo):
    distancia = 0
    for i in range(1, 16):  # ignorar o 0 (espaço vazio)
        idx_atual = estado_atual.tabuleiro.index(i)
        idx_objetivo = estado_objetivo.tabuleiro.index(i)
        linha_atual, col_atual = divmod(idx_atual, 4)
        linha_obj, col_obj = divmod(idx_objetivo, 4)
        distancia += abs(linha_atual - linha_obj) + abs(col_atual - col_obj)
    return distancia


def a_estrela(grafo, estado_inicial, estado_objetivo, limite_vertices_total=1000000):
    pbar = tqdm(total=limite_vertices_total, desc="A* Expandindo nós")
    heap = []
    contador = 0
    g_score = {estado_inicial: 0}
    f_score = {estado_inicial: heuristica_distancia_manhattan(
        estado_inicial, estado_objetivo)}
    predecessores = {estado_inicial: None}
    em_heap = {estado_inicial}
    visitados = set()
    nos_expandidos = 0

    grafo.adicionar_vertice(estado_inicial)
    heapq.heappush(heap, (f_score[estado_inicial], contador, estado_inicial))

    while heap:
        _, _, atual = heapq.heappop(heap)
        em_heap.discard(atual)

        if atual in visitados:
            continue

        visitados.add(atual)
        nos_expandidos += 1
        pbar.update(1)
        if atual == estado_objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            grafo.nos_expandidos = nos_expandidos
            pbar.close()
            return caminho

        for vizinho in atual.get_neighbors():
            if len(grafo.vertices) >= limite_vertices_total:
                continue

            grafo.adicionar_vertice(vizinho)
            grafo.adicionar_aresta(atual, vizinho)

            if vizinho in visitados:
                continue

            g_tentativa = g_score[atual] + 1

            if g_tentativa < g_score.get(vizinho, float('inf')):
                g_score[vizinho] = g_tentativa
                f = g_tentativa + \
                    heuristica_distancia_manhattan(vizinho, estado_objetivo)
                f_score[vizinho] = f
                predecessores[vizinho] = atual

                if vizinho not in em_heap:
                    contador += 1
                    heapq.heappush(heap, (f, contador, vizinho))
                    em_heap.add(vizinho)

    grafo.nos_expandidos = nos_expandidos
    pbar.close()
    return None


def avaliar_algoritmo(nome_alg, funcao_busca, estado_objetivo, num_testes=10, movimentos_iniciais=30):
    total_nos_expandidos = 0
    total_movimentos = 0
    total_tempo = 0
    solucoes_encontradas = 0

    for i in range(num_testes):
        print(
            f"\n🧪 Teste {i+1}/{num_testes} - Gerando estado inicial com {movimentos_iniciais} movimentos aleatórios...")
        estado_inicial = gerar_estado_por_movimentos(movimentos_iniciais)
        grafo = Grafo()

        tempo_inicio = time.time()
        caminho = funcao_busca(grafo, estado_inicial, estado_objetivo)
        tempo_fim = time.time()
        duracao = tempo_fim - tempo_inicio

        if caminho:
            print(
                f"✅ Solução encontrada em {duracao:.4f}s com {len(caminho) - 1} movimentos.")
            solucoes_encontradas += 1
            total_movimentos += len(caminho) - 1
        else:
            print(f"❌ Nenhuma solução encontrada em {duracao:.4f}s.")

        total_tempo += duracao
        total_nos_expandidos += grafo.nos_expandidos
        print(f"🔧 Nós expandidos nesta execução: {grafo.nos_expandidos}")

        gc.collect()

    print(f"\n📊 🔍 Resultados finais para {nome_alg}:")
    print(f"✔️ Soluções encontradas: {solucoes_encontradas}/{num_testes}")
    print(
        f"📏 Média de movimentos: {total_movimentos/solucoes_encontradas if solucoes_encontradas else 0:.2f}")
    print(f"🌐 Média de nós expandidos: {total_nos_expandidos/num_testes:.2f}")
    print(f"⏱️ Média de tempo por execução (s): {total_tempo/num_testes:.4f}")


def bfs_otimizada(grafo, estado_inicial, estado_objetivo, limite_vertices_total=1000000):
    fila = deque([estado_inicial])
    fila_set = {estado_inicial}
    visitados = set()
    predecessores = {estado_inicial: None}
    nos_expandidos = 0

    grafo.adicionar_vertice(estado_inicial)

    barra = tqdm(total=limite_vertices_total,
                 desc="🔄 BFS Expandindo nós", unit="nó", ncols=80)

    while fila:
        atual = fila.popleft()
        fila_set.discard(atual)

        if atual in visitados:
            continue
        visitados.add(atual)
        nos_expandidos += 1
        barra.update(1)

        if atual == estado_objetivo:
            barra.close()
            caminho = []
            while atual:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            print(f"🔎 BFS - Nós expandidos: {nos_expandidos}")
            grafo.nos_expandidos = nos_expandidos
            return caminho

        for vizinho in atual.get_neighbors():
            if vizinho not in grafo.vertices:
                if len(grafo.vertices) >= limite_vertices_total:
                    continue
                grafo.adicionar_vertice(vizinho)
                grafo.adicionar_aresta(atual, vizinho)

            if vizinho not in visitados and vizinho not in fila_set:
                fila.append(vizinho)
                fila_set.add(vizinho)
                predecessores[vizinho] = atual

    barra.close()
    print(f"⚠️ BFS - Limite de nós atingido. Nós expandidos: {nos_expandidos}")
    grafo.nos_expandidos = nos_expandidos
    return None
