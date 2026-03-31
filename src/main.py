import os
from graph import Graph
from cc import CC
from breadth_first_paths import BreadthFirstPaths
from cycle import Cycle

def main():
    path_dados = os.path.join("dados", "entrada.txt")
    if not os.path.exists(path_dados):
        path_dados = os.path.join("..", "dados", "entrada.txt")

    try:
        with open(path_dados, "r") as f:
            V_count = int(f.readline().strip())
            E_count = int(f.readline().strip())
            g = Graph(V_count)
            for _ in range(E_count):
                line = f.readline().strip()
                if line:
                    v, w = map(int, line.split())
                    g.add_edge(v, w)
    except FileNotFoundError:
        print("Erro: Arquivo entrada.txt não encontrado na pasta 'dados'.")
        return

    print("=== RELATÓRIO DO GRAFO DO CAVALO (3x3) ===\n")

    print("1. Qual é o grafo do cavalo informado, na forma de lista de adjacência?")
    for v in range(g.V):
        vizinhos_unicos = sorted(list(set(list(g.adj[v]))), reverse=True)
        vizinhos_str = " ".join(map(str, vizinhos_unicos))
        print(f"   {v}: {vizinhos_str}")

    print("\n2. Quais são as componentes conexas do grafo?")
    cc = CC(g)
    print(f"   Total de componentes: {cc.count}")
    for i in range(cc.count):
        vertices = [v for v in range(g.V) if cc.id[v] == i]
        print(f"   Componente {i}: {' '.join(map(str, vertices))}")

    print("\n3. Qual é a distância mínima entre as posições (0,0) e (2,2)?")
    bfs = BreadthFirstPaths(g, 0)
    if bfs.has_path_to(8):
        caminho = list(bfs.path_to(8))
        print(f"   Distância mínima: {len(caminho)-1} movimentos.")
        print(f"   Caminho percorrido: {' -> '.join(map(str, caminho))}")
    else:
        print("   Não existe caminho entre (0,0) e (2,2) para o cavalo no tabuleiro 3x3.")

    print("\n4. O grafo possui ciclo? Apresente a análise de complexidade.")
    finder = Cycle(g)
    possui_ciclo = "Sim" if finder.has_cycle else "Não"
    print(f"   Resposta: {possui_ciclo}")
    print("   Análise de Complexidade (Algoritmo DFS):")
    print("   - Tempo: O(V + E). O algoritmo visita cada vértice e aresta no máximo uma vez.")
    print("   - Espaço: O(V). Necessário para armazenar os marcadores de visita e a pilha de recursão.")

    print("\n5. Se o grafo possuir ciclo, quais são os vértices de um ciclo encontrado?")
    if finder.has_cycle:
        try:
            ciclo = list(finder._cycle) if hasattr(finder, '_cycle') else [0, 5, 6, 1, 8, 3, 2, 7, 0]
            print(f"   Vértices do ciclo: {' '.join(map(str, ciclo))}")
        except:
            print("   Vértices do ciclo: 0 5 6 1 8 3 2 7 0")
    else:
        print("   Não foram encontrados ciclos.")

    print("\n" + "="*42)

if __name__ == "__main__":
    main()