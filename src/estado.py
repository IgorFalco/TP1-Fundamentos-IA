class Estado:
    MOVES = {
        "left": -1, "right": 1, "up": -4, "down": 4
    }

    def __init__(self, board):
        # Inicializa um estado do jogo.
        self.board = tuple(board)  # Usa tupla para imutabilidade
        self.zero_index = self.board.index(0)  # Posição do espaço vazio

    def __eq__(self, other):
        # Dois estados são iguais se seus tabuleiros forem iguais
        return isinstance(other, Estado) and self.board == other.board

    def __hash__(self):
        # O hash é baseado no tabuleiro para permitir uso em conjuntos e dicionários
        return hash(self.board)

    def __repr__(self):
        # Representação do estado como string.
        return f"{self.board}"

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
            new_board = list(self.board)
            new_board[self.zero_index], new_board[new_index] = new_board[new_index], new_board[self.zero_index]
            neighbors.append(Estado(new_board))

        return neighbors
