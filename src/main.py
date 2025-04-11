import os

from puzzle import Puzzle

def main() -> None:
    """Sample of loading and solving a complicated puzzle"""

    path_to_puzzle = os.path.join(os.path.dirname(__file__), "../res/TA/5-05.json")

    puzzle = Puzzle()
    puzzle.load_from_json_file(path_to_puzzle)
    puzzle.solve()

    for move, (x, y) in enumerate(puzzle.solution, start=1):
        print(f"Move {move}: {x}, {y}")

if __name__ == "__main__":
    main()
