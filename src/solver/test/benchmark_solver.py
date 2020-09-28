import sys
sys.path.insert(0, "..") # solver.py is in the directory above!

import cProfile
import json
import os

import solver

def benchmark_puzzle(puzzle):
    """
    Benchmark how many function calls it takes to solve the puzzle and how long
    each function takes.

    @param puzzle: Information pertaining to the puzzle being solved.
    """

    moves = puzzle["moves"]
    playfield = puzzle["playfield"]

    cProfile.runctx("solver.is_solvable(moves, playfield)",
                    globals=globals(),
                    locals=locals())

def main():
    # Directory towards my list of puzzles!
    dir = os.path.join(os.path.dirname(__file__), "../../../puzzles")

    for p in os.listdir(dir):
        filename = "../../../puzzles/{}".format(p)
        with open(filename) as f:
            try:
                puzzle = json.load(f)
            except:
                continue

        benchmark_puzzle(puzzle)

if __name__ == "__main__":
    main()
