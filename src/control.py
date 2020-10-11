import keyboard
import time

def move_right():
    """
    Move the cursor 1 block to the right.
    """

    keyboard.press("d")
    time.sleep(2/60)
    keyboard.release("d")
    time.sleep(2/60)

def move_left():
    """
    Move the cursor 1 block to the left.
    """

    keyboard.press("a")
    time.sleep(2/60)
    keyboard.release("a")
    time.sleep(2/60)

def move_up():
    """
    Move the cursor 1 block to the top.
    """

    keyboard.press("w")
    time.sleep(2/60)
    keyboard.release("w")
    time.sleep(2/60)

def move_down():
    """
    Move the cursor 1 block to the bottom.
    """

    keyboard.press("s")
    time.sleep(2/60)
    keyboard.release("s")
    time.sleep(2/60)

def swap_blocks():
    """
    Make the cursor swap the blocks.
    """

    keyboard.press("z")
    time.sleep(2/60)
    keyboard.release("z")
    time.sleep(2/60)

def make_move(current, destination):
    """
    Move the cursor to the designated spot and swap the block.

    @param current: Current position of the cursor.
    @param destination: Destination position of the cursor.
    """

    x1, y1 = current
    x2, y2 = destination

    while x1 < x2:
        move_right()
        x1 += 1

    while x1 > x2:
        move_left()
        x1 -= 1

    while y1 > y2:
        move_up()
        y1 -= 1

    while y1 < y2:
        move_down()
        y1 += 1

    swap_blocks()
