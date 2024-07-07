import json
import os
import random
import time
import pyautogui as pag
pag.FAILSAFE = True

def get_config():
    filename = 'config.json'
    if not os.path.isfile(filename):
        return 'config.json not found, download it from the repo.'
    else:
        with open(filename, 'r') as fp:
            config = json.load(fp)
        return config

config = get_config()
