import pyautogui, time, pathlib

time.sleep(10)

path = pathlib.Path().parent.absolute()
path_italo = str(path)
path_italo2 = path_italo + r"\\teamoitalo.txt"

f = open(path_italo2)

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")