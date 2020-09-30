import cv2

def crop_to_playfield(img):
    """
    Crop the capture of the game feed to the playfield only.

    @param: Image of the game feed.
    @return: Image of the playfield.
    """

    cv2.resize(img, (256, 224))

    x1, y1 = (88, 23) # Top Left
    x2, y2 = (x1  + 16 * 6, y1 + 16 * 12) # Bottom Right

    return img[y1:y2, x1:x2]
