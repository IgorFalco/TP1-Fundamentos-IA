# TP 1 - Fundamentos de IA
# Julia Machado, Igor Falco, Eduardo Fernandes

import random
from collections import deque

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
