from collections import deque

class Grafo:
    def __init__(self):
        self.vertices = {}  # estado: set(vizinhos)
        self.nos_expandidos = 0

    def copia(self):
        novo = Grafo()
        for estado, vizinhos in self.vertices.items():
            novo.vertices[estado] = set(vizinhos)
        return novo

    def adicionar_vertice(self, estado):
        if estado not in self.vertices:
            self.vertices[estado] = set()

    def adicionar_aresta(self, estado1, estado2):
        self.adicionar_vertice(estado1)
        self.adicionar_vertice(estado2)
        self.vertices[estado1].add(estado2)
        self.vertices[estado2].add(estado1)

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
        return f"Grafo({len(self.vertices)} estados armazenados)"

    def exibir_grafo(self):
        for estado, vizinhos in self.vertices.items():
            print(f"Estado: {estado}")
            print(f"  Número de vizinhos: {len(vizinhos)}")
            print("  Vizinhos:")
            for vizinho in vizinhos:
                print(f"    {vizinho}")
            print("-" * 40)
