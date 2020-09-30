import sys
sys.path.insert(0, "..") # imager.py is in the directory above!

import cProfile
import cv2
import os

import imager

def benchmark_playfield(img):
    """
    Benchmark how many function calls it takes to process the playfield image
    and how long each function takes.

    @param img: Image of the playfield.
    """

    cProfile.runctx("imager.img_to_playfield(img)",
                    globals=globals(),
                    locals=locals())

def main():
    # Directory towards my list of images!
    dir = os.path.join(os.path.dirname(__file__), "../../res/playfields")

    for i in os.listdir(dir):
        filename = "../../res/playfields/{}".format(i)
        try:
            img = cv2.imread(filename)
        except:
            continue

        if (img is None):
            continue

        benchmark_playfield(img)

if __name__ == "__main__":
    main()
