from typing import List, Optional
from .base import Grafos

class GrafoMatriz(Grafos):
    """
    Implementação usando matriz de adjacência.
    - Sem aresta: None
    - Com aresta: float (peso)
    """

    def __init__(self, direcionado: bool, ponderado: bool):
        super().__init__(direcionado, ponderado)
        self.matriz: List[List[Optional[float]]] = []

    def inserirVertice(self, label: str) -> bool:
        if label in self.rotulos:
            return False  # rótulo repetido (opcional)
        self.rotulos.append(label)
        n = len(self.rotulos)
        # Expande linhas existentes
        for linha in self.matriz:
            if len(linha) < n:
                linha.append(None)
        # Adiciona nova linha
        self.matriz.append([None] * n)
        return True

    def removerVertice(self, indice: int) -> bool:
        if not self._indices_validos(indice):
            return False
        self.rotulos.pop(indice)
        self.matriz.pop(indice)
        for i in range(len(self.matriz)):
            self.matriz[i].pop(indice)
        return True

    def imprimeGrafo(self) -> None:
        n = len(self.rotulos)
        if n == 0:
            print("(grafo vazio)")
            return
        header = ["   "] + [f"{i:>3}" for i in range(n)]
        print(" ".join(header))
        for i in range(n):
            linha_fmt = [f"{i:>3}"]
            for j in range(n):
                val = self.matriz[i][j]
                if val is None:
                    linha_fmt.append(f"{'-':>3}")
                else:
                    linha_fmt.append(f"{int(val) if float(val).is_integer() else val:>3}")
            print(" ".join(linha_fmt))

    def inserirAresta(self, origem: int, destino: int, peso: float = 1) -> bool:
        if not self._indices_validos(origem, destino):
            return False
        w = self._peso_validado(peso)
        self.matriz[origem][destino] = w
        if not self.direcionado:
            self.matriz[destino][origem] = w
        return True

    def removerAresta(self, origem: int, destino: int) -> bool:
        if not self._indices_validos(origem, destino):
            return False
        if self.matriz[origem][destino] is None:
            return False
        self.matriz[origem][destino] = None
        if not self.direcionado:
            self.matriz[destino][origem] = None
        return True

    def existeAresta(self, origem: int, destino: int) -> bool:
        if not self._indices_validos(origem, destino):
            return False
        return self.matriz[origem][destino] is not None

    def pesoAresta(self, origem: int, destino: int) -> Optional[float]:
        if not self._indices_validos(origem, destino):
            return None
        return self.matriz[origem][destino]

    def retornarVizinhos(self, vertice: int) -> List[int]:
        if not self._indices_validos(vertice):
            return []
        return [j for j, val in enumerate(self.matriz[vertice]) if val is not None]