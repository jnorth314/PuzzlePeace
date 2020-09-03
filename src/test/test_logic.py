import sys
sys.path.insert(0, "..") # logic.py is in the directory above!

import unittest

import logic

class TestLogic(unittest.TestCase):
    def test_clear_matches(self):
        """
        Test the ability to find and clear matches of 3 or more blocks in a row
        both horizontally and vertically.
        """

        # Creating an empty playfield, no matches
        playfield = [[0 for x in range(6)] for y in range(12)]
        solution = [[0 for x in range(6)] for y in range(12)]
        status = logic.clear_matches(playfield)
        self.assertFalse(status)
        self.assertEqual(playfield, solution)

        # Creating a simple playfield, no matches
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[11][1] = 1
        playfield[10][0] = 1
        solution = [[0 for x in range(6)] for y in range(12)]
        solution[11][1] = 1
        solution[11][0] = 1
        solution[10][0] = 1
        status = logic.clear_matches(playfield)
        self.assertFalse(status)
        self.assertEqual(playfield, solution)

        # Creating a horizontal match of 3
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[11][1] = 1
        playfield[11][2] = 1
        solution = [[0 for x in range(6)] for y in range(12)]
        status = logic.clear_matches(playfield)
        self.assertTrue(status)
        self.assertEqual(playfield, solution)

        # Creating a horizontal match of greater than 3
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[11][1] = 1
        playfield[11][2] = 1
        playfield[11][3] = 1
        playfield[11][4] = 1
        solution = [[0 for x in range(6)] for y in range(12)]
        status = logic.clear_matches(playfield)
        self.assertTrue(status)
        self.assertEqual(playfield, solution)

        # Creating a vertical match of 3
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[10][0] = 1
        playfield[9][0] = 1
        solution = [[0 for x in range(6)] for y in range(12)]
        status = logic.clear_matches(playfield)
        self.assertTrue(status)
        self.assertEqual(playfield, solution)

        # Creating a vertical match of greater than 3
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[10][0] = 1
        playfield[9][0] = 1
        playfield[8][0] = 1
        playfield[7][0] = 1
        solution = [[0 for x in range(6)] for y in range(12)]
        status = logic.clear_matches(playfield)
        self.assertTrue(status)
        self.assertEqual(playfield, solution)

        # Creating a horizontal AND vertical match of 3 (Forming an L)
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[11][1] = 1
        playfield[11][2] = 1
        playfield[10][0] = 1
        playfield[9][0] = 1
        solution = [[0 for x in range(6)] for y in range(12)]
        status = logic.clear_matches(playfield)
        self.assertTrue(status)
        self.assertEqual(playfield, solution)

    def test_fall_blocks(self):
        """
        Test the ability to find and modify gaps between blocks in columns of
        the playfield.
        """

        # Creating an empty playfield, no blocks to fall
        playfield = [[0 for x in range(6)] for y in range(12)]
        solution = [[0 for x in range(6)] for y in range(12)]
        status = logic.fall_blocks(playfield)
        self.assertFalse(status)
        self.assertEqual(playfield, solution)

        # Creating a playfield with some blocks, but no gaps in the columns
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[11][1] = 2
        playfield[10][0] = 3
        solution = [[0 for x in range(6)] for y in range(12)]
        solution[11][0] = 1
        solution[11][1] = 2
        solution[10][0] = 3
        status = logic.fall_blocks(playfield)
        self.assertFalse(status)
        self.assertEqual(playfield, solution)

        # Creating a playfield with some blocks and gaps between columns
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[9][0] = 2
        playfield[7][0] = 3
        solution = [[0 for x in range(6)] for y in range(12)]
        solution[11][0] = 1
        solution[10][0] = 2
        solution[9][0] = 3
        status = logic.fall_blocks(playfield)
        self.assertTrue(status)
        self.assertEqual(playfield, solution)

    def test_is_solved(self):
        """
        Test checking if a playfield is solved with all blocks being empty.
        """

        # Creating an empty playfield,is solved
        playfield = [[0 for x in range(6)] for y in range(12)]
        status = logic.is_solved(playfield)
        self.assertTrue(status)

        # Creating a non-empty playfield, is not solved
        playfield = [[1 for x in range(6)] for y in range(12)]
        status = logic.is_solved(playfield)
        self.assertFalse(status)

if __name__ == "__main__":
    unittest.main()
