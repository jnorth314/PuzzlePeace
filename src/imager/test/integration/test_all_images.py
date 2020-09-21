import sys
sys.path.insert(0, "../..") # imager.py is in the directory above!

import cv2
import json
import os
import unittest

import imager

class TestImages(unittest.TestCase):
    def test_all_images(self):
        """
        Test all of the sample puzzles given since we have the corresponding
        JSON equal to the results!
        """

        dir = os.path.join(os.path.dirname(__file__), "../../../../images")

        for p in os.listdir(dir):
            filename = "../../../../images/{}".format(p)
            try:
                img = cv2.imread(filename)
            except:
                continue

            if (img is None):
                continue

            filename = "../../../../puzzles/{}".format(p)
            with open(filename) as f:
                try:
                    puzzle = json.load(f)
                except:
                    continue

            playfield = imager.img_to_playfield(img)

            self.assertEqual(playfield, puzzle["playfield"])

if __name__ == "__main__":
    unittest.main()
