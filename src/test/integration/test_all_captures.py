import sys
sys.path.insert(0, "../..") # capture.py is in the directory above!

import cv2
import os
import unittest

import capture

class TestCaptures(unittest.TestCase):
    def test_all_captures(self):
        """
        Test all of the sample captures given.
        """

        dir = os.path.join(os.path.dirname(__file__), "../../../res/captures")

        for c in os.listdir(dir):
            filename = "../../../res/captures/{}".format(c)
            try:
                img = cv2.imread(filename)
            except:
                continue

            if (img is None):
                continue

            playfield = capture.crop_to_playfield(img)

if __name__ == "__main__":
    unittest.main()
