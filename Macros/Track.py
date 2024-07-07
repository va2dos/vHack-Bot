import time
import pyautogui as pag
pag.FAILSAFE = True

def Track_Nouse():
    try:
        while True:
            print(pag.position())
            time.sleep(1)
    except KeyboardInterrupt:
        pass