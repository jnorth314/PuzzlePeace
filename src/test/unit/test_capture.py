import sys
sys.path.insert(0, "../..") # capture.py is in the directory above!

import cv2
import numpy
import unittest

import capture

class TestCapture(unittest.TestCase):
    def test_crop_to_playfield(self):
        """
        Test cropping an image of the capture to the playfield.
        """

        img = numpy.zeros((256, 224, 3), numpy.uint8)

        playfield = capture.crop_to_playfield(img)

    def test_crop_to_moves(self):
        """
        Test cropping an image of the capture to the move count.
        """

        img = numpy.zeros((256, 224, 3), numpy.uint8)

        moves = capture.crop_to_moves(img)

if __name__ == "__main__":
    unittest.main()
