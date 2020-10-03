import cv2
import os

import capture
import imager
import solver

def main():
    """
    Take the saved captures of the game feed and solve the puzzle based on the
    image provided.
    """

    dir = os.path.join(os.path.dirname(__file__), "../res/captures")

    for c in os.listdir(dir):
        filename = "../res/captures/{}".format(c)
        try:
            img = cv2.imread(filename)
        except:
            continue

        if (img is None):
            continue

        # Pull the important image information from the capture
        playfield_img = capture.crop_to_playfield(img)
        moves_img = capture.crop_to_moves(img)

        # Process these smaller images into the game states
        playfield = imager.img_to_playfield(playfield_img)
        moves = imager.img_to_moves(moves_img)

        if solver.is_solvable(moves, playfield):
            x, y = solver.solution[-1]

            # Create and display the image of the solution
            solved = imager.combined_to_img(playfield, (x, y))
            cv2.imshow("Puzzle Solution", solved)
            cv2.waitKey(0)
        else:
            print("{} is not solvable!".format(c))

if __name__ == "__main__":
    main()
