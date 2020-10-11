import sys
sys.path.insert(0, "..") # src is in the directory above!

import json
import os

import solver

def main():
    dir = os.path.join(os.path.dirname(__file__), "../../res/puzzles")

    for p in os.listdir(dir):
        filename = "../../res/puzzles/{}".format(p)
        with open(filename) as f:
            try:
                puzzle = json.load(f)
            except:
                continue

        status = solver.is_solvable(puzzle["moves"], puzzle["playfield"])

        if status:
            # The solver appends the moves in reverse order so the list will
            # need to be flipped before displaying the solution.
            print("{} solved with the following moves: {}".format(p, solver.solution[::-1]))
        else:
            print("{} is not solvable!".format(p))

if __name__ == "__main__":
    main()
