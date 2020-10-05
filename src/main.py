import cv2
import os
import win32gui

import capture
import logic
import imager
import solver

def main():
    # Pulling the capture information from the desktop, using the Windowed
    # Projector in OBS Studio is a great way to capture game feed without any
    # borders of windows.
    hwnd = win32gui.FindWindow(None, "Windowed Projector (Source) - Game Capture")
    rect = capture.get_window_rect(hwnd)

    prev_moves = None
    prev_playfield = None

    # Constantly be monitoring that window to solve the puzzles as they come
    # across the game feed.
    while True:
        img = capture.capture_window(hwnd, rect)

        # Pull the important image information from the capture
        playfield_img = capture.crop_to_playfield(img)
        moves_img = capture.crop_to_moves(img)

        # Process these smaller images into the game states
        playfield = imager.img_to_playfield(playfield_img)
        moves = imager.img_to_moves(moves_img)

        # Inbetween puzzles the count will be 0, we can't solve and shouldn't
        if (moves == 0):
            continue

        # We should probably wait until the playfield is in a stable state.
        if logic.clear_matches(playfield) or logic.fall_blocks(playfield):
            continue

        # To prevent reevaluating the same puzzle that we just displayed an
        # an image for, we should just continue until we find a new one.
        if (prev_moves == moves and prev_playfield == playfield):
            continue
        else:
            prev_moves = moves
            prev_playfield = [i[:] for i in playfield]

        if solver.is_solvable(moves, playfield):
            solved = imager.combined_to_img(playfield, solver.solution[-1])

            cv2.imshow("Puzzle Solution", solved)
            cv2.waitKey(1)

if __name__ == "__main__":
    main()
