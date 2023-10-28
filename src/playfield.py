class Playfield:
    """Class describing the layout of a playfield and its logic"""

    def __init__(self, width: int=6, height: int=12):
        self.width = width
        self.height = height
        self.blocks: list[list[int]] = [[0 for _ in range(width)] for _ in range(height)]

    def fall(self) -> bool:
        """Cause all blocks to fall into empty spaces below"""

        blocks = [[0] * self.width for _ in range(self.height)]

        for x in range(self.width): # pylint: disable=invalid-name
            row = 0
            for y in range(self.height): # pylint: disable=invalid-name
                if self.blocks[y][x] != 0:
                    blocks[row][x] = self.blocks[y][x]
                    row += 1

        has_fall = blocks != self.blocks

        if has_fall:
            self.blocks[:] = [row[:] for row in blocks]

        return has_fall

    def match(self) -> bool:
        """Cause all matches of 3 to disappear"""

        blocks = [row[:] for row in self.blocks]

        for x in range(self.width): # pylint: disable=invalid-name
            for y in range(self.height): # pylint: disable=invalid-name
                if self.blocks[y][x] == 0:
                    continue

                if x < self.width - 2 and self.blocks[y][x] == self.blocks[y][x + 1] == self.blocks[y][x + 2]:
                    blocks[y][x] = blocks[y][x + 1] = blocks[y][x + 2] = 0

                if y < self.height - 2 and self.blocks[y][x] == self.blocks[y + 1][x] == self.blocks[y + 2][x]:
                    blocks[y][x] = blocks[y + 1][x] = blocks[y + 2][x] = 0

        has_match = blocks != self.blocks

        if has_match:
            self.blocks[:] = [row[:] for row in blocks]

        return has_match

    def update(self) -> None:
        """Update the playfield until it is in a stable state"""

        while self.fall() or self.match():
            pass

    def is_empty(self) -> bool:
        """Check if the puzzle has any blocks remaining"""

        return not any(map(any, self.blocks))
