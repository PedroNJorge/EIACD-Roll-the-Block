# EIACD-Roll-the-Block

## Introduction
This project recreates the classic Bloxorz puzzle game (without the teleport feature) and implements various search algorithms to automatically solve each level, i.e. **Breath-First Search**, **Depth-First Search**, **Iterative Deepening Search**, **Uniform-Cost Search**, for the uninformed search algorithms, and, **Greedy Search**, **A\* Search**, for the informed search algorithms. Bloxorz is a 3D block-rolling puzzle game where players navigate a rectangular block through challenging terrain to reach a goal hole.

## Game Rules
The game features a 2x1x1 rectangular block that can move in four direction: **up**, **down**, **right**, **left**.
1. **Block States**:
   - **Upright** (2 cubes stacked in the z-axis)
   - **Horizontal** (2 cubes side by side in the x-axis)
   - **Vertical** (2 cubes side by side in the y-axis
por imagens do jogo em si
2. **Level Elements**:
   - **Void tiles**: The block falls over, ending the game
   - **Floor tiles**: Can support the block in any orientation
   - **Glass Floor tiles**: Break if the block stands upright on them (must be crossed lying flat)
   - **Goal tile**: The hole where the block must end in the upright state to win
   - **Hidden Path**: Require the block to activate switches to cross
   - **Buttons**
     * *X Type*: Require the block to be standing upright to activate
     * *Hexagonal Type*: Can be activated by the block in any orientation
     * *One-Time-Use Type*: Have the same visual cue as the X Type, but only function one time
por imagens do jogo em si
3. **Movement**:
   - The block always rolls over an edge
   - Each move changes the block's orientation
   - From the upright state, any roll makes the block lay flat (horizontal/vertical)
   - From the horizontal/vertical state, rolling "forward" makes it stand up, while rolling "sideways" keeps it flat

4. **Losing Conditions**:
   - Block falls off the map (touches a void tile)
   - Block stands upright on a glass tile

## Project Features
- Faithful recreation of the original Bloxorz game mechanics
- Visual representation of the game board and block movement
- Multiple implemented search algorithms to solve puzzles automatically
- Implementation of the *Manhattan distance* as an heuristic for the informed search algorithms
- Step-by-step solution visualization given by the chosen search algorithm
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

## Implementation Details
The project is implemented in Python3 and features:
- Modular game logic separated from algorithm implementations
- Clean object-oriented design for game elements
- Visualization layer to observe the solving process
- Performance metrics for algorithm comparison

```bash
# Installation (using conda)
git clone https://github.com/PedroNJorge/EIACD-Roll-the-Block
cd EIACD-Roll-the-Block
conda create -f environment.yml
```

## How to Use
1. Run the main file to launch the game:
   ```bash
   conda activate environment
   python3 main.py
   ```
2. Play manually using the WASD or arrow keys
3. Or select a search algorithm from the menu
4. View solution statistics and replay solutions

## Acknowledgments
Inspired by the original Bloxorz game by Damien Clarke. This project was created for educational purposes to explore search algorithms in game AI.
