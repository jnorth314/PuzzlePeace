import unittest
from unittest.mock import patch

from puzzle import Puzzle

class TestPuzzle(unittest.TestCase):
    def test_create(self):
        puzzle = Puzzle()

        self.assertEqual(puzzle.moves, 0)
        self.assertListEqual(puzzle.playfields, [])
        self.assertListEqual(puzzle.solution, [])

    def test_load_from_json_file(self):
        blocks = [[x + y for x in range(6)] for y in range(12)]
        moves = 3
        puzzle = Puzzle()

        with (
            patch("builtins.open"),
            patch("json.load", return_value={"blocks": blocks, "moves": moves})
        ):
            puzzle.load_from_json_file("puzzle.json")

        self.assertEqual(puzzle.moves, moves)
        self.assertEqual(len(puzzle.playfields), moves + 1)
        self.assertListEqual(puzzle.playfields[moves].blocks, blocks)

    def test_solve_one_move(self):
        blocks = [
            [0, 0, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        moves = 1
        puzzle = Puzzle()

        with (
            patch("builtins.open"),
            patch("json.load", return_value={"blocks": blocks, "moves": moves})
        ):
            puzzle.load_from_json_file("puzzle.json")

        result = puzzle.solve()

        self.assertTrue(result)
        self.assertListEqual(puzzle.solution, [(4, 0)])

    def test_solve_two_moves(self):
        blocks = [
            [0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        moves = 2
        puzzle = Puzzle()

        with (
            patch("builtins.open"),
            patch("json.load", return_value={"blocks": blocks, "moves": moves})
        ):
            puzzle.load_from_json_file("puzzle.json")

        result = puzzle.solve()

        self.assertTrue(result)
        self.assertListEqual(puzzle.solution, [(4, 0), (3, 0)])

    def test_solve_no_solution(self):
        blocks = [
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        moves = 1
        puzzle = Puzzle()

        with (
            patch("builtins.open"),
            patch("json.load", return_value={"blocks": blocks, "moves": moves})
        ):
            puzzle.load_from_json_file("puzzle.json")

        result = puzzle.solve()

        self.assertFalse(result)
        self.assertListEqual(puzzle.solution, [])

if __name__ == "__main__":
    unittest.main()
