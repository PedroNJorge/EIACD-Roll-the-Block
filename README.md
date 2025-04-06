# EIACD-Roll-the-Block

## Introduction
This project recreates the classic Bloxorz puzzle game (without the teleport feature) and implements various search algorithms to automatically solve each level, i.e. **Breath-First Search**, **Depth-First Search**, **Iterative Deepening Search**, **Uniform-Cost Search**, for the uninformed search algorithms, and, **Greedy Search**, **A\* Search**, for the informed search algorithms. Bloxorz is a 3D block-rolling puzzle game where players navigate a rectangular block through challenging terrain to reach a goal hole.</br></br>

## Game Rules
The game features a 2x1x1 rectangular block that can move in four direction: **up**, **down**, **right**, **left**.
1. **Block States**:
   - **Upright** (2 cubes stacked in the z-axis)
   - **Horizontal** (2 cubes side by side in the x-axis)
   - **Vertical** (2 cubes side by side in the y-axis

2. **Level Elements**:
   - **Void tiles**: The block falls over, ending the game
   - **Floor tiles**: Can support the block in any orientation
   - **Glass Floor tiles**: Break if the block stands upright on them (must be crossed lying flat)
   - **Goal tile**: The hole where the block must end in the upright state to win
   - **Hidden Path**: Require the block to activate switches to cross
   - **Buttons**
   - * *X Type*: Require the block to be standing upright to activate
     * *Hexagonal Type*: Can be activated by the block in any orientation
     * *One-Time-Use Type*: Have the same visual cue as the X Type, but only function one time

3. **Movement**:
   - The block always rolls over an edge (never slides)
   - Each move changes the block's orientation
   - From standing position, any roll makes the block lay flat
   - From flat position, rolling "forward" makes it stand up, while rolling "sideways" keeps it flat

3. **Level Elements**:
   - **Normal tiles**: Can support the block in any orientation
   - **Weak tiles**: Break if the block stands upright on them (must be crossed lying flat)
   - **Goal tile**: The hole where the block must end standing upright to win
   - **Bridges**: Require the block to activate switches to cross
   - **Walls**: Block movement in certain directions

4. **Losing Conditions**:
   - Block falls off the map
   - Block stands upright on a weak tileThe key rules are:The block itself has 3 different states:
* **Upright**
* **Horizontal**
* **Vertical**
por imagens do jogo em si


Matrix Caption: </br>
* `-2` - Hidden Path
* `-1` - Void
* `0` - Floor
* `1` - Block "upright"
* `2` - Block "horizontal" / "vertical"
* `3` - Glass Floor
* `4` - X Type Button
* `5` - Hexagonal Type Button
* `6` - One Time Use Type Button
* `7` - Goal

# Libraries used

Roll The Block em Python

	Este programa foi feito baseado no jogo Space Block/Bloroxrz cujo objetivo é mover o bloco até à meta (tendo este de terminar na "vertical").

	Legenda da matriz: 	0-Espaços vazios
				1-Espaços por onde o bloco pode andar
				2-Representação do bloco na vertical/"em pé"
				3-Representação do bloco deitado (Tanto na horizontal como na vertical)
				4-Chão de vidro (ou seja, espaço onde se o bloco estiver "em pé" perde)
				5-Botão desativado
				51-Caminho escondido que será ativado após o bloco chegar ao botão e ficar "em pé"
				6-Botão ativado
				9-Meta

	Para o programa funcionar é necessário dar import à biblioteca pygame (parte gráfica feita em pygame), exit (para poder fechar o programa), 
pprint(para dar print às matrizes de forma mais legível), time (útil para executar o programa de forma mais lenta para detetar erros), copy (usamos deppcopy no programa), numpy 
(para criar matrizes de forma mais rápida), deque (usado no algoritmo BFS) e heapq (usado nos algoritmos greedy e A*)
	
	Modo de execução: 

			Pygame- Para jogar o utilizador deve extrair os ficheiros do ficheiro ZIP. De seguida, abrir o terminal,e digitar "python3 jogo.py". Clique em "Play" 
e escolha o nível que quer jogar (pode diminuir a música em OPTIONS>VOLUME> "-"). Depois de escolhido o nível o utilizador deve utilizar as teclas "w", "a", "s" e "d" 
para fazer os movimentos para a cima, esquerda, baixo e direita, respetivamente. O objetivo é levar o bloco vermelho a ficar "de pé" em cima da meta (quadrado amarelo). Caso perca ou vença o nível prima "s" para voltar ao menu.

			Terminal- Para jogar no terminal o utilizador deve abrir o Jupyter (por exemplo) e executar a primeira célula do notebook. De seguida digite o nível (de 1 a 5). Depois deve correr as próximas duas células 
e irá abrir-lhe uma janela pygame. Pode, ou não executar movimentos antes de serem aplicados os algoritmos de pesquisa. Caso faça algum movimento DEVE correr a "célula das posições". 
Caso não tenha feito movimentos NÃO execute a "célula das posições". De seguida, estão listados os vários algoritmos de pesquisa entre os quais o utilizador pode escolher qual executar. Para 
os algoritmos greedy e A* TEM de executar antes a "célula heurística".

Ps.:    Em caso de falha do Menu, pode jogar os níveis no Notebook (Atenção que os níveis de 6 a 9 não têm algoritmos de pesquisa devido à adição do botão e da complexidade do nível do chão de vidro).
	Caso queira saber os estados resultantes do caminho até à meta dos algoritmos de pesquisa é só apagar os " # " atrás dos prints/pprints.
