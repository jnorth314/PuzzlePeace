import json
from typing import TypedDict

from playfield import Playfield

class PuzzleJSON(TypedDict):
    """Type definition for the JSON Files"""

    blocks: list[list[int]]
    moves: int

class Puzzle:
    """Class definition describing a playfield puzzle with a given layout"""

    def __init__(self) -> None:
        self.moves = 0
        self.playfields: list[Playfield] = []
        self.solution: list[tuple[int, int]] = []

    def load_from_json_file(self, filename: str) -> None:
        """Load a puzzle from a JSON file"""

        with open(filename, encoding="utf-8") as file:
            puzzle: PuzzleJSON = json.load(file)
            self.moves = puzzle["moves"]
            self.playfields = [Playfield() for _ in range(self.moves + 1)]
            self.playfields[self.moves].blocks = [row[:] for row in puzzle["blocks"]]

    def solve(self) -> bool:
        """Solve the puzzle"""

        playfield = self.playfields[self.moves]
        playfield.update()

        if playfield.is_empty():
            return True

        if self.moves == 0:
            return False

        self.moves -= 1
        next_ = self.playfields[self.moves]

        for x in range(playfield.width - 1): # pylint: disable=invalid-name
            for y in range(playfield.height): # pylint: disable=invalid-name
                if playfield.blocks[y][x] != playfield.blocks[y][x + 1]:
                    next_.blocks = [row[:] for row in playfield.blocks]
                    next_.blocks[y][x], next_.blocks[y][x + 1] = next_.blocks[y][x + 1], next_.blocks[y][x]

                    if self.solve():
                        self.solution.insert(0, (x, y))
                        return True

        self.moves += 1
        return False
