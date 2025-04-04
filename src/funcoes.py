# TP 1 - Fundamentos de IA
# Julia Machado, Igor Falco, Eduardo Fernandes

import random
from collections import deque
from estado import Estado
from grafo import Grafo

#########   Tarefa 1   #########

def verificaSolvabilidade(tabuleiro):
    inversoes = 0
    
    for i in range(15):  # até o penúltimo elemento
        for j in range(i + 1, 16):
            if tabuleiro[i] > tabuleiro[j] and tabuleiro[i] != 0 and tabuleiro[j] != 0:
                inversoes += 1

    posicao_vazia = tabuleiro.index(0)
    linha_vazia_de_baixo = 4 - (posicao_vazia // 4)  # Conta de baixo pra cima

    # Verifica solvabilidade com base nas regras do jogo 15 (4x4)
    if (inversoes % 2 == 0 and linha_vazia_de_baixo % 2 == 1) or \
       (inversoes % 2 == 1 and linha_vazia_de_baixo % 2 == 0):
        return True
    else:
        return False

#########   Tarefa 2   #########

def gerarTabuleiro():
    tabuleiro = list(range(16))  # [0, 1, ..., 15]
    random.shuffle(tabuleiro)
    return tabuleiro

#########   Tarefa 3   #########

def bfs_em_grafo(grafo, estado_inicial, estado_objetivo):
    if estado_inicial not in grafo.vertices or estado_objetivo not in grafo.vertices:
        return None

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

        for vizinho in grafo.vertices.get(atual, []):
            if vizinho not in visitados and vizinho not in fila:
                fila.append(vizinho)
                predecessores[vizinho] = atual

    return None

def dfs_em_grafo(grafo, estado_inicial, estado_objetivo, limite_profundidade=5000):
    if estado_inicial not in grafo.vertices or estado_objetivo not in grafo.vertices:
        return None

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

        for vizinho in reversed(grafo.vertices.get(atual, [])):
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))

    return None
