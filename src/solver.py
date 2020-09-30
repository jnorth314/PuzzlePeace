import logic

# The moves that need to be made in order to solve the puzzle in reverse order!
solution = []

def is_solvable(moves, playfield):
    """
    Recursive function to figure out with the given moves left and playfield
    that the puzzle is solvable.

    @param moves: Number of moves left
    @param playfield: State of the playfield.
    @return: Status of whether the puzzle is solvable from this position.
    """

    global solution

    # Do the game logic until both of these return false
    while (logic.clear_matches(playfield) or logic.fall_blocks(playfield)):
        pass

    if (logic.is_solved(playfield)):
        solution = [] # Clear the solution from previous puzzles!
        return True

    if (moves == 0):
        return False

    for y in range(12):
        for x in range(6 - 1):
            # Can only swap when the two adjacent blocks are not equal
            if (playfield[y][x] != playfield[y][x + 1]):
                # Create a temp for this branch as we want to keep the playfield
                # as is if this branch fails.
                temp = [i[:] for i in playfield]

                # Swap the blocks
                temp[y][x], temp[y][x + 1] = temp[y][x + 1], temp[y][x]

                if (is_solvable(moves - 1, temp)):
                    solution.append((x, y))
                    return True

    return False
