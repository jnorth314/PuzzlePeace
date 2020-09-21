# PuzzlePeace
A solver for the puzzle mode of games like Tetris Attack/Panel de Pon/Puzzle League.

# How it works!
## `imager.py`
The imager works by checking the center of each block for the color. It compares colors by calculating the euclidean distance of all 3 components and normalizing it between 0.0 and 1.0. It repeats this for all colors until it finds a distance that is less than 0.1. If no color matches, than that spot must be empty. This method could be improved upon by some of the functionality in open-cv like Histograms or L2 Norm.

## `solver.py`
The solver works by checking if a block is able to be swapped. If a move is possible it takes the branch and simulates the game logic until the playfield is in a stable state. This is repeated for every possible block swap and move until it finds that the board is empty (thus the puzzle is solved).

# File formats!
## Image format
The images only consist of the playfield's 6 by 12 grid. This gives image dimensions of 96 by 192, where each block is a square that is 16 by 16.

## Puzzle JSON format
There are two parts to the JSON file used in solving the puzzles in `solver/main.py`

* `playfield` - A 2D array of blocks with a width of 6 and height of 12. Zero represents an empty square, non-zero represents a block.
* `moves` - Number of moves that the game suggests the puzzle can be beaten in.

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
