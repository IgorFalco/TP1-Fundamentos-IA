# TP 1 - Fundamentos de IA
# Julia Machado, Igor Falco, Eduardo Fernandes

import random
from collections import deque
import heapq
from estado import Estado

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
        estado_objetivo = Estado([1, 2, 3, 4,
                                  5, 6, 7, 8,
                                  9, 10, 11, 12,
                                  13, 14, 15, 0])

    estado_atual = estado_objetivo
    caminho = [estado_atual]
    anterior = None

    for _ in range(n):
        vizinhos = estado_atual.get_neighbors()

        # evita desfazer o movimento anterior (opcional, pra evitar ciclos curtos)
        if anterior:
            vizinhos = [v for v in vizinhos if v != anterior]
        if not vizinhos:
            break  # sem mais movimentos possíveis

        proximo = random.choice(vizinhos)
        anterior = estado_atual
        estado_atual = proximo
        caminho.append(estado_atual)

    return estado_atual  # ou return caminho[-1] se preferir


#########   Tarefa 3   #########


def bfs_em_grafo(grafo, estado_inicial, estado_objetivo, limite_vertices_total=100000):
    fila = deque([estado_inicial])
    visitados = set()
    predecessores = {estado_inicial: None}

    while fila:
        atual = fila.popleft()
        visitados.add(atual)

        if atual == estado_objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
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

    return None


def dfs_em_grafo(grafo, estado_inicial, estado_objetivo, limite_profundidade=5000, limite_vertices_total=100000):
    pilha = [(estado_inicial, [estado_inicial])]
    visitados = set()

    while pilha:
        atual, caminho = pilha.pop()
        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == estado_objetivo:
            return caminho

        if len(caminho) >= limite_profundidade:
            continue

        for vizinho in reversed(atual.get_neighbors()):
            if vizinho not in grafo.vertices:
                if len(grafo.vertices) >= limite_vertices_total:
                    continue
                grafo.adicionar_vertice(vizinho)
                grafo.adicionar_aresta(atual, vizinho)

            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))

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


def a_estrela(grafo, estado_inicial, estado_objetivo, limite_vertices_total=100000):
    heap = []
    contador = 0
    heapq.heappush(heap, (0, contador, estado_inicial))
    g_score = {estado_inicial: 0}
    f_score = {estado_inicial: heuristica_distancia_manhattan(
        estado_inicial, estado_objetivo)}
    predecessores = {estado_inicial: None}
    visitados = set()

    while heap:
        _, _, atual = heapq.heappop(heap)

        if atual == estado_objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            return caminho

        visitados.add(atual)

        for vizinho in atual.get_neighbors():
            if vizinho not in grafo.vertices:
                if len(grafo.vertices) >= limite_vertices_total:
                    continue
                grafo.adicionar_vertice(vizinho)
                grafo.adicionar_aresta(atual, vizinho)

            if vizinho in visitados:
                continue

            tentativo_g = g_score[atual] + 1

            if tentativo_g < g_score.get(vizinho, float('inf')):
                predecessores[vizinho] = atual
                g_score[vizinho] = tentativo_g
                f = tentativo_g + \
                    heuristica_distancia_manhattan(vizinho, estado_objetivo)
                f_score[vizinho] = f
                contador += 1
                heapq.heappush(heap, (f, contador, vizinho))

    return None
