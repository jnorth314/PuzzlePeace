# Puzzle Peace
A solver for the puzzle mode of games like Tetris Attack/Panel de Pon/Puzzle League.

# How it works!
This implements the basic algorithms of the game for matching and falling in order to brute force the solution.

## Puzzle JSON Format
| **Key** |    **Value**    |                **Description**               |
|:-------:|:---------------:|:--------------------------------------------:|
|  blocks | list[list[int]] |   2D-list of blocks in the initial puzzle.   |
|  moves  |       int       | Number of moves required to beat the puzzle. |
