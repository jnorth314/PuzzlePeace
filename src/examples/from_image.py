import sys
sys.path.insert(0, "..") # src is in the directory above!

import cv2
import os

def main():
    dir = os.path.join(os.path.dirname(__file__), "../../res/playfields")

    for i in os.listdir(dir):
        filename = "../../res/playfields/{}".format(i)
        try:
            img = cv2.imread(filename)
        except:
            continue

        if (img is None):
            continue

        playfield = imager.img_to_playfield(img)

        filename = "../../res/moves/{}".format(i)
        try:
            img = cv2.imread(filename)
        except:
            continue

        if (img is None):
            continue

        moves = imager.img_to_playfield(img)

        status = solver.is_solvable(moves, playfield)

        if status:
            # The solver appends the moves in reverse order so the list will
            # need to be flipped before displaying the solution.
            print("{} solved with the following moves: {}".format(p, solver.solution[::-1]))
        else:
            print("{} is not solvable!".format(p))

if __name__ == "__main__":
    main()
