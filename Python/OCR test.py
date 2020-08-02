from pytesseract import *
from PIL import Image

fil = Image.open("hej.png")

print(image_to_string(fil, config="", lang = "dan"))
