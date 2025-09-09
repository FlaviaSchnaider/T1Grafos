from collections import deque
import heapq

def bfs(grafo, origem: int):
    visitados = [False] * len(grafo.rotulos)
    ordem = []
    fila = deque([origem])
    visitados[origem] = True

    while fila:
        u = fila.popleft()
        ordem.append(grafo.labelVertice(u))
        for v in grafo.retornarVizinhos(u):
            if not visitados[v]:
                visitados[v] = True
                fila.append(v)
    return ordem


def dfs(grafo, origem: int):
    visitados = [False] * len(grafo.rotulos)
    ordem = []

    def explorar(u):
        visitados[u] = True
        ordem.append(grafo.labelVertice(u))
        for v in grafo.retornarVizinhos(u):
            if not visitados[v]:
                explorar(v)

    explorar(origem)
    return ordem


def dijkstra(grafo, origem: int):
    n = len(grafo.rotulos)
    dist = [float("inf")] * n
    pai = [None] * n
    dist[origem] = 0
    pq = [(0, origem)]  # distancia , vertice)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v in grafo.retornarVizinhos(u):
            peso = grafo.pesoAresta(u, v)
            if peso is None:
                continue
            if dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                pai[v] = u
                heapq.heappush(pq, (dist[v], v))

    # reconstroi caminhos
    caminhos = {}
    for v in range(n):
        if dist[v] == float("inf"):
            caminhos[grafo.labelVertice(v)] = None
        else:
            caminho = []
            atual = v
            while atual is not None:
                caminho.append(grafo.labelVertice(atual))
                atual = pai[atual]
            caminhos[grafo.labelVertice(v)] = list(reversed(caminho))

    return dist, caminhos
