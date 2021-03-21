def clear_matches(playfield):
    """
    Clear matches of 3 blocks in both the vertical and horizontal positions of
    the playfield.

    @param playfield: Playfield to check for matches of 3.
    @return: Status if any blocks were cleared.
    """

    # Create a copy of the playfield
    temp = [i[:] for i in playfield]

    for y in range(12):
        for x in range(6):
            # Empty blocks don't count as a match of 3
            if (playfield[y][x] == 0):
                continue

            # Horizontal
            if (x < (6 - 2) and playfield[y][x] == playfield[y][x + 1] and playfield[y][x] == playfield[y][x + 2]):
                temp[y][x] = temp[y][x + 1] = temp[y][x + 2] = 0

            # Vertical
            if (y < (12 - 2) and playfield[y][x] == playfield[y + 1][x] and playfield[y][x] == playfield[y + 2][x]):
                temp[y][x] = temp[y + 1][x] = temp[y + 2][x] = 0

    # Check if any of the blocks cleared, if they did we need to copy them back
    # over to the playfield.
    if (playfield != temp):
        playfield[:] = [i[:] for i in temp]
        return True
    else:
        return False

def fall_blocks(playfield):
    """
    Get rid of the empty gaps between blocks of a column.

    @param playfield: Playfield to check for the empty gaps.
    @return: Status if any empty gaps were removed.
    """

    temp = [[0] * 6 for y in range(12)]

    # Go through each column and start placing blocks at the lowest available
    # row. Since the lowest available row is the largest number, we decrement
    # each time we find a non-empty block to be placed.
    for x in range(6):
        r = 11
        for y in range(11, -1, -1):
            if (playfield[y][x] != 0):
                temp[r][x] = playfield[y][x]
                r -= 1

    # Check if any of the blocks moved, if they did we need to copy them back
    # over to the playfield.
    if (playfield != temp):
        playfield[:] = [i[:] for i in temp]
        return True
    else:
        return False

def is_solved(playfield):
    """
    Get the status of whether or not the playfield has been solved and no blocks
    are remaining.

    @param playfield: Playfield to check for remaining blocks.
    @return: Status if the playfield is empty.
    """

    return not any(map(any, playfield))
