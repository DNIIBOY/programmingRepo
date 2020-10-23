import pyperclip

while True:
    pyperclip.copy(" ".join([":regional_indicator_" + i.lower() + ":" if i != " " else "   " for i in input()]))
