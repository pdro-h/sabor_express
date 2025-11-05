# sabor express
### Descrição do Problema e Objetivos
O projeto **Sabor Express** tem como objetivo otimizar o processo de entrega de pedidos em um sistema de delivery, utilizando algoritmos de rotas.  
O desafio proposto é encontrar as **rotas mais eficientes** entre o restaurante e os clientes, considerando a distância.

### Objetivos principais:
- Reduzir o tempo de entrega por meio de rotas inteligentes;  
- Explorar diferentes algoritmos de busca (BFS, DFS, A*);  
- Comparar a eficiência de cada abordagem;

### Descrição
No projeto foi testado três algoritmos de busca: **A\***, **BFS** e **DFS**, para encontrar a melhor rota de entrega do **Sabor Express**.  
O objetivo foi ver qual algoritmo conseguia o caminho mais curto entre o ponto de partida e o destino.

### Resultados
| Algoritmo | Distância |
|------------|------------|
| A\*        | **6 km**   |
| BFS        | 7 km       |
| DFS        | 7 km       |

### Conclusão
O algoritmo **A\*** foi o mais eficiente para o problema de entrega, encontrando a melhor rota entre os três testados.

### Passos
```
pip install -r requirements.txt
```
```
python main.py
```

