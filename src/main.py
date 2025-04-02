from funcoes import gerarTabuleiro, verificaSolvabilidade

def main():
    tabuleiro = gerarTabuleiro()
    print("Tabuleiro gerado:", tabuleiro)
    
    if verificaSolvabilidade(tabuleiro):
        print("✅ O tabuleiro é solucionável!")
    else:
        print("❌ O tabuleiro NÃO é solucionável!")

if __name__ == "__main__":
    main()
