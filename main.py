import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt

from grafos.ler_arquivo import carregar_grafo_de_arquivo
from grafos.algoritmo import bfs, dfs, dijkstra

def mostrar_resultados(grafo):
    resultados = []

    resultados.append("=== Grafo carregado ===")
    # Captura a saída de imprimeGrafo()
    import io
    import sys
    buffer = io.StringIO()
    sys.stdout = buffer
    grafo.imprimeGrafo()
    sys.stdout = sys.__stdout__
    resultados.append(buffer.getvalue())

    resultados.append("\n=== Busca em Largura (BFS) ===")
    resultados.append(str(bfs(grafo, 0)))

    resultados.append("\n=== Busca em Profundidade (DFS) ===")
    resultados.append(str(dfs(grafo, 0)))

    resultados.append("\n=== Dijkstra (a partir do vértice 0) ===")
    dist, caminhos = dijkstra(grafo, 0)
    for v, d in enumerate(dist):
        nome = grafo.labelVertice(v)
        resultados.append(f"{nome}: dist={d}, caminho={caminhos[nome]}")

    resultado_final = "\n".join(resultados)

    # Cria janela grande com Text widget
    popup = tk.Toplevel()
    popup.title("Resultados do Grafo")
    popup.geometry("1000x700")  # largura x altura

    text_box = tk.Text(popup, wrap="word", width=120, height=35)
    text_box.insert("1.0", resultado_final)
    text_box.config(state="disabled")
    text_box.pack(padx=10, pady=10, fill="both", expand=True)

    btn_close = tk.Button(popup, text="Fechar", command=popup.destroy)
    btn_close.pack(pady=5)

def visualizar_grafo(grafo):
    G = nx.DiGraph() if grafo.direcionado else nx.Graph()

    # Adiciona vértices
    for i, label in enumerate(grafo.rotulos):
        G.add_node(label)

    # Adiciona arestas com pesos
    for i in range(len(grafo.rotulos)):
        for v in grafo.retornarVizinhos(i):
            peso = grafo.pesoAresta(i, v)
            G.add_edge(grafo.labelVertice(i), grafo.labelVertice(v), weight=peso)

    # Layout automático e tamanho maior
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)  # seed para sempre ter mesma posição
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1500, font_size=12, font_weight="bold")
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10)
    plt.show()

def main():
    # Escolher se vai usar matriz ou lista
    usar_matriz = False
    grafo = carregar_grafo_de_arquivo("grafo.txt", usar_matriz=usar_matriz)

    root = tk.Tk()
    root.title("Painel do Grafo")
    root.geometry("400x200")  # tamanho inicial da janela principal

    btn_resultados = tk.Button(root, text="Mostrar Resultados", command=lambda: mostrar_resultados(grafo))
    btn_resultados.pack(pady=10, padx=20, fill="x")

    btn_visualizar = tk.Button(root, text="Visualizar Grafo", command=lambda: visualizar_grafo(grafo))
    btn_visualizar.pack(pady=10, padx=20, fill="x")

    btn_sair = tk.Button(root, text="Sair", command=root.destroy)
    btn_sair.pack(pady=10, padx=20, fill="x")

    root.mainloop()

if __name__ == "__main__":
    main()
