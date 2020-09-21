import json
import os

import solver

def main():
    # Directory towards my list of puzzles!
    dir = os.path.join(os.path.dirname(__file__), "../../puzzles")

    for p in os.listdir(dir):
        filename = "../../puzzles/{}".format(p)
        with open(filename) as f:
            try:
                puzzle = json.load(f)
            except:
                continue

        # Solve the puzzle!
        status = solver.is_solvable(puzzle["moves"], puzzle["playfield"])

        if (status == True):
            # The solution should be reversed because the moves get appended in
            # reverse order as it goes back up the graph. Keep in mind that the
            # solver waits for the playfield to achieve a stable state before
            # moving on to the next move. Thus, attempting to use these moves
            # means you should wait until the playfield is done clearing/falling
            # before the next input.
            print("{} has been solved with the following moves: {}".format(p, solver.solution[::-1]))
        else:
            print("{} can not be solved!".format(p))

if __name__ == "__main__":
    main()
