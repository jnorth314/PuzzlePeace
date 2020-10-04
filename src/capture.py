import cv2
import numpy
import win32ui
import win32gui
import win32con

def capture_window(hwnd, rect):
    """
    Uses the windows API to capture a region from a window.

    @param hwnd: Handle to the window.
    @param rect: Bounding box of the region
    @return: Image of the window's region
    """

    width = rect[2] - rect[0]
    height = rect[3]- rect[1]

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(bmp)
    cDC.BitBlt((0, 0), (width, height), dcObj, (rect[0], rect[1]), win32con.SRCCOPY)

    img = bmp.GetBitmapBits(True)
    img = numpy.frombuffer(img, dtype='uint8')
    img.shape = (height, width, 4)

    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(bmp.GetHandle())

    return img

def get_window_rect(hwnd):
    """
    Get the rect of the window relative to client without borders.

    @param hwnd: Handle to the window.
    @return: Bounding box of the window's region.
    """

    rect = win32gui.GetWindowRect(hwnd)

    # Left = 8 pixels of border
    # Top = 30 pixels of border
    # Right = 8 pixels of border
    # Bottom = 8 pixels of border
    rect = (8, 30, rect[2] - rect[0] - 8, rect[3] - rect[1] - 8)

    return rect

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

def crop_to_moves(img):
    """
    Crop the capture of the game feed to the moves only.

    @param: Image of the game feed.
    @return: Image of the number of moves.
    """

    cv2.resize(img, (256, 224))

    x1, y1 = (195, 59) # Top Left
    x2, y2 = (x1 + 42, y1 + 48)

    return img[y1:y2, x1:x2]
