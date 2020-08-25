import pyscreenshot as imggrab
from time import sleep
import ctypes
from os import system


def setup():
    system("mode con: cols=15 lines=2")

    """LF_FACESIZE = 32
    STD_OUTPUT_HANDLE = -11

    class COORD(ctypes.Structure):
        _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    class CONSOLE_FONT_INFOEX(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("nFont", ctypes.c_ulong),
                    ("dwFontSize", COORD),
                    ("FontFamily", ctypes.c_uint),
                    ("FontWeight", ctypes.c_uint),
                    ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

    font = CONSOLE_FONT_INFOEX()
    font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
    font.dwFontSize.X = 45
    font.dwFontSize.Y = 45
    font.FontFamily = 60

    handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    ctypes.windll.kernel32.SetCurrentConsoleFontEx(
            handle, ctypes.c_long(False), ctypes.pointer(font))"""


def get_bomb_status():
    img = imggrab.grab(bbox=(945, 27, 946, 28))
    rgb_pixel_value = img.getpixel((0, 0))

    if rgb_pixel_value == (230, 0, 0) or rgb_pixel_value == (170, 0, 0):
        return True
    else:
        return False

setup()
while True:
    if get_bomb_status() and bombtime >=0:
        sleep(.69)
        bombtime -=1
    else:
        bombtime = 45
    print(bombtime)
