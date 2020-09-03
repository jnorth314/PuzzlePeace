# PuzzlePeace
A solver for the puzzle mode of games like Tetris Attack/Panel de Pon/Puzzle League.

# How it works!
The solver works by checking if a block is able to be swapped. If a move is possible it takes the branch and simulates the game logic until the playfield is in a stable state. This is repeated for every possible block swap and move until it finds that the board is empty (thus the puzzle is solved).

# Puzzle JSON format!

There are two parts to the JSON file used in solving the puzzles in `main.py`

`playfield` - A 2D array of blocks with a width of 6 and height of 12. Zero represents an empty square, non-zero represents a block.
`moves` - Number of moves that the game suggests the puzzle can be beaten in.

Here is an example of a very simple puzzle:
```
{
    "playfield" : [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 0, 1, 0, 0]
    ],
    "moves" : 1
}
```
