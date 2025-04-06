from collections import deque


class Grafo:
    def __init__(self):
        # Inicializa um grafo como uma lista de adjacência vazia
        self.vertices = {}

    def copia(self):
        novo = Grafo()
        for estado, vizinhos in self.vertices.items():
            novo.vertices[estado] = list(vizinhos)
        return novo

    def adicionar_vertice(self, estado):
        # Adiciona um estado ao grafo se ainda não estiver presente
        if estado not in self.vertices:
            self.vertices[estado] = []

    def adicionar_aresta(self, estado1, estado2):
        # Cria uma aresta entre dois estados.
        self.adicionar_vertice(estado1)
        self.adicionar_vertice(estado2)

        if estado2 not in self.vertices[estado1]:
            self.vertices[estado1].append(estado2)

        if estado1 not in self.vertices[estado2]:
            self.vertices[estado2].append(estado1)

    def construir_grafo(self, estado_inicial, limite=1000):

        fila = deque([estado_inicial])
        self.adicionar_vertice(estado_inicial)

        while fila and len(self.vertices) < limite:
            estado_atual = fila.popleft()

            for vizinho in estado_atual.get_neighbors():
                if vizinho not in self.vertices:
                    self.adicionar_vertice(vizinho)
                    fila.append(vizinho)
                self.adicionar_aresta(estado_atual, vizinho)

    def __repr__(self):
        # Representação do grafo
        return f"Grafo({len(self.vertices)} estados armazenados)"

    def exibir_grafo(self):
        # Exibe o grafo com os estados e seus vizinhos
        for estado, vizinhos in self.vertices.items():
            print(f"Estado: {estado}")
            # Exibe a quantidade de vizinhos
            print(f"  Número de vizinhos: {len(vizinhos)}")
            print("  Vizinhos:")
            for vizinho in vizinhos:
                # Cada vizinho aparece em uma linha separada
                print(f"    {vizinho}")
            print("-" * 40)
