# TP 1 - Fundamentos de IA
# Julia Machado, Igor Falco, Eduardo Fernandes


#########   Tarefa 1   #########

def verificaSolvabilidade(tabuleiro):
    inversoes = 0
    posicaoVazia = -1

    for i in range(15): # Percorre até o penúltimo elemento
        for j in range(i+1, 16): # Compara com os elementos à frente
            
            if tabuleiro[i] > tabuleiro[j] and tabuleiro[i] != 0 and tabuleiro[j] != 0:
                inversoes+= 1
    
    # Encontra a posição do número 0 (espaço vazio)
    posicaoVazia = tabuleiro.index(0)

    if posicaoVazia != -1:
        linhaVazia = posicaoVazia//4  # Linha em que está o espaço vazio

    # Verifica se é solucionável
    if (inversoes%2 == 0 and linhaVazia%2 != 0) or (inversoes%2 != 0 and linhaVazia%2==0):
        return True
    else:
        return False
    


## teste
tabuleiro = [1, 2, 3, 4,
             5, 6, 7, 8,
             9, 10, 11, 12,
             13, 14, 0, 15]
tabuleiro_nao_solvavel = [1, 2, 3, 4,
                           5, 6, 7, 8,
                           9, 10, 11, 12,
                           13, 15, 14, 0] 
print(verificaSolvabilidade(tabuleiro))
print(verificaSolvabilidade(tabuleiro_nao_solvavel))
##


#########   Tarefa 2   #########