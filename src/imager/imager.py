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

def img_to_playfield(img):
    """
    Convert the image from the game into the playfield list that can be solved
    by the solver.

    @param img: Image of the playfield.
    @return: State of the playfield.
    """

    playfield = [[0 for x in range(6)] for y in range(12)]

    colors = [
        (0, 0, 255),     # Red
        (0, 255, 0),     # Green
        (255, 0, 255),   # Purple
        (0, 255, 255),   # Yellow
        (255, 255, 0),   # Cyan
        (255, 128, 64)   # Dark Blue (These blocks have a weird center color)
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

def playfield_to_img(playfield):
    """
    Create an image of the playfield to be displayed to the user!

    @param playfield: State of the playfield.
    @return: Image of the playfield.
    """

    img = numpy.zeros((16 * 12, 16 * 6, 3), numpy.uint8)

    colors = [
        (255, 255, 255), # White
        (0, 0, 255),     # Red
        (0, 255, 0),     # Green
        (255, 0, 255),   # Purple
        (0, 255, 255),   # Yellow
        (255, 255, 0),   # Cyan
        (255, 0, 0)      # Dark Blue
    ]

    for y in range(12):
        for x in range(6):
            # p1 is the top left of the rectangle
            # p2 is the bottom right of the rectangle
            p1 = (16 * x, 16 * y)
            p2 = (16 * x + (16 - 1), 16 * y + (16 - 1))
            c = colors[playfield[y][x]]

            cv2.rectangle(img, p1, p2, c, cv2.FILLED)

    return img
