from .lista import GrafoLista
from .matriz import GrafoMatriz

def carregar_grafo_de_arquivo(caminho: str, usar_matriz: bool = False):
    with open(caminho, "r") as f:
        linhas = [linha.strip() for linha in f if linha.strip()]
    
    # Primeira linha
    V, A, D, P = map(int, linhas[0].split())
    direcionado = bool(D)
    ponderado = bool(P)

    grafo = GrafoMatriz(direcionado, ponderado) if usar_matriz else GrafoLista(direcionado, ponderado)

    # Cria vértices 
    for i in range(V):
        grafo.inserirVertice(str(i))

    # Le arestas
    for linha in linhas[1:]:
        dados = linha.split()
        origem, destino = int(dados[0]), int(dados[1])
        if ponderado:
            peso = float(dados[2])
            grafo.inserirAresta(origem, destino, peso)
        else:
            grafo.inserirAresta(origem, destino)
    
    return grafo
