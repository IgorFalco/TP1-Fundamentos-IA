class Estado:
    MOVES = {
        "left": -1, "right": 1, "up": -4, "down": 4
    }
    
    def __init__(self, tabuleiro):
        # Inicializa um estado do jogo.
        self.tabuleiro = tuple(tabuleiro)  # Usa tupla para imutabilidade
        self.zero_index = self.tabuleiro.index(0)  # Posição do espaço vazio

    def __eq__(self, other):
        # Dois estados são iguais se seus tabuleiros forem iguais
        return isinstance(other, Estado) and self.tabuleiro == other.tabuleiro

    def __hash__(self):
        # O hash é baseado no tabuleiro para permitir uso em conjuntos e dicionários
        return hash(self.tabuleiro)

    def __repr__(self):
        # Representação do estado como string.
        return f"{self.tabuleiro}"

    def get_neighbors(self):
        # Gera os estados vizinhos possíveis a partir do estado atual.
        neighbors = []

        for move, delta in self.MOVES.items():
            new_index = self.zero_index + delta

            # Regras para impedir movimentos inválidos
            if move == "left" and self.zero_index % 4 == 0:
                continue
            if move == "right" and self.zero_index % 4 == 3:
                continue
            if move == "up" and self.zero_index < 4:
                continue
            if move == "down" and self.zero_index >= 12:
                continue

            # Criar novo estado trocando os elementos
            new_tabuleiro = list(self.tabuleiro)
            new_tabuleiro[self.zero_index], new_tabuleiro[new_index] = new_tabuleiro[new_index], new_tabuleiro[self.zero_index]
            neighbors.append(Estado(new_tabuleiro))

        return neighbors
