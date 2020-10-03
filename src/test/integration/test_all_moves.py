import sys
sys.path.insert(0, "../..") # imager.py is in the directory above!

import cv2
import json
import os
import unittest

import imager

class TestMoves(unittest.TestCase):
    def test_all_moves(self):
        """
        Test all of the moves images since we have the provided JSON equal to
        the results!
        """

        dir = os.path.join(os.path.dirname(__file__), "../../../res/moves")

        for p in os.listdir(dir):
            filename = "../../../res/moves/{}".format(p)
            try:
                img = cv2.imread(filename)
            except:
                continue

            if (img is None):
                continue

            filename = "../../../res/puzzles/{}.json".format(os.path.splitext(p)[0])
            with open(filename) as f:
                try:
                    puzzle = json.load(f)
                except:
                    continue

            moves = imager.img_to_moves(img)

            self.assertEqual(moves, puzzle["moves"])

if __name__ == "__main__":
    unittest.main()
