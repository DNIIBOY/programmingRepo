import numpy as np
import cv2
from PIL import ImageGrab
from pytesseract import *

def box():
    img = ImageGrab.grab(bbox=(10, 200, 500, 300)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    cv2.waitKey(0)


while True:
    box()
    cv2.destroyAllWindows()