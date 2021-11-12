import keyboard

clickedKeys = [2]


def detect_combos(keys):
    if keys[-3:] == [":", "="]:
        pass


while True:
    if len(clickedKeys) >= 5:
        clickedKeys.pop(0)
    clickedKeys.append(keyboard.read_key())
    print(clickedKeys)
