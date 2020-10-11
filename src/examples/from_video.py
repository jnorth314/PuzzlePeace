import sys
sys.path.insert(0, "..") # src is in the directory above!

import cv2
import keyboard
import os
import win32gui

import capture
import control
import logic
import imager
import solver

def main():
    # Pulling the capture information from the desktop, using the Windowed
    # Projector in OBS Studio is a great way to capture game feed without any
    # borders of windows.
    hwnd = win32gui.FindWindow(None, "Windowed Projector (Source) - Game Capture")
    rect = capture.get_window_rect(hwnd)

    # State of the game in the previous captured frame.
    previous = (None, None)

    # Constantly be monitoring that window to solve the puzzles as they come
    # across the game feed.
    while True:
        img = capture.capture_window(hwnd, rect)

        # Pull the important image information from the capture
        images = (capture.crop_to_moves(img), capture.crop_to_playfield(img))

        # Process these smaller images into the game states
        moves = imager.img_to_moves(images[0])
        playfield = imager.img_to_playfield(images[1])
        cursor = imager.img_to_cursor(images[1])

        # Waits for a specific hotkey on the keyboard for automated control of
        # the game, there are also additional checks making sure that a solution
        # does exist and it properly read the cursor position.
        if (keyboard.is_pressed("q")
                and len(solver.solution) > 0
                and cursor[0] != -1
                and cursor[1] != -1):
            control.make_move(cursor, solver.solution[-1])

        # Inbetween puzzles the count will be 0, we can't solve and shouldn't
        if (moves == 0):
            continue

        # We should probably wait until the playfield is in a stable state.
        if logic.clear_matches(playfield) or logic.fall_blocks(playfield):
            continue

        # To prevent reevaluating the same puzzle that we just displayed an
        # an image for, we should just continue until we find a new one.
        if (previous[0] == moves and previous[1] == playfield):
            continue
        else:
            previous = (moves, [i[:] for i in playfield])

        if solver.is_solvable(moves, playfield):
            solved = imager.combined_to_img(playfield, solver.solution[-1])
            #solved = imager.solution_to_img(playfield, solver.solution[::-1])

            cv2.imshow("Puzzle Solution", solved)
            cv2.waitKey(1)

if __name__ == "__main__":
    main()
