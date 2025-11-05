import os, sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from algorithms.a_star import GraphSearchAlgorithms
from algorithms.bfs import bfs
from algorithms.dfs import dfs


def build_test_data():
    data = [
        {"id": 0, "name": "SaborExpress",     "x": 0.0, "y": 0.0},
        {"id": 1, "name": "Cliente A", "x": 3.0, "y": 0.2},
        {"id": 2, "name": "Cliente B", "x": 4.0, "y": 2.0},
        {"id": 3, "name": "Cliente C", "x": 6.0, "y": 2.0},
        {"id": 4, "name": "Cliente D", "x": 2.5, "y": -1.0},
    ]
    locations_df = pd.DataFrame(data).set_index("id")
    distance_matrix = np.array([
        [0.0, 2.0, 4.0, 7.0, 3.5],
        [2.0, 0.0, 2.5, 5.0, 2.0],
        [4.0, 2.5, 0.0, 2.0, 5.5],
        [7.0, 5.0, 2.0, 0.0, 3.0],
        [3.5, 2.0, 5.5, 3.0, 0.0],
    ])
    return locations_df, distance_matrix


def plot_path(locations_df: pd.DataFrame, path: list, title: str, outfile: str):
    """
    Plota os nós (com rótulos) e liga apenas as arestas da rota `path`.
    Um gráfico por figura, sem definir cores explicitamente.
    """
    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    plt.figure()
    # scatter dos nós
    for node_id, row in locations_df.iterrows():
        plt.scatter(row["x"], row["y"])
        # rótulo com id e nome
        plt.annotate(f'{node_id}:{row["name"]}',
                     (row["x"], row["y"]),
                     xytext=(5, 5),
                     textcoords="offset points")
    # desenha o caminho (segmentos consecutivos)
    if path and len(path) > 1:
        xs = [locations_df.loc[n, "x"] for n in path]
        ys = [locations_df.loc[n, "y"] for n in path]
        # linha contínua para a rota
        plt.plot(xs, ys, linewidth=2)
        # marca ordem de visita (0,1,2,...) perto de cada ponto da rota
        for idx, n in enumerate(path):
            x = locations_df.loc[n, "x"]
            y = locations_df.loc[n, "y"]
            plt.annotate(str(idx), (x, y), xytext=(0, -12), textcoords="offset points")

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.savefig(outfile, dpi=160, bbox_inches="tight")
    plt.close()


def plot_costs_bar(algorithms: list, costs: list, outfile: str):
    """
    Gráfico de barras simples comparando custos (um gráfico por figura).
    """
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    plt.figure()
    plt.bar(algorithms, costs)
    plt.title("Comparação de custos por algoritmo (km)")
    plt.ylabel("km")
    plt.tight_layout()
    plt.savefig(outfile, dpi=160, bbox_inches="tight")
    plt.close()


def main():
    # 1) cenário
    locations_df, distance_matrix = build_test_data()
    start_node = 0
    goal_node = 3

    print("=== Cenário de teste ===")
    print(f"Ir do nó {start_node} -> {goal_node}\n")

    # 2) A*
    gs = GraphSearchAlgorithms(locations_df, distance_matrix)
    a_path, a_cost = gs.a_star(start_node, goal_node)
    print("[A*]")
    print("Caminho:", a_path)
    print("Custo (km):", round(a_cost, 2))
    print()

    # 3) BFS
    bfs_path, bfs_cost = bfs(locations_df, distance_matrix, start_node, goal_node)
    print("[BFS]")
    print("Caminho:", bfs_path)
    print("Custo acumulado (km):", round(bfs_cost, 2))
    print("OBS: BFS não é focado em custo mínimo ponderado; serve como baseline.")
    print()

    # 4) DFS
    dfs_path, dfs_cost = dfs(locations_df, distance_matrix, start_node, goal_node)
    print("[DFS]")
    print("Caminho:", dfs_path)
    print("Custo acumulado (km):", round(dfs_cost, 2))
    print("OBS: DFS encontra um caminho válido, mas não otimizado.")
    print()

    # 5) Comparação (prints)
    print("=== Comparação ===")
    print(f"A*:  custo {round(a_cost,2)} km, rota {a_path}")
    print(f"BFS: custo {round(bfs_cost,2)} km, rota {bfs_path}")
    print(f"DFS: custo {round(dfs_cost,2)} km, rota {dfs_path}")

    # 6) Salva CSV de comparação (opcional, bom pro README)
    os.makedirs("docs", exist_ok=True)
    comparacao = pd.DataFrame([
        {"algoritmo": "A*",  "rota": str(a_path),   "custo_km": round(a_cost, 2)},
        {"algoritmo": "BFS", "rota": str(bfs_path), "custo_km": round(bfs_cost, 2)},
        {"algoritmo": "DFS", "rota": str(dfs_path), "custo_km": round(dfs_cost, 2)},
    ])
    comparacao.to_csv("docs/resultado_buscas.csv", index=False)
    print("Salvo em docs/resultado_buscas.csv")

    # 7) Gera imagens das rotas
    plot_path(locations_df, a_path,  "Rota A*",  "docs/path_astar.png")
    plot_path(locations_df, bfs_path, "Rota BFS", "docs/path_bfs.png")
    plot_path(locations_df, dfs_path, "Rota DFS", "docs/path_dfs.png")
    print("Imagens de rotas salvas em docs/path_astar.png, docs/path_bfs.png, docs/path_dfs.png")

    # 8) Gera imagem do comparativo de custos
    plot_costs_bar(["A*", "BFS", "DFS"], [a_cost, bfs_cost, dfs_cost], "docs/buscas_comparacao.png")
    print("Imagem de custos salva em docs/buscas_comparacao.png")


if __name__ == "__main__":
    main()
