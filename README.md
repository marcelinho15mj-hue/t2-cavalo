# Trabalho Prático 2 - Unidade 2

Disciplina: Resolução de Problemas com Grafos
Professor: Ricardo Carubbi


# Link do Video: https://drive.google.com/file/d/1UqqVGpLN1QxnyHj0Mq3achoCjw1Yayvz/view?usp=sharing

## Alunos

* Bernardo Pinheiro 
* Marcelo Kalsovik Junior
* Guilherme Abrunheiro De Souza

## Descrição

Este projeto consiste na modelagem e análise de um tabuleiro de xadrez 3x3 utilizando a Teoria dos Grafos. O objetivo é aplicar algoritmos clássicos para entender a movimentação e a conectividade de um cavalo em um espaço reduzido.

Vértices: Cada uma das 9 casas do tabuleiro (0 a 8).

Arestas: Representam um movimento válido do cavalo (salto em "L") entre duas casas.

O projeto utiliza a biblioteca algs4 para processar componentes conexas, caminhos mínimos e detecção de ciclos.

## Mapeamento dos Estados

Mapeamento do Tabuleiro

Os vértices foram numerados na ordem de leitura (da esquerda para a direita, de cima para baixo):

Plaintext
(0,0) -> 0  |  (0,1) -> 1  |  (0,2) -> 2
(1,0) -> 3  |  (1,1) -> 4  |  (1,2) -> 5
(2,0) -> 6  |  (2,1) -> 7  |  (2,2) -> 8

## 📁 Estrutura do Projeto

t2-cavalo/
├── README.md
├── dados/
│   └── entrada.txt
└── src/
    ├── main.py
    ├── graph.py
    ├── cc.py
    ├── cycle.py
    └── breadth_first_paths.py


## Como executar

1. Acesse a pasta do projeto:
cd t2-cavalo/src

2. Execute o programa:
python3 main.py

## Perguntas que o Programa Responde

O programa gera um relatório automático respondendo:

✔ Lista de Adjacência: Qual o grafo gerado pelos movimentos?
✔ Componentes Conexas: Quantos grupos isolados existem e quais vértices pertencem a cada um?
✔ Distância Mínima: Qual o menor caminho entre as posições (0,0) e (2,2)?
✔ Detecção de Ciclos: O grafo possui ciclos? (Com análise de complexidade de tempo $O(V + E)$ e espaço $O(V)$).
✔ Exemplo de Ciclo: Quais os vértices que compõem um ciclo encontrado?

## Conclusão

Este trabalho demonstra como problemas lúdicos ou matemáticos (como movimentos de peças de xadrez) podem ser abstraídos para grafos. Através desta modelagem, foi possível comprovar que o cavalo no tabuleiro 3x3 possui um grafo com duas componentes conexas e contém ciclos que percorrem todas as bordas do tabuleiro.