import sys
sys.path.insert(0, "../..") # imager.py is in the directory above!

import cv2
import json
import os
import unittest

import imager

class TestPlayfields(unittest.TestCase):
    def test_all_playfields(self):
        """
        Test all of the sample puzzles given since we have the corresponding
        JSON equal to the results!
        """

        dir = os.path.join(os.path.dirname(__file__), "../../../res/playfields")

        for p in os.listdir(dir):
            filename = "../../../res/playfields/{}".format(p)
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

            playfield = imager.img_to_playfield(img)

            self.assertEqual(playfield, puzzle["playfield"])

if __name__ == "__main__":
    unittest.main()
