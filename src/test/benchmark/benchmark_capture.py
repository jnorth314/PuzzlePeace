import sys
sys.path.insert(0, "../..") # capture.py is in the directory above!

import cProfile
import cv2
import os

import capture

def benchmark_capture(img):
    """
    Benchmark how many function calls it takes to process the game feed image
    and how long each function takes.

    @param img: Image of the game feed.
    """

    cProfile.runctx("capture.crop_to_playfield(img)",
                    globals=globals(),
                    locals=locals())

def main():
    # Directory towards my list of images!
    dir = os.path.join(os.path.dirname(__file__), "../../../res/captures")

    for i in os.listdir(dir):
        filename = "../../../res/captures/{}".format(i)
        try:
            img = cv2.imread(filename)
        except:
            continue

        if (img is None):
            continue

        benchmark_capture(img)

if __name__ == "__main__":
    main()
