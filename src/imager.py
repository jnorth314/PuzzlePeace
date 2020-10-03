import cv2
import numpy

def get_normalized_distance(c1, c2):
    """
    Calculate the euclidean distance between the colors.

    @param c1: Color 1.
    @param c2: Color 2.
    @return: Distance between colors as number from 0.0 to 1.0
    """

    # Square distance for each component
    sdb = (c1[0] - c2[0]) ** 2
    sdg = (c1[1] - c2[1]) ** 2
    sdr = (c1[2] - c2[2]) ** 2

    dt = (sdb + sdg + sdr) ** 0.5 # Total Distance

    return dt / ((255**2 + 255**2 + 255**2) ** 0.5) # Normalize it

def img_to_cursor(img):
    """
    Convert the image from the game into the cursor position.

    @param img: Image of the playfield.
    @return: Cursor's position. Since the cursor takes the space of two blocks
    horizontally, the position of the left block is what is returned.
    """

    c = (255, 251, 255) # Cursor color

    for y in range(12):
        for x in range(6 - 1):
            p1 = img[16 * y][16 * x]                     # Top Left
            p2 = img[16 * y][16 * (x + 2) - 1]           # Top Right
            p3 = img[16 * (y + 1) - 1][16 * x]           # Bottom Left
            p4 = img[16 * (y + 1) - 1][16 * (x + 2) - 1] # Bottom Right

            # Checking if each of those sections are close to the cursor color,
            # if they are we will return the coordinates. 0.1 is an arbitrary
            # distance chosen.
            if (get_normalized_distance(p1, c) < 0.1
                    and get_normalized_distance(p2, c) < 0.1
                    and get_normalized_distance(p3, c) < 0.1
                    and get_normalized_distance(p4, c) < 0.1):
                return (x, y)

    return (-1, -1) # Returns this if the cursor was not found

def img_to_playfield(img):
    """
    Convert the image from the game into the playfield list that can be solved
    by the solver.

    @param img: Image of the playfield.
    @return: State of the playfield.
    """

    playfield = [[0 for x in range(6)] for y in range(12)]

    colors = [
        (16, 16, 255),  # Red
        (0, 251, 0),    # Green
        (255, 26, 255), # Magenta
        (0, 251, 255),  # Yellow
        (255, 251, 0),  # Cyan
        (255, 115, 66)  # Blue
    ]

    for y in range(12):
        for x in range(6):
            # Center pixel of the block
            p = img[16 * y + 16 // 2][16 * x + 16 // 2]

            for i, c in enumerate(colors, 1):
                # 0.1 is an arbitrary distance that fits the goal
                if (get_normalized_distance(p, c) < 0.1):
                    playfield[y][x] = i
                    break

    return playfield

def img_to_moves(img):
    """
    Convert the image from the game into the number of moves left in the puzzle.

    @param img: Image of the number of moves.
    @return: Number of moves
    """

    c = (107, 32, 0) # Color of the font that displays the number

    # This method works like reading a 7-segment display, although it would be
    # better to have predetermined images that are compared and the best fit
    # is chosen. This is a very poor method that happens to work with my test
    # images. Also, only works assuming the number displayed is in range [0, 9]

    # Coordinates for each light of the 7-segment display
    segments = [
        (29, 24), # A
        (33, 29), # B
        (33, 35), # C
        (29, 40), # D
        (25, 35), # E
        (25, 29), # F
        (29, 32)  # G
    ]

    # A mapping of each 7-segment display to the numbers they would be in-game
    numbers = {
        #0bGFEDCBA
        0b0111111 : 0, # ABCDEF
        0b1001001 : 1, # ADG
        0b1011011 : 2, # ABDEG
        0b1001111 : 3, # ABCDG
        0b1100110 : 4, # BCFG
        0b1101101 : 5, # ACDFG
        0b1111101 : 6, # ACDEFG
        0b1001011 : 7, # ABDG
        0b1111111 : 8, # ABCDEFG
        0b1100111 : 9  # ABCFG
    }

    n = 0 # Number showing each segment of the displayed that is turned on.

    for i, (x, y) in enumerate(segments):
        p = img[y][x]
        if (get_normalized_distance(p, c) < 0.1):
            n += 1 << i

    if n in numbers:
        return numbers[n]
    else:
        return 0

def cursor_to_img(cursor):
    """
    Create an image of the cursor position to be displayed to the user!

    @param cursor: Position of the cursor.
    @return: Image of the cursor position in the playfield.
    """

    img = numpy.zeros((16 * 12, 16 * 6, 3), numpy.uint8)

    x, y = cursor # These coordinates are of the left block on the cursor

    # p1 is the top left of the cursor
    # p2 is the bottom right of the cursor
    p1 = (16 * x, 16 * y)
    p2 = (16 * (x + 2) - 1, 16 * (y + 1) - 1)
    c = (255, 251, 255) # Cursor color

    cv2.rectangle(img, p1, p2, c, 2)

    return img

def playfield_to_img(playfield):
    """
    Create an image of the playfield to be displayed to the user!

    @param playfield: State of the playfield.
    @return: Image of the playfield.
    """

    img = numpy.zeros((16 * 12, 16 * 6, 3), numpy.uint8)

    colors = [
        (0, 0, 0),      # Black
        (16, 16, 255),  # Red
        (0, 251, 0),    # Green
        (255, 26, 255), # Magenta
        (0, 251, 255),  # Yellow
        (255, 251, 0),  # Cyan
        (255, 115, 66)  # Blue
    ]

    for y in range(12):
        for x in range(6):
            # p1 is the top left of the rectangle
            # p2 is the bottom right of the rectangle
            p1 = (16 * x, 16 * y)
            p2 = (16 * (x + 1) - 1, 16 * (y + 1) - 1)
            c = colors[playfield[y][x]]

            cv2.rectangle(img, p1, p2, c, cv2.FILLED)

    return img

def combined_to_img(playfield, cursor):
    """
    Create an image of both the playfield and cursor position to be displayed to
    the user!

    @param playfield: State of the playfield.
    @param cursor: Position of the cursor.
    @return: Image of the playfield with the cursor.
    """

    # We can just take the image from here and draw the cursor on top of it
    img = playfield_to_img(playfield)

    x, y = cursor # These coordinates are of the left block on the cursor

    # p1 is the top left of the cursor
    # p2 is the bottom right of the cursor
    p1 = (16 * x, 16 * y)
    p2 = (16 * (x + 2) - 1, 16 * (y + 1) - 1)
    c = (255, 251, 255) # Cursor color

    cv2.rectangle(img, p1, p2, c, 2)

    return img
