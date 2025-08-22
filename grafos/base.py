from typing import List, Optional

class Grafos:
    """
    Classe base para grafos.
    - direcionado: se True, arestas têm direção (u -> v)
    - ponderado: se True, arestas possuem pesos; caso False, peso padrão = 1
    """

    def __init__(self, direcionado: bool, ponderado: bool):
        self.direcionado = direcionado
        self.ponderado = ponderado
        self.rotulos: List[str] = []

    def labelVertice(self, indice: int) -> Optional[str]:
        if 0 <= indice < len(self.rotulos):
            return self.rotulos[indice]
        return None

    # Utilidades compartilhadas
    def _peso_validado(self, peso: float) -> float:
        """Se não ponderado, sempre retorna 1."""
        return float(peso if self.ponderado else 1)

    def _indices_validos(self, *indices: int) -> bool:
        n = len(self.rotulos)
        return all(0 <= i < n for i in indices)