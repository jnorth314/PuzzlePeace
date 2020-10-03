import sys
sys.path.insert(0, "../..") # imager.py is in the directory above!

import cv2
import numpy
import unittest

import imager

class TestImager(unittest.TestCase):
    def test_img_to_cursor(self):
        """
        Test creating cursor position from an image.
        """

        img = numpy.zeros((16 * 12, 16 * 6, 3), numpy.uint8)

        cursor = imager.img_to_cursor(img)

    def test_img_to_playfield(self):
        """
        Test creating a playfield from an image.
        """

        img = numpy.zeros((16 * 12, 16 * 6, 3), numpy.uint8)

        playfield = imager.img_to_playfield(img)

    def test_img_to_moves(self):
        """
        Test creating number of moves from an image.
        """

        img = numpy.zeros((42, 48, 3), numpy.uint8)

        moves = imager.img_to_moves(img)
        
    def test_cursor_to_img(self):
        """
        Test creating an image from a cursor position.
        """

        cursor = (0, 0)

        img = imager.cursor_to_img(cursor)

    def test_playfield_to_img(self):
        """
        Test creating an image from a playfield.
        """

        playfield = [[0 for x in range(6)] for y in range(12)]

        img = imager.playfield_to_img(playfield)

    def test_combined_to_img(self):
        """
        Test creating an image from a playfield and cursor position.
        """

        cursor = (0, 0)
        playfield = [[0 for x in range(6)] for y in range(12)]

        img = imager.combined_to_img(playfield, cursor)

    def test_get_normalized_distance(self):
        """
        Test calculating the euclidean distance between two colors.
        """

        c1 = (0, 0, 0)
        c2 = (255, 255, 255)
        d1 = imager.get_normalized_distance(c1, c2)
        d2 = 1.0 # The pixels are as far apart as possible
        self.assertEqual(d1, d2)

        c1 = (255, 255, 255)
        c2 = (0, 0, 0)
        d1 = imager.get_normalized_distance(c1, c2)
        d2 = 1.0 # The pixels are as far apart as possible, but flipped
        self.assertEqual(d1, d2)

        c1 = (0, 0, 0)
        c2 = (0, 0, 0)
        d1 = imager.get_normalized_distance(c1, c2)
        d2 = 0.0 # The pixels are the same
        self.assertEqual(d1, d2)

        c1 = (0, 0, 0)
        c2 = (30, 40, 50)
        d1 = imager.get_normalized_distance(c1, c2)
        d2 = ((30**2 + 40**2 + 50**2) ** 0.5) / ((255**2 + 255**2 + 255**2) ** 0.5)
        self.assertEqual(d1, d2)

if __name__ == "__main__":
    unittest.main()
