import time
import pyautogui as pag
from random import randrange, uniform
from Utils import config
from BlueHackWindow import GetElement, check_connection
pag.FAILSAFE = True

BlueHackImages = {
    'network_exploit': ['images/network_exploit.png', 'Network Exploit'],
    'network_max': ['images/network_max_reach.png', 'Network Max Reach'],
    'network_target': ['images/network_target.png', 'Network Target'],
}

# Icon 750, 330
MouseCords = {
    'Network Icon': [750, 330]
}

## TODO OCR Over Target's stats

TargetPositions = [[685,725],[685,763],[685,796],[685,831],[685,868],
                   [1230,725],[1230,763],[1230,796],[1230,831],[1230,868]]

def click_wait(x, y):
    cX = randrange(10) - 5 + x
    cY = randrange(10) - 5 + y
    pag.click(cX, cY)
    time.sleep(uniform(0.5, 1.1))

def Farm_Network():
    #Target icon, low conficence threshold so may get random selection
    network_x, network_y = MouseCords['Network Icon'][0], MouseCords['Network Icon'][1]
    click_wait(network_x, network_y)

    target_cursor = 0

    try:
        while check_connection(0): # Continuously attack targets until no more energy

            target_x, target_y = TargetPositions[target_cursor]
            target_cursor += 1
            if target_cursor == 10: target_cursor = 0

            click_wait(target_x, target_y)

            eploit_btn_found,(eploit_x, eploit_y) = GetElement(BlueHackImages['network_exploit'][0], 0.90)
            if eploit_btn_found == False:
                # Target not attackable
                continue

            click_wait(eploit_x, eploit_y)

            max_reach,(_,_) = GetElement(BlueHackImages['network_max'][0], 0.95)
            if max_reach == True:
                print('Limit Reach!') 
                break

    except KeyboardInterrupt:
        pass

    print('Completed Network Farm.')

