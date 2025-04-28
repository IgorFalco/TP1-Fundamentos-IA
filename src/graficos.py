import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def gerar_graficos(caminhos_csv, saida_pasta="graficos"):
    """
    caminhos_csv: lista de caminhos para os arquivos .csv de resultados
    saida_pasta: pasta onde os gráficos serão salvos
    """

    # Lê todos os CSVs e junta num único dataframe
    dfs = []
    for caminho in caminhos_csv:
        df = pd.read_csv(caminho)
        dfs.append(df)

    resultados = pd.concat(dfs, ignore_index=True)

    # Cria pasta de saída se não existir
    os.makedirs(saida_pasta, exist_ok=True)

    # Configurações de estilo
    sns.set(style="whitegrid")
    palette = sns.color_palette("Set2")

    def adicionar_linha_vertical(x_valor):
        """Adiciona uma linha vertical no gráfico."""
        plt.axvline(x=x_valor, color='red', linestyle='--',
                    label=f'Marcação em {x_valor}')
        plt.legend()

    # --------- Gráfico 1: Tempo Médio ---------
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=resultados, x="Movimentos_Iniciais",
                 y="Media_Tempo_Segundos", hue="Algoritmo", marker="o", palette=palette)
    adicionar_linha_vertical(50)  # <<< adiciona linha vermelha no 50
    plt.title("Tempo Médio de Execução")
    plt.xlabel("Movimentos Iniciais")
    plt.ylabel("Tempo Médio (s)")
    plt.tight_layout()
    plt.savefig(f"{saida_pasta}/tempo_medio.png")
    plt.close()

    # --------- Gráfico 2: Nós Expandidos ---------
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=resultados, x="Movimentos_Iniciais",
                 y="Media_Nos_Expandidos", hue="Algoritmo", marker="o", palette=palette)
    adicionar_linha_vertical(50)  # <<< adiciona linha vermelha no 50
    plt.title("Nós Expandidos")
    plt.xlabel("Movimentos Iniciais")
    plt.ylabel("Média de Nós Expandidos")
    plt.tight_layout()
    plt.savefig(f"{saida_pasta}/nos_expandidos.png")
    plt.close()

    # --------- Gráfico 3: Movimentos na Solução ---------
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=resultados, x="Movimentos_Iniciais",
                 y="Media_Movimentos", hue="Algoritmo", marker="o", palette=palette)
    adicionar_linha_vertical(50)  # <<< adiciona linha vermelha no 50
    plt.title("Movimentos na Solução")
    plt.xlabel("Movimentos Iniciais")
    plt.ylabel("Média de Movimentos para Solução")
    plt.tight_layout()
    plt.savefig(f"{saida_pasta}/movimentos_solucao.png")
    plt.close()

    print(f"✅ Gráficos salvos na pasta '{saida_pasta}'!")


if __name__ == "__main__":
    caminhos = [
        "src/bfs_resultados.csv",
        "src/dfs_resultados.csv",
        "src/a_estrela_resultados.csv"
    ]

    gerar_graficos(caminhos)
