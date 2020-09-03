import sys
sys.path.insert(0, "..") # solver.py is in the directory above!

import unittest

import solver

class TestSolver(unittest.TestCase):
    def test_is_solvable(self):
        """
        Test the ability to solve puzzles.
        """

        # We can only test whether or not the puzzle is solvable! If a puzzle
        # has multiple solutions, the solver will stop at the first solution
        # that it has found!

        # Creating an easy playfield to solve
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1
        playfield[11][1] = 1
        playfield[11][3] = 1 # Row looks like: 110100
        moves = 1
        status = solver.is_solvable(moves, playfield)
        self.assertTrue(status)

        # Creating an impossible playfield to solve
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[11][0] = 1 # Row looks like: 100001
        playfield[11][5] = 1 # Only 2 blocks remain, can't make a match of 3!
        moves = 1
        status = solver.is_solvable(moves, playfield)
        self.assertFalse(status)

        # Creating a "complex" playfield to solve
        playfield = [[0 for x in range(6)] for y in range(12)]
        playfield[8][2] = 3
        playfield[9][2] = 2
        playfield[10][0] = 3
        playfield[10][1] = 3
        playfield[10][2] = 1
        playfield[11][0] = 1
        playfield[11][1] = 1
        playfield[11][2] = 2
        playfield[11][5] = 2
        moves = 3
        status = solver.is_solvable(moves, playfield)
        self.assertTrue(status)

if __name__ == "__main__":
    unittest.main()
