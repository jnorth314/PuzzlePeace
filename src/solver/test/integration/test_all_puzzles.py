import sys
sys.path.insert(0, "../..") # solver.py is in the directory above!

import json
import os
import unittest

import solver

class TestPuzzles(unittest.TestCase):
    def test_all_puzzles(self):
        """
        Test all of the sample puzzles given since they should all be solvable!
        """

        dir = os.path.join(os.path.dirname(__file__), "../../../../puzzles")

        for p in os.listdir(dir):
            filename = "../../../../puzzles/{}".format(p)
            with open(filename) as f:
                try:
                    puzzle = json.load(f)
                except:
                    continue

            status = solver.is_solvable(puzzle["moves"], puzzle["playfield"])

            self.assertTrue(status)

if __name__ == "__main__":
    unittest.main()
