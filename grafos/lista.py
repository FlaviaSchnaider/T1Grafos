from dataclasses import dataclass
from typing import List, Optional
from .base import Grafos

@dataclass
class Aresta:
    destino: int
    peso: float

class GrafoLista(Grafos):
    """
    Implementação usando lista de adjacência.
    - Para cada vértice i, adj[i] é uma lista de Aresta(destino, peso).
    """

    def __init__(self, direcionado: bool, ponderado: bool):
        super().__init__(direcionado, ponderado)
        self.adj: List[List[Aresta]] = []

    def inserirVertice(self, label: str) -> bool:
        if label in self.rotulos:
            return False
        self.rotulos.append(label)
        self.adj.append([])
        return True

    def removerVertice(self, indice: int) -> bool:
        if not self._indices_validos(indice):
            return False

        # Remove arestas que chegam ao vértice 'indice'
        for u in range(len(self.adj)):
            if u == indice:
                continue
            self.adj[u] = [e for e in self.adj[u] if e.destino != indice]
            # Ajusta índices de destino maiores que 'indice'
            for e in self.adj[u]:
                if e.destino > indice:
                    e.destino -= 1

        # Remove as arestas que saem do vértice e sua lista
        self.adj.pop(indice)
        self.rotulos.pop(indice)
        return True

    def imprimeGrafo(self) -> None:
        n = len(self.rotulos)
        if n == 0:
            print("(grafo vazio)")
            return
        for i, lista in enumerate(self.adj):
            base = f"{i} ({self.rotulos[i]}):"
            if not lista:
                print(base + " ∅")
                continue
            partes = []
            for e in lista:
                if self.ponderado:
                    partes.append(
                        f" -> {e.destino}({self.rotulos[e.destino]}|{int(e.peso) if float(e.peso).is_integer() else e.peso})"
                    )
                else:
                    partes.append(f" -> {e.destino}({self.rotulos[e.destino]})")
            print(base + "".join(partes))

    def inserirAresta(self, origem: int, destino: int, peso: float = 1) -> bool:
        if not self._indices_validos(origem, destino):
            return False
        w = self._peso_validado(peso)

        def upsert(u: int, v: int):
            for e in self.adj[u]:
                if e.destino == v:
                    e.peso = w
                    return
            self.adj[u].append(Aresta(v, w))

        upsert(origem, destino)
        if not self.direcionado:
            upsert(destino, origem)
        return True

    def removerAresta(self, origem: int, destino: int) -> bool:
        if not self._indices_validos(origem, destino):
            return False
        antes = len(self.adj[origem])
        self.adj[origem] = [e for e in self.adj[origem] if e.destino != destino]
        removida = len(self.adj[origem]) < antes
        if not self.direcionado:
            antes2 = len(self.adj[destino])
            self.adj[destino] = [e for e in self.adj[destino] if e.destino != origem]
            removida = removida or (len(self.adj[destino]) < antes2)
        return removida

    def existeAresta(self, origem: int, destino: int) -> bool:
        if not self._indices_validos(origem, destino):
            return False
        return any(e.destino == destino for e in self.adj[origem])

    def pesoAresta(self, origem: int, destino: int) -> Optional[float]:
        if not self._indices_validos(origem, destino):
            return None
        for e in self.adj[origem]:
            if e.destino == destino:
                return e.peso
        return None

    def retornarVizinhos(self, vertice: int) -> List[int]:
        if not self._indices_validos(vertice):
            return []
        return [e.destino for e in self.adj[vertice]]