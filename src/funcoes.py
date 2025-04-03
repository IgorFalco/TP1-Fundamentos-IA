# TP 1 - Fundamentos de IA
# Julia Machado, Igor Falco, Eduardo Fernandes

import random
from collections import deque
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
    tabuleiro = list(range(16))  # Cria uma lista [0, 1, 2, ..., 15]
    random.shuffle(tabuleiro)  # Embaralha os números
    return tabuleiro

#########   Tarefa 3   #########

def busca_em_largura(estado_inicial, estado_objetivo):
    fila = deque([estado_inicial])
    visitados = set()
    predecessores = {estado_inicial: None}

    while fila:
        atual = fila.popleft()
        visitados.add(atual)

        if atual.board == estado_objetivo.board:
            # Reconstrói o caminho da solução
            caminho = []
            while atual:
                caminho.append(atual)
                atual = predecessores[atual]
            caminho.reverse()
            return caminho  # Lista de estados do inicial ao objetivo

        for vizinho in atual.get_neighbors():
            if vizinho not in visitados and vizinho not in fila:
                fila.append(vizinho)
                predecessores[vizinho] = atual

    return None  # Não encontrou solução

def busca_em_profundidade(estado_inicial, estado_objetivo, limite_profundidade=50):
    pilha = [(estado_inicial, [estado_inicial])]
    visitados = set()

    while pilha:
        atual, caminho = pilha.pop()
        if atual in visitados:
            continue
        visitados.add(atual)

        if atual.board == estado_objetivo.board:
            return caminho

        if len(caminho) >= limite_profundidade:
            continue

        for vizinho in reversed(atual.get_neighbors()):
            if vizinho not in visitados:
                pilha.append((vizinho, caminho + [vizinho]))

    return None  # Não encontrou solução dentro do limite
