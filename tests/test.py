import unittest
from src.funcoes import verificaSolvabilidade, gerarTabuleiro

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
            self.assertEqual(sorted(tabuleiro), list(range(16)), f"Tabuleiro inválido: {tabuleiro}")
            self.assertEqual(len(set(tabuleiro)), 16, f"Tabuleiro contém números repetidos: {tabuleiro}")

if __name__ == '__main__':
    unittest.main()
