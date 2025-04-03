from src.funcoes import verificaSolvabilidade, gerarTabuleiro, busca_em_largura, busca_em_profundidade
from src.estado import Estado
from src.grafo import Grafo
import unittest
import random


class TestJogoDos15(unittest.TestCase):

    def test_tabuleiro_solvavel(self):
        tabuleiro = [1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 10, 11, 12,
                     13, 14, 0, 15]  # Tabuleiro solvável
        self.assertTrue(verificaSolvabilidade(tabuleiro))

    def test_tabuleiro_nao_solvavel(self):
        tabuleiro = [1, 2, 3, 4,
                     5, 6, 7, 8,
                     9, 10, 11, 12,
                     13, 15, 14, 0]  # Tabuleiro não solucionável
        self.assertFalse(verificaSolvabilidade(tabuleiro))

    def test_gerar_tabuleiro(self):
        for _ in range(10):  # Testa 10 tabuleiros gerados aleatoriamente
            tabuleiro = gerarTabuleiro()
            self.assertEqual(sorted(tabuleiro), list(range(16)),
                             f"Tabuleiro inválido: {tabuleiro}")
            self.assertEqual(len(set(tabuleiro)), 16,
                             f"Tabuleiro contém números repetidos: {tabuleiro}")


class TestEstado(unittest.TestCase):

    def test_get_neighbors(self):
        estado = Estado([1, 2, 3, 4,
                         5, 6, 7, 8,
                         9, 10, 11, 12,
                         13, 14, 0, 15])  # Espaço vazio na posição 14

        vizinhos = estado.get_neighbors()
        self.assertEqual(len(vizinhos), 3)  # Deve ter 3 vizinhos possíveis

    def test_estado_repr(self):
        estado = Estado([1, 2, 3, 4,
                         5, 6, 7, 8,
                         9, 10, 11, 12,
                         13, 14, 0, 15])

        self.assertEqual(
            repr(estado), "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15)")


class TestGrafo(unittest.TestCase):

    def test_adicionar_vertice(self):
        grafo = Grafo()
        estado = Estado([1, 2, 3, 4,
                         5, 6, 7, 8,
                         9, 10, 11, 12,
                         13, 14, 0, 15])

        grafo.adicionar_vertice(estado)
        self.assertIn(estado, grafo.vertices)

    def test_adicionar_aresta(self):
        grafo = Grafo()
        estado1 = Estado([1, 2, 3, 4,
                          5, 6, 7, 8,
                          9, 10, 11, 12,
                          13, 14, 0, 15])

        estado2 = Estado([1, 2, 3, 4,
                          5, 6, 7, 8,
                          9, 10, 11, 12,
                          13, 14, 15, 0])

        grafo.adicionar_aresta(estado1, estado2)
        self.assertIn(estado2, grafo.vertices[estado1])
        self.assertIn(estado1, grafo.vertices[estado2])

    def test_construir_grafo(self):
        grafo = Grafo()
        estado_inicial = Estado([1, 2, 3, 4,
                                 5, 6, 7, 8,
                                 9, 10, 11, 12,
                                 13, 14, 0, 15])

        grafo.construir_grafo(estado_inicial, limite=5)
        self.assertGreaterEqual(len(grafo.vertices), 5)

    def test_limite_vizinhos(self):
        grafo = Grafo()
        estado_inicial = Estado(random.sample(range(16), 16))
        grafo.adicionar_vertice(estado_inicial)

        fila = [estado_inicial]
        visitados = set()

        while fila and len(grafo.vertices) < 1000:
            estado_atual = fila.pop(0)
            visitados.add(estado_atual)

            for vizinho in estado_atual.get_neighbors():
                if vizinho not in visitados and vizinho not in grafo.vertices:
                    grafo.adicionar_aresta(estado_atual, vizinho)
                    fila.append(vizinho)

        for estado, vizinhos in grafo.vertices.items():
            self.assertLessEqual(len(vizinhos), 4)
            if estado != estado_inicial:
                self.assertGreaterEqual(len(vizinhos), 1)


class TestBuscaEmLargura(unittest.TestCase):

    def test_bfs_encontra_solucao_simples(self):
        estado_inicial = Estado([1, 2, 3, 4,
                                 5, 6, 7, 8,
                                 9, 10, 11, 12,
                                 13, 14, 0, 15])

        estado_objetivo = Estado([1, 2, 3, 4,
                                  5, 6, 7, 8,
                                  9, 10, 11, 12,
                                  13, 14, 15, 0])

        caminho = busca_em_largura(estado_inicial, estado_objetivo)

        self.assertIsNotNone(caminho)
        self.assertEqual(caminho[-1], estado_objetivo)
        self.assertEqual(len(caminho) - 1, 1)  # 1 movimento até o objetivo

class TestBuscaEmProfundidade(unittest.TestCase):

    def test_dfs_encontra_solucao_simples(self):
        estado_inicial = Estado([1, 2, 3, 4,
                                 5, 6, 7, 8,
                                 9, 10, 11, 12,
                                 13, 14, 0, 15])  # apenas 1 movimento do objetivo

        estado_objetivo = Estado([1, 2, 3, 4,
                                  5, 6, 7, 8,
                                  9, 10, 11, 12,
                                  13, 14, 15, 0])

        caminho = busca_em_profundidade(estado_inicial, estado_objetivo)

        self.assertIsNotNone(caminho)
        self.assertEqual(caminho[-1], estado_objetivo)
        self.assertEqual(len(caminho) - 1, 1)  # Apenas 1 movimento até o objetivo


if __name__ == '__main__':
    unittest.main()
