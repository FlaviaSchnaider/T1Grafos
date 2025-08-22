# Trabalho 1 - Grafos
#### Professor: Rodrigo Lyra
#### Alunos: Flávia Schnaider, Gregori Maciel, Murilo Francio


###  Descrição
Este trabalho tem como objetivo implementar a estrutura básica de grafos, permitindo representações em matriz de adjacência e lista de adjacência.
A implementação foi pensada de forma genérica, contemplando grafos direcionados/não direcionados e ponderados/não ponderados.

### Estrutura do Projeto
**O projeto é composto por:**
- Classe Grafos (abstrata/base):
  - Construtor recebe:
    -   Tipo do grafo (direcionado ou não)
    - Se é ponderado ou não
  - Define as operações básicas de manipulação de vértices e arestas. 

- Classe GrafoMatriz:
  - Representa o grafo utilizando matriz de adjacência.

- Classe GrafoLista:
    - Representa o grafo utilizando lista de adjacência, com estrutura auxiliar Aresta.

### Funcionalidades Implementadas
#### Operações com Vértices
- bool inserirVertice(string label); → Insere um novo vértice.
- bool removerVertice(int indice); → Remove um vértice e suas arestas associadas.
- string labelVertice(int indice); → Retorna o nome de um vértice.

#### Operações com Arestas
- bool inserirAresta(int origem, int destino, float peso = 1);
    - Considera se o grafo é ponderado.
    - Em grafos não direcionados, adiciona a ligação de retorno.

- bool removerAresta(int origem, int destino); → Remove a aresta (e retorno, se não direcionado).
- bool existeAresta(int origem, int destino); → Verifica se a aresta existe.
- float pesoAresta(int origem, int destino); → Retorna o peso da aresta.

#### Outras Operações
- vector<int> retornarVizinhos(int vertice); → Retorna os vizinhos de um vértice.
- void imprimeGrafo(); → Exibe o grafo no console de forma legível.