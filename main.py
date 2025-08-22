# This is a sample Python script.
# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from grafos import GrafoMatriz, GrafoLista

def exemplo_matriz():
    print("=== GrafoMatriz (não direcionado, ponderado) ===")
    gm = GrafoMatriz(direcionado=False, ponderado=True)
    gm.inserirVertice("A")
    gm.inserirVertice("B")
    gm.inserirVertice("C")
    gm.inserirAresta(0, 1, 2.5)
    gm.inserirAresta(1, 2, 3)
    gm.imprimeGrafo()
    print("vizinhos(1):", gm.retornarVizinhos(1))
    print("peso(1,2):", gm.pesoAresta(1, 2))
    gm.removerVertice(1)
    gm.imprimeGrafo()

def exemplo_lista():
    print("\n=== GrafoLista (direcionado, não ponderado) ===")
    gl = GrafoLista(direcionado=True, ponderado=False)
    gl.inserirVertice("A")
    gl.inserirVertice("B")
    gl.inserirVertice("C")
    gl.inserirAresta(0, 1)
    gl.inserirAresta(1, 2)
    gl.inserirAresta(2, 0)
    gl.imprimeGrafo()
    print("existe(2,0)?", gl.existeAresta(2, 0))
    print("peso(1,2):", gl.pesoAresta(1, 2))
    print("vizinhos(1):", gl.retornarVizinhos(1))
    gl.removerAresta(2, 0)
    gl.imprimeGrafo()
    gl.removerVertice(1)
    gl.imprimeGrafo()

if __name__ == "__main__":
    exemplo_matriz()
    exemplo_lista()