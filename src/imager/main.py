import cv2
import os

import imager

def main():
    # Directory towards my list of images!
    dir = os.path.join(os.path.dirname(__file__), "../../images")

    for i in os.listdir(dir):
        filename = "../../images/{}".format(i)
        try:
            img = cv2.imread(filename)
        except:
            continue

        if (img is None):
            continue

        playfield = imager.img_to_playfield(img)
        cursor = imager.img_to_cursor(img)

        # Concatenate the images side by side for easy comparison
        img = cv2.hconcat([img, imager.playfield_to_img(playfield)])

        cv2.imshow("Img vs Playfield", img)
        cv2.waitKey(0)

if __name__ == "__main__":
    main()
